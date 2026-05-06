import importlib.util
import os

path = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Pyth" + os.sep + "Modu" + os.sep + "Modu.py"
spec = importlib.util.spec_from_file_location("Modu", path)
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

def main():

	import bpy
	import math
	import random

	a = 0
	while a < len(bpy.context.object.data.vertices):
		vert = bpy.context.object.data.vertices[a]
		loc1 = bpy.context.object.data.vertices[a].co
		vectList = []
		b = 0
		while b < len(bpy.context.object.data.vertices):
			
			if a != b:
				loc2 = bpy.context.object.data.vertices[b].co
				vect = Math.Vect(loc1, loc2)
				magn = Math.VectMagn(vect)
				if magn < 1.0:
					vectList.append([magn, b, vect])
		vectList = sorted(vectList)

		# find node
		# get a vector from vectList[0] to node
		# rotate a opposite vector
		#	rotate everything above node

main()

