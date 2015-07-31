.PHONY: view generate

all:

generate:
	blender -b -P generate.py

view:
	blender -P view.py