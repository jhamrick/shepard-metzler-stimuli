.PHONY: view generate

all:

generate:
	blender -b -P generate_meshes.py
	python generate_scenes.py

edit:
	blender -P view.py

preview:
	mtsgui stimuli/scene/{A,B}_x_2_y_3_z_2_x_-3/*.xml

render:
	python render_images.py