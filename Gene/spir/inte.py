import importlib.util
import os

spec = importlib.util.spec_from_file_location("Modu", os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Pyth" + os.sep + "Modu" + os.sep + "Modu.py")
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
	#import random

	print()

	# TODO
	# bad rebuilding
	# polygons
	# organize and comment

	# get a list of polys belonging to all edges
	# TODO: add all these kinds of functions to Blen.py
	edgePolyList = []
	edgeList = Blen.EdgeList()
	polyList = Blen.PolyList()
	for a in range(len(edgeList)):
		edgePolyList.append([])
		ver1 = edgeList[a][0]
		ver2 = edgeList[a][1]
		for b in range(len(polyList)):
			if (ver1 in polyList[b]) and (ver2 in polyList[b]):
				edgePolyList[len(edgePolyList) - 1].append(b)
		#edgePolyList[a] = sorted(edgePolyList[a], reverse = True)

	pop_List = []
	appeList = []
	# TODO: make anglTole maybe
	tole = 0.001
	vertList = Blen.VertList()
	# TODO: super slow
	for a in range(0, len(edgeList)):
		for b in range(len(edgeList)):
			if a != b:
				e1v1 = edgeList[a][0]
				e1v2 = edgeList[a][1]
				e2v1 = edgeList[b][0]
				e2v2 = edgeList[b][1]
				if e1v1 != e2v1 and e1v1 != e2v2 and e1v2 != e2v1 and e1v2 != e2v2:
					ori1 = tuple(vertList[e1v1])
					# TODO: make a note in math if this is a problem
					vec1 = Math.VectNorm(Math.Vect(ori1, tuple(vertList[e1v2])))
					ori2 = tuple(vertList[e2v1])
					vec2 = Math.VectNorm(Math.Vect(ori2, tuple(vertList[e2v2])))

					inte = Math.VectInte2d__((ori1[0], ori1[1]), (vec1[0], vec1[1]), (ori2[0], ori2[1]), (vec2[0], vec2[1]))

					# TODO: make all this a function if one doesnt exist
					# TODO: does inte need to be > 0.0
					mag1 = Math.VectMagn(Math.Vect(ori1, tuple(vertList[e1v2])))
					if type(inte) == float and inte > 0.0 and inte < mag1 - tole:

						# TODO: redundant
						mag2 = Math.VectMagn(Math.Vect(ori2, tuple(vertList[e2v2])))

						# get a vector that represents inte
						inte = Math.VectScal(Math.VectNorm(vec1), inte)
						# check if inte vect and vec1 are pointing in the same direction
						dot_ = Math.VectDot_(vec1, inte)
						# get world point of inte
						inte = Math.VectAdd_(ori1, inte)

						# TODO: doesnt seem like this should need to be done
						if dot_ > 0.0:

							# get a vector from ori2 to inte
							vect = Math.Vect(ori2, inte)
							# check if vec2 and ^ have the same angle
							#angl = 

							if Math.VectAngl(vect, vec2) < tole and Math.VectMagn(vect) < mag2 - tole:
								#### split both edges at inte
								# delete edges
								pop_List.append(a)
								pop_List.append(b)
								# add two new edges for each old edge
								appeList.append(((inte[0], inte[1], 0.0), (vertList[e1v1], vertList[e1v2], vertList[e2v1], vertList[e2v2])))
								#### split polygons belonging to edges
								#for poly in edgePolyList[a]:

	pop_List = sorted(pop_List)
	# purge duplicates in pop_List
	a = len(pop_List) - 1
	while a > 0:
		if pop_List[a - 1] == pop_List[a]:
			pop_List.pop(a)
		a -= 1
	# remove edges marked for deletion
	a = len(pop_List) - 1
	while a >= 0:
		edgeList.pop(pop_List[a])
		a -= 1

	for a in range(len(appeList)):
		vertList.append(appeList[a][0])
		# TODO: super slow
		ver0 = Blen.VertIndeBy__Loca(appeList[a][1][0])
		ver1 = Blen.VertIndeBy__Loca(appeList[a][1][1])
		ver2 = Blen.VertIndeBy__Loca(appeList[a][1][2])
		ver3 = Blen.VertIndeBy__Loca(appeList[a][1][3])
		edgeList.append((len(vertList) - 1, ver0))
		edgeList.append((len(vertList) - 1, ver1))
		edgeList.append((len(vertList) - 1, ver2))
		edgeList.append((len(vertList) - 1, ver3))

	Blen.Dele()
	Blen.Uplo([vertList, edgeList, []])
	# TODO
	Blen.VertDoub()

main()

