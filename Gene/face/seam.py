
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
	import random

	impo = True
	#impo = False
	if impo:

		# index 0: name of the vertex group
		# other indices: names of vertex groups that border the vertex group
		overlap_ = []
		overlap_.append(["neck", "chin", "jaw"])
		overlap_.append(["chin", "neck", "jaw", "mouth", "cheeks_lower"])
		overlap_.append(["jaw", "neck", "chin", "mouth"])
		overlap_.append(["mouth", "lips", "jaw", "nose", "cheeks_lower"])
		overlap_.append(["lips", "mouth"])
		overlap_.append(["cheeks_lower", "cheeks_upper", "nose", "jaw"])
		overlap_.append(["cheeks_upper", "cheeks_lower", "nose", "eyesockets", "brow"])
		overlap_.append(["nose", "eyesockets", "mouth", "cheeks_lower", "cheeks_upper"])
		overlap_.append(["eyesockets", "eyes", "nose", "brow", "cheeks_upper"])
		overlap_.append(["eyes", "eyesockets"])
		overlap_.append(["brow", "eyesockets", "nose", "cheeks_upper", "forehead"])
		overlap_.append(["forehead", "brow"])

		# separate each vertex group into a mesh
		for over in overlap_:
			# duplicate mesh
			Blen.Sele("face")
			Blen.Dupl()
			### get a section
			Blen.VertDese()
			Blen.VertGrouSele(over[0])
			Blen.Edit()
			bpy.ops.mesh.select_all(action='INVERT')
			Blen.Edit()
			Blen.VertDele()
			###
			Blen.Name(over[0])

		# get a list of all vertex locations, vertex indices, and the part it belongs to
		vertList = []
		vertInde = []
		grouList = []
		seam = []
		for over in overlap_:
			Blen.Sele(over[0])
			vert = Blen.VertList()
			vertList += vert
			for a in range(len(vert)):
				seam.append([vert[a][0], vert[a][1], vert[a][2], a, over[0]])
		seam = sorted(seam)
		a = 0
		while a < len(seam) - 1:
			if seam[a][0] == seam[a + 1][0]:
				if seam[a][1] > seam[a + 1][1]:
					temp = seam[a]
					seam[a] = seam[a + 1]
					seam[a + 1] = temp
					a = -1
			a += 1
		a = 0
		while a < len(seam) - 1:
			if seam[a][0] == seam[a + 1][0]:
				if seam[a][1] == seam[a + 1][1]:
					if seam[a][2] > seam[a + 1][2]:
						temp = seam[a]
						seam[a] = seam[a + 1]
						seam[a + 1] = temp
						a = -1
			a += 1
		coun = 0
		a = len(seam) - 1
		while a >= 1:
			if seam[a][0] == seam[a - 1][0] and seam[a][1] == seam[a - 1][1] and seam[a][2] == seam[a - 1][2]:
				coun += 1
			else:
				if coun == 0:
					seam.pop(a)
				coun = 0
			a -= 1
		if coun == 0:
			seam.pop(0)
		line = []
		for a in range(len(seam)):
			line.append(str(seam[a][0]) + " " + str(seam[a][1]) + " " + str(seam[a][2]) + " " + str(seam[a][3]) + " " + seam[a][4])
		Pyth.LineTo__File(line, "face/seam/seam")

main()

