# Import-Export Skinned Graphs

Import/Export Graphs with [Skin Modifier](
https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/skin.html) for Blender


# Instructions

- Download the script and install addon.

- Create or open a .blend file containing a graph with the `Skin` modifier added, but not applied, to the top of the modifier stack. Apply any `Mirror` or `Weld` modifiers added.

- *Select* the mesh and export as a .npz file.

- The .npz file can be imported. Add a few levels of `Subdivision Surface` *below* the `Skin` modifier, and shade smooth using the option in the Skin Modifier panel.   

# File format

The .npz file contains the following arrays:

- `verts`, 3-tuples of floats, the coordinates of the vertices.
- `edges`, 2-tuples of integers, the edges.
- `skin_radii`, 2-tuples of floats, the radii along the x and y axes for each vertex.
- `skin_loose`, Booleans specifiying whether or not the vertex is marked as loose. This only affects "branch vertices", those with three or more connected edges.
- `skin_root`, Booleans specifying whether or not the vertex is marked as root. Only one vertex per set of connected vertices will be treated as the root.
