import math
import random

import importlib.util

def file_to_lines(file_to_open):
	file_obj = open(file_to_open, mode = 'r')
	ret = file_obj.read()
	file_obj.close()
	ret = ret.strip()
	ret = ret.split("\n")
	return ret

filename = "dire"
lines = file_to_lines(filename)
directories = {}
i = 0
while i < len(lines):
	line = lines[i]
	line = line.split("=")
	line[0] = line[0].strip()
	line[1] = line[1].strip()
	directories.update({line[0]:line[1]})
	i += 1

main_dir = directories["main_dir"]
blender_command = directories["blender_command"]
#old = True
old = False
if old == True:
	this_dir = directories["this_dir"]
	python_dir = directories["python_dir"]
	blender_dir = directories["blender_dir"]
	blender_game_dir = directories["blender_game_dir"]
	engine_dir = directories["engine_dir"]
	logic_dir = directories["logic_dir"]
else:
	this_dir = directories["th_dir"]
	python_dir = directories["py_dir"]
	blender_dir = directories["bl_dir"]
	blender_game_dir = directories["bg_dir"]
	engine_dir = directories["en_dir"]
	logic_dir = directories["lo_dir"]

spec = importlib.util.spec_from_file_location("python", python_dir + "python.py")
python = importlib.util.module_from_spec(spec)
spec.loader.exec_module(python)

spec = importlib.util.spec_from_file_location("blender", blender_dir + "blender.py")
blender = importlib.util.module_from_spec(spec)
spec.loader.exec_module(blender)

spec = importlib.util.spec_from_file_location("engine", engine_dir + "engine.py")
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)

spec = importlib.util.spec_from_file_location("blender_game", blender_game_dir + "blender_game.py")
blender_game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(blender_game)

flag_python = "--python"

def main():

	import os

	layers = ["0", "1", "2", "3", "4", "5", "6"]
	#"""
	for layer in layers:
		python.lines_to_file("filenum", "w", [layer])
		# open blend and run script
		syst = blender_command + " -b a/a.blend --python a/a.py"
		os.system(syst)
		# save image
		syst = blender_command + " -b a/a.blend -f 1"
		os.system(syst)
		# move image
		syst = "mv /tmp/0001.png out/" + layer + ".png"
		os.system(syst)
	#"""

	"""
	syst = "mogrify -combine "
	for layer in layers:
		syst += "out/" + layer + ".png "
	#syst += "all.png"
	os.system(syst)
	"""


main()

	
