.PHONY: all meshes scenes preview_mesh preview_scene render

all:

meshes:
	blender -b -P generate_meshes.py

scenes:
	python3 generate_scenes.py

preview_mesh:
	blender -P preview_mesh.py

preview_scene:
	mtsgui stimuli/scene/A_x_2_y_3_z_2_x_-3/A_x_2_y_3_z_2_x_-3_xrot_000_zrot_000_yrot_000.xml

render:
	python3 render_images.py