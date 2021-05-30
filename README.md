# Blender_Skinned_Graph_io
Import/Export Graphs with [Skin Modifier](
https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/skin.html) for Blender


# Instructions

- Download the script and install addon.

- Create or open a .blend file containing a graph with the skin modifier added, but not applied, to the top of the modifier stack.

- *Select* the mesh and export as a .npz file.

- The .npz file can be imported.

# File format

The .npz file contains the following arrays:

- `verts`, 3-tuples of floats, the coordinates of the vertices.
- `edges`, 2-tuples of integers, the edges.
- `skin_radii`, 2-tuples of floats, the radii along the x and y axes for each vertex.
- `skin_loose`, Booleans specifiying whether or not the vertex is marked as loose. Only affects "branch vertices", those with three or more connected edges.
- `skin_root`, Booleans specifying whether or not the vertex is marked as root. Only vertex will be treated as the root.
