import importlib.util
import os

spec = importlib.util.spec_from_file_location("Modu", os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Modu" + os.sep + "Modu.py")
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
	import math

	exte = False
	try:
		paraDict = para
		exte = True
		direOut = dire + "out_/tree_simp_" + numb + "_para"
	except:
		paraDict = Gene.ParaInit("tree_simp_para")
		direOut = ""
	# write para vars to console if exte is false, or a file if exte is true
	Gene.ParaWrit(para = paraDict, dire = direOut, exte = exte)

	# bevel object for branches
	bpy.data.objects["BezierCircle"].scale[0] = paraDict["beve_x"]
	bpy.data.objects["BezierCircle"].scale[1] = paraDict["beve_y"]
	# taper curve object for branches
	bpy.data.objects["taper"].data.splines[0].bezier_points[0].handle_right.x = paraDict["tape_x"]
	bpy.data.objects["taper"].data.splines[0].bezier_points[1].handle_left.y = paraDict["tape_x"]
	leng = paraDict["leng_star"]
	rend = paraDict["end"] * paraDict["radi"]
	radc = paraDict["radi"]

	cent = (0.0, 0.0, paraDict["heig"])
	vertList = []
	edgeList = []
	sections = []
	# alternate between between +x and -x for spheres with an odd number of segments
	rota = False
	# make point shells
	while radc > rend:
		vert = []
		# get a sphere
		vert, edge, poly = Math.Sphe(segs = paraDict["segs"], ring = paraDict["segs"], cent = cent, radi = radc, distCirc = False)
		if rota == False:
			if int(math.fmod(paraDict["segs"], 2)) == 1:
				rota = True
		else:
			if int(math.fmod(paraDict["segs"], 2)) == 1:
				rota = False
				angl = math.pi / paraDict["segs"]
				a = 0
				while a < len(vert):
					anglPrev = math.atan2(vert[a][1], vert[a][0])
					anglPrev += angl
					rad_ = Math.VectMagn((vert[a][0], vert[a][1]))
					vert[a] = (rad_ * math.cos(anglPrev), rad_ * math.sin(anglPrev), vert[a][2])
					a += 1
		# randomize vertices
		vert = Math.VertListRand(vert, paraDict["fact"])
		# add the new verts to the main list
		vertList += vert[:]
		# track the vert count of each sphere
		sections.append(len(vertList) - 1)
		radc *= paraDict["decr"]
		paraDict["fact"] *= paraDict["decf"]
		paraDict["segs"] *= paraDict["decs"]
		paraDict["segs"] = int(paraDict["segs"])
		if paraDict["segs"] < 3:
			paraDict["segs"] = 3

	# pick a single outside point and work towards the center
	a = 0
	while a < sections[0]:
		next = a
		vert = vertList[a]
		leng = paraDict["leng_star"]
		Blen.Curv()
		poin = bpy.context.object.data.splines[0].bezier_points
		Blen.CurvLoca(0, vert)
		for e in range(1, len(sections)):
			rend = sections[e]
			b = sections[e - 1]
			thisList = vertList[b:rend - 1]
			clos, dist = Math.VectClos(vert, thisList)
			clos += b
			# zigzag towards clos
			# draw lines until they pass target point
			ver2 = vertList[clos]
			# vector from start to end
			vect = Math.Vect(vert, ver2)
			# vector magnitude from one branch tip to another
			# difference between outside starting point and inside ending point. use to check if branching is done
			magn = Math.VectMagn(vect)
			vecc = 0.0
			# list of points that zig-zag from start point to end point
			thisList = []
			thisList.append(vert)
			# length of each zigzag section
			thisLeng = leng
			while vecc < magn:
				poin = bpy.context.object.data.splines[0].bezier_points
				# get a random axis and a random angle for rotation
				x, y, z = Math.VertRand(2.0)
				# zig zag angle
				angl = Math.Rand(paraDict["maxa"])
				# vecn. vector representing previous zigzag section
				if len(thisList) > 1:
					vecn = Math.Vect(thisList[len(thisList) - 2], thisList[len(thisList) - 1])
				else:
					vecn = vect
				# rotate vector a random angle around a random axis
				vecn = Math.Quat(vecn, angl, (x, y, z))
				# add a random variation to the length of the section
				thisVari = thisLeng * paraDict["varl"] * 2.0
				thisVari = Math.Rand(thisVari)
				thisLeng += thisVari
				# set the section to the length thisLeng
				vecn = Math.VectScal(Math.VectNorm(vecn), thisLeng)
				# new world point to connect to
				vecn = Math.VectAdd_(thisList[len(thisList) - 1], vecn)
				# check if branching has passed connecting destination
				vecc = Math.VectMagn(Math.Vect(vert, vecn))
				if vecc < magn:
					if len(thisList) == 1:
						vertList.append(vecn)
						Blen.CurvLoca(len(poin), vecn)
						edgeList.append((next, len(vertList) - 1))
					else:
						vertList.append(vecn)
						Blen.CurvLoca(len(poin), vecn)
						edgeList.append((len(vertList) - 2, len(vertList) - 1))
					thisList.append(vecn)
				else:
					if len(thisList) == 1:
						edgeList.append((next, clos))
					else:
						edgeList.append((len(vertList) - 1, clos))
					Blen.CurvLoca(len(poin), vertList[clos])
					break
				thisLeng *= paraDict["incr"]
			leng *= paraDict["incs"]
			next = clos
			vert = vertList[next]
		poin = bpy.context.object.data.splines[0].bezier_points
		x = poin[len(poin) - 1].co.x
		y = poin[len(poin) - 1].co.y
		Blen.CurvLoca(len(poin), (x, y, 0.0))
		Blen.CurvHand()
		bpy.context.object.data.taper_object = bpy.data.objects["taper"]
		bpy.context.object.data.bevel_object = bpy.data.objects["BezierCircle"]
		bpy.context.object.data.bevel_resolution = 6
		a += 1

	# upload vert / edge lists for reference
	Blen.Uplo([vertList, edgeList, []])

main()

