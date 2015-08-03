.PHONY: all generate_meshes generate_scenes edit preview render

all:

generate_meshes:
	blender -b -P generate_meshes.py

generate_scenes:
	python generate_scenes.py

preview_mesh:
	blender -P view.py

preview_scenes:
	mtsgui stimuli/scene/A_x_2_y_3_z_2_x_-3/A_x_2_y_3_z_2_x_-3_xrot_270_zrot_090_yrot_0*.xml

render:
	python render_images.py