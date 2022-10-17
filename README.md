# Import-Export Skinned Graphs

Import/Export Graphs with [Skin Modifier](
https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/skin.html) for Blender


# Instructions

- Download the script and install as an addon.

- Create or open a .blend file containing a graph with the `Skin` modifier added, but not applied, to the top of the modifier stack. Apply any `Mirror` or `Weld` modifiers added.

- *Select* the mesh and export as a .npz file.

- The .npz file can now be imported. The imported mesh has two levels of `Subdivision Surface`  applied.

![default_cube_skin_graph](https://user-images.githubusercontent.com/16606427/196298264-fed42b9f-ccc1-441a-a54a-98e50b6cd710.png)

# File format

The .npz file contains the following arrays:

- `verts`, 3-tuples of floats, the coordinates of the vertices.
- `edges`, 2-tuples of integers, the edges.
- `skin_radii`, 2-tuples of floats, the radii along the x and y axes for each vertex.
- `skin_loose`, Booleans specifiying whether or not the vertex is marked as loose. This only affects "branch vertices", those with three or more connected edges.
- `skin_root`, Booleans specifying whether or not the vertex is marked as root. Only one vertex per set of connected vertices will be treated as the root.
