.PHONY: all generate generate_meshes generate_scenes edit preview render

all: generate render

generate: generate_meshes generate_scenes

generate_meshes:
	blender -b -P generate_meshes.py

generate_scenes:
	python generate_scenes.py

edit:
	blender -P view.py

preview:
	mtsgui stimuli/scene/A_x_2_y_3_z_2_x_-3/A_x_2_y_3_z_2_x_-3_xrot_000_yrot_000_zrot_*.xml

render:
	python render_images.py