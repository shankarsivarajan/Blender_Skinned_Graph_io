bl_info = {
  "name": "Skinned graph",
  "author": "Shankar Sivarajan",
  "blender": (3,2,0),
  "version": (1,0, 2),
  "location": "File > Import-Export",
  "description": "Import-Export graphs with skin modifier",
  "category": "Import-Export",
}

import bpy

import numpy as np

from pathlib import Path

from bpy_extras.io_utils import ImportHelper, ExportHelper

class ImportGraph(bpy.types.Operator, ImportHelper):
    bl_idname = "import_graph.npz"
    bl_label = "Import Skinned Graph"
    
    bl_description = "Import graph with skin modifier"
    # bl_options = {'UNDO'}
  
    filename_ext = ".npz";
  
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
  
    filter_glob: bpy.props.StringProperty(
        default="*.npz",
        options={"HIDDEN"},
    )
  
    @classmethod
    def poll(cls, context):
      return True
  
    def execute(self, context):
        
        filename = self.filepath
        file = np.load(filename)
        
        verts_list = file['verts']
        edges_list = file['edges']
      
        verts = []
        edges = []

        for vert in verts_list:
            verts.append(vert)      
         
        for edge in edges_list:
            edges.append(edge) 
            
        skin_radii = file['skin_radii']
        skin_loose = file['skin_loose']
        skin_root = file['skin_root']
          
        name = Path(filename).stem
        me = bpy.data.meshes.new(name)
          
        me.from_pydata(verts, edges, [])
          
        ob = bpy.data.objects.new(name, me)
          
        col = bpy.context.collection
        col.objects.link(ob)
        bpy.context.view_layer.objects.active = ob
        ob.select_set(True)
          
        ob.modifiers.new("Skin", type='SKIN')
        ob.modifiers["Skin"].use_smooth_shade = True
        bpy.ops.object.subdivision_set(level=2)
        
        for i, vert in enumerate(ob.data.skin_vertices[0].data):
            vert.radius[0], vert.radius[1] = skin_radii[i]
            vert.use_loose = skin_loose[i]
            vert.use_root = skin_root[i]
          
        return {'FINISHED'}
  
    def draw(self, context):
        pass



class ExportGraph(bpy.types.Operator, ExportHelper):
    bl_idname = "export_graph.npz"
    bl_label = "Export Skinned Graph"
    
    bl_description = "Save graph with skin modifier"
    # bl_options = {'UNDO'}
  
    filename_ext = ".npz";
  
    filter_glob: bpy.props.StringProperty(
        default="*.npz",
        options={"HIDDEN"},
    )
    
    def execute(self, context):

        selected_objs = context.selected_objects

        filepath = Path(self.filepath)
        
        for ob in selected_objs:
            verts = []
            edges = []
            skin_radii = []
            skin_loose = []
            skin_root = []
            
            for vert in ob.data.vertices:
                verts.append((vert.co[0], vert.co[1], vert.co[2]))
                
            for edge in ob.data.edges:
                edges.append((edge.vertices[0], edge.vertices[1]))
            
            for vert in ob.data.skin_vertices[0].data:
                skin_radii.append((vert.radius[0], vert.radius[1]))
                skin_loose.append(vert.use_loose)
                skin_root.append(vert.use_root)

            np.savez(filepath, verts=verts, edges = edges, 
                     skin_radii = skin_radii, skin_loose=skin_loose, skin_root=skin_root)

        return {'FINISHED'}

    def draw(self, context):
        pass


def menu_import(self, context):
    self.layout.operator(ImportGraph.bl_idname, text="Skinned graph (.npz)")

def menu_export(self, context):
    self.layout.operator(ExportGraph.bl_idname, text="Skinned graph (.npz)")
    
def register():
    bpy.utils.register_class(ImportGraph)
    bpy.utils.register_class(ExportGraph)
    
    bpy.types.TOPBAR_MT_file_import.append(menu_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)

def unregister():
    
    bpy.utils.unregister_class(ImportGraph)
    bpy.utils.unregister_class(ExportGraph)
    
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)
  
if __name__ == "__main__":
  register()
