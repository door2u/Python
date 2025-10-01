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

def BranSepa():
	import bpy
	obje = bpy.context.object.name
	founList = []
	for a in range(len(Blen.Vertices())):
		founList.append(False)
	# get first vertex
	vert = Blen.VertListSele()
	vert = vert[0]
	# get connected to first
	conn = Blen.VertConn(vert)
	conn = conn[0]
	# get locations
	vec1 = bpy.context.object.data.vertices[vert].co
	vec2 = bpy.context.object.data.vertices[conn].co
	vect = Math.Vect(vec1, vec2)
	# start a vector list to determine new / old branch by angle
	vectList = [vect]
	# check if every vertex has been accounted for
	founList[vert] = True
	# track indices that make up each branch
	branList = [[vert]]
	# track the branch index that spawned this branch
	branPare = [-1]
	while (False in founList):
		# start at the beginning of the branch list
		a = 0
		leng = len(branList)
		while a < leng:
			# get the last vertex of this branch
			vert = branList[a][len(branList[a]) - 1]
			vect = vectList[a]
			if vert != -1:
				# get connected
				conn = Blen.VertConn(vert)
				appe = False
				# if a node has been found
				if len(conn) > 2:
					# get the location of this vertex
					vec1 = bpy.context.object.data.vertices[vert].co
					# get vertices that havent been previously found
					vertList = []
					for con_ in conn:
						if founList[con_] == False:
							founList[con_] = True
							vertList.append(con_)
							appe = True
					# determine whether to continue previous branch or start a new one
					# connection that has the smallest angle difference between the parent branch continues
					anglDiff = -1.0
					anglSmal = -1
					for ver_ in vertList:
						# get the location of that vertex
						vec2 = bpy.context.object.data.vertices[ver_].co
						vec_ = Math.Vect(vec1, vec2)
						angl = Math.VectAngl(vect, vec_)
						if anglDiff < 0.0 or angl < anglDiff:
							anglDiff = angl
							anglSmal = ver_
					for ver_ in vertList:
						# continue previous branch
						if ver_ == anglSmal:
							branList[a].append(ver_)
						# start a new branch
						else:
							branList.append([vert, ver_])
							branPare.append(a)
							leng = len(branList)
							vec1 = bpy.context.object.data.vertices[vert].co
							vec2 = bpy.context.object.data.vertices[ver_].co
							vectList.append(Math.Vect(vec1, vec2))
				# a node hasnt been found. continue branch
				else:
					# add the connected vertex to this branch
					for con_ in conn:
						if founList[con_] == False:
							founList[con_] = True
							branList[a].append(con_)
							appe = True
							###
							vec1 = bpy.context.object.data.vertices[vert].co
							vec2 = bpy.context.object.data.vertices[con_].co
							vectList[a] = Math.Vect(vec1, vec2)
							###
				# if no new vertices were added, this branch has ended. add an "end" flag of -1
				if appe == False:
					branList[a].append(-1)

			a += 1
	#retu = branList[:]
	retu = branPare[:]
	# TODO: maybe do this elsewhere
	uplo = True
	#uplo = False
	if uplo:
		#adde = False
		for a in range(len(branList)):
			Blen.Sele(obje)
			bra_ = branList[a]
			if bra_[len(bra_) - 1] == -1:
				bra_.pop()
			vertList = Blen.VertLoca(bra_)
			Blen.Uplo([vertList, Math.EdgeLine(len(vertList) - 1), []])
			if bpy.context.object.name == "obje":
				Blen.Name("obje.000")
			#if adde:
			#	# TODO
			#	Blen.Sele("obje")
			#	Blen.Join("obje.001")
			#if adde == False:
			#	adde = True
		#Blen.Name("bran_temp")
	return retu

def ScenVertList(exclList = []):
	import bpy
	vertList = []
	for obje in bpy.context.scene.objects:
		if (obje.name in exclList) == False:
			Blen.Sele(obje.name)
			new_VertList = Blen.VertList()
			vertList += new_VertList[1 : len(new_VertList)]
	return vertList

"""
def Coun():
	import bpy
	
	boun = 8.0
	inte = 20
	incr = boun / float(inte)
	coun = []
	for a in range(inte ** 3):
		coun.append(0)
	coux = 0
	incx = -1.0 * boun / 2.0
	while incx < boun / 2.0:
		incy = -1.0 * boun / 2.0
		couy = 0
		while incy < boun / 2.0:
			incz = 0.0
			couz = 0
			while incz < boun:
				for a in range(len(vertList)):
					x = vertList[a][0]
					y = vertList[a][1]
					z = vertList[a][2]
					if x >= incx and x < incx + incr and y >= incy and y < incy + incr and z >= incz and z < incz + incr:
						coun[couz * (inte ** 2) + couy * inte + coux] += 1
				couz += 1
				incz += incr
			couy += 1
			incy += incr
		coux += 1
		incx += incr
	return coun
"""



def Coun(vertList, inte, minx, maxx, miny, maxy, minz, maxz):
	#boun = 8.0
	#inte = 20
	incr = (maxx - minx) / float(inte)
	coun = []
	for a in range(inte ** 3):
		coun.append(0)
	coux = 0
	incx = minx
	while incx < maxx:
		incy = miny
		couy = 0
		while incy < maxy:
			incz = minz
			couz = 0
			while incz < maxz:
				for a in range(len(vertList)):
					x = vertList[a][0]
					y = vertList[a][1]
					z = vertList[a][2]
					if x >= incx and x < incx + incr and y >= incy and y < incy + incr and z >= incz and z < incz + incr:
						coun[couz * (inte ** 2) + couy * inte + coux] += 1
				couz += 1
				incz += incr
			couy += 1
			incy += incr
		coux += 1
		incx += incr
	return coun

def main():

	import bpy
	import math
	import random

	print()

	# TODO:

	# leave tree separated. dont count root vertices.

	# normalize separation score
	# ideal score:
	#	number of vertices divided by number of grid regions = 1000
	#	x * leng / (inte ** 3) = ideal
	#	x = ideal * (i ** 3) / leng
	# compare given score to ideal instead of lowest?
	# make distributed score and normalize. add values for regions that are empty

	# make sphere score and normalize
	# x * number of vertices = 1000
	# x = 1000 / leng

	# TODO: messes up if object is named obje
	#branPare = BranSepa()
	#print(branPare)

	branPare = [-1, 0, 0, 1, 2, 3, 0, 3, 7, 0, 1, 2, 3, 9, 10, 11, 13, 15, 1, 2, 6, 9, 10, 11, 19, 20, 23, 25, 0, 1, 2, 10, 18, 19, 21, 29, 30, 31, 32, 34, 0, 2, 6, 9, 10, 11, 18, 19, 20, 21, 28, 30, 31, 32, 33, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 53, 55, 56, 57, 58, 1, 2, 6, 9, 19, 20, 28, 30, 32, 40, 43, 46, 47, 50, 55, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 87, 88, 89, 0, 1, 28, 32, 40, 41, 42, 43, 46, 71, 75, 78, 80, 81, 102, 104, 105, 107, 108, 109, 114, 116, 117, 0, 1, 2, 6, 9, 19, 28, 30, 40, 41, 42, 72, 73, 77, 80, 102, 103, 106, 107, 108, 109, 116, 125, 127, 128, 129, 131, 133, 135, 136, 137, 138, 139, 140, 142, 144, 145, 147, 149, 150, 151, 152, 6, 9, 30, 40, 41, 42, 43, 72, 73, 74, 77, 102, 104, 106, 127, 129, 131, 133, 134, 135, 136, 137, 138, 142, 147, 168, 169, 170, 171, 174, 175, 177, 178, 179, 180, 181, 183, 185, 186, 188, 191, 192, 194, 199, 0, 6, 28, 72, 73, 102, 104, 106, 127, 128, 129, 131, 133, 137, 140, 147, 167, 168, 171, 173, 174, 175, 176, 177, 179, 180, 182, 183, 184, 191, 211, 214, 215, 216, 217, 218, 219, 222, 225, 226, 227, 228, 232, 233, 235, 0, 9, 28, 40, 42, 43, 73, 74, 77, 102, 104, 128, 129, 133, 147, 167, 168, 170, 175, 176, 178, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 226, 227, 228, 257, 258, 259, 260, 262, 263, 265, 266, 267, 268, 269, 271, 272, 273, 275, 276, 277, 278, 279, 281, 282, 283, 285, 286, 287, 288, 292, 293, 294, 304, 312, 321, 0, 6, 9, 28, 40, 102, 106, 128, 131, 147, 167, 168, 170, 175, 178, 211, 212, 213, 215, 216, 217, 221, 222, 256, 257, 258, 259, 262, 263, 265, 267, 268, 269, 270, 271, 276, 279, 282, 312, 324, 327, 329, 331, 332, 333, 334, 335, 336, 338, 340, 341, 342, 345, 346, 347, 348, 349, 350, 353, 354, 355, 356, 357, 361, 363, 364, 365, 369, 390, 0, 28, 40, 74, 102, 104, 128, 129, 131, 167, 168, 170, 213, 216, 256, 257, 258, 259, 265, 267, 268, 273, 282, 324, 326, 327, 328, 329, 331, 332, 333, 335, 336, 341, 348, 349, 350, 353, 361, 365, 390, 393, 394, 395, 397, 399, 400, 401, 402, 403, 404, 405, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 422, 424, 425, 428, 429, 432, 434, 435, 436, 437, 444, 0, 40, 102, 133, 170, 212, 213, 257, 258, 259, 265, 324, 326, 327, 328, 332, 335, 336, 341, 365, 394, 395, 397, 399, 400, 401, 402, 403, 404, 405, 408, 409, 410, 411, 419, 432, 470, 471, 475, 476, 477, 478, 479, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 493, 494, 496, 497, 498, 500, 501, 502, 503, 505, 506, 507, 510, 523, 532, 534, 0, 40, 102, 131, 168, 213, 256, 257, 258, 259, 265, 268, 324, 327, 328, 365, 393, 394, 395, 397, 400, 401, 403, 404, 405, 409, 410, 432, 469, 471, 473, 475, 476, 477, 480, 482, 483, 488, 489, 490, 491, 505, 507, 539, 540, 541, 543, 544, 546, 547, 548, 549, 551, 552, 553, 555, 556, 557, 558, 560, 561, 562, 563, 564, 565, 567, 568, 569, 570, 571, 572, 574, 575, 576, 578, 580, 581, 582, 583, 584, 588, 589, 592, 593, 597, 0, 28, 40, 102, 170, 213, 258, 259, 326, 327, 328, 365, 393, 394, 395, 397, 405, 469, 470, 471, 473, 478, 482, 483, 488, 505, 507, 539, 540, 543, 546, 547, 548, 549, 552, 553, 554, 555, 556, 557, 558, 570, 583, 597, 627, 629, 630, 631, 633, 634, 636, 637, 638, 640, 641, 645, 647, 648, 649, 650, 651, 652, 655, 656, 658, 659, 660, 662, 663, 664, 665, 670, 671, 673, 0, 28, 213, 257, 258, 259, 327, 394, 397, 469, 470, 475, 477, 505, 507, 539, 540, 541, 547, 548, 552, 553, 556, 557, 558, 570, 597, 627, 630, 631, 633, 634, 635, 636, 637, 638, 641, 643, 649, 652, 664, 698, 699, 700, 702, 703, 704, 705, 706, 708, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 732, 733, 735, 738, 739, 744, 28, 213, 327, 328, 393, 394, 395, 470, 505, 539, 540, 541, 547, 548, 552, 553, 627, 630, 631, 633, 634, 637, 638, 652, 698, 702, 703, 704, 705, 711, 715, 716, 722, 774, 775, 776, 777, 779, 780, 782, 783, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 811, 812, 258, 259, 394, 395, 469, 540, 630, 631, 633, 634, 702, 703, 704, 705, 714, 776, 777, 780, 782, 784, 785, 838, 840, 841, 842, 843, 844, 845, 847, 849, 850, 851, 852, 854, 258, 259, 327, 328, 394, 471, 505, 704, 777, 780, 784, 838, 873, 876, 877, 878, 879, 880, 881, 328, 394, 395, 540, 838, 892]

	#return 0


	inte = 20

	vertList = ScenVertList(exclList = ["obje.000"])
	vertCoun = len(vertList)

	#idea = 1000.0

	#norm = idea * (inte ** 3) / vertCoun
	#norm = (idea * ((inte ** 3) ** 1)) / vertCoun
	
	#norm = (inte ** 3) / vertCoun
	# ideal count of vertices per grid region
	idea = 1000.0
	scorIdea = vertCoun / idea
	vertPer_Grid = vertCoun / (inte ** 3)
	#print(len(vertList))
	#print(len(vertList[1 : len(vertList)]))

	#return 0

	spheLoca = (0.0, 0.0, 4.3)
	spheRadi = 2.6
	cubeLoca = (0.0, 0.0, 4.3)
	cubeRadi = 3.0

	# different methods

	

	coun = Coun(vertList, inte, cubeLoca[0] - cubeRadi, cubeLoca[0] + cubeRadi, cubeLoca[1] - cubeRadi, cubeLoca[1] + cubeRadi, cubeLoca[2] - cubeRadi, cubeLoca[2] + cubeRadi)
	scorDist = 0.0
	for a in range(len(coun)):
		scorDist += math.fabs(coun[a] - vertPer_Grid)
	scorSphe = 0.0
	for a in range(len(vertList)):
		magn = Math.Vect(spheLoca, vertList[a])
		magn = Math.VectMagn(magn)
		magn -= spheRadi
		if magn > 0.0:
			scorSphe += magn
	scorPrev = scorDist + scorSphe

	#return 0

	#Blen.Sele("tree")
	#Blen.Dele()

	objeCoun = len(bpy.data.objects)
	random.seed()
	obje = random.randint(1, objeCoun - 1)
	
	Blen.Sele(bpy.data.objects[obje].name)
	random.seed()
	rota = 360.0 * random.random()
	random.seed()
	axix = -1.0 + 2.0 * random.random()
	random.seed()
	axiy = -1.0 + 2.0 * random.random()
	random.seed()
	axiz = -1.0 + 2.0 * random.random()

	pivo = bpy.context.object.data.vertices[0].co
	chilList = [obje]
	a = 0
	while a < len(branPare):
		if (a in chilList) == False and (branPare[a] in chilList):
			chilList.append(a)
			a = -1
		a += 1
	a = 0
	while a < len(chilList):
		Blen.Sele("obje." + Blen.Pad_(chilList[a]))
		for b in range(len(bpy.context.object.data.vertices)):
			vect = bpy.context.object.data.vertices[b].co
			vect = Math.Vect(pivo, vect)
			vect = Math.Quat(vect, rota, Math.VectNorm((axix, axiy, axiz)))
			vect = Math.VectAdd_(pivo, vect)
			bpy.context.object.data.vertices[b].co = vect
		a += 1
	#bpy.ops.object.select_all(action = 'SELECT')
	#bpy.ops.object.join()
	#Blen.Name("tree")
	#Blen.VertDoub(threshold = 0.005)
	#counNext = Coun()
	# TODO: how is this not a function? Math?
	#loca = (0.0, 0.0, 0.0)
	#tole = 0.0001
	#for a in range(len(bpy.context.object.data.vertices)):
	#	co = tuple(bpy.context.object.data.vertices[a].co)
	#	co = Math.Vect(loca, co)
	#	co = Math.VectMagn(co)
	#	if co <= tole:
	#		Blen.VertSele([a])
	#		break
	# TODO: get at the beginning
	#leng = len(bpy.context.object.data.vertices)
	save = False
	#if leng == 2221:

	#valuPrev = 0
	#valuNext = 0
	#for a in range(len(counPrev)):
	#	valuPrev += counPrev[a] * counPrev[a]
	#	valuNext += counNext[a] * counNext[a]
	#print(valuPrev, valuNext)
	#if valuNext < valuPrev:
	#	save = True

	vertList = ScenVertList(exclList = ["obje.000"])
	#vertCoun = len(vertList)

	coun = Coun(vertList, inte, cubeLoca[0] - cubeRadi, cubeLoca[0] + cubeRadi, cubeLoca[1] - cubeRadi, cubeLoca[1] + cubeRadi, cubeLoca[2] - cubeRadi, cubeLoca[2] + cubeRadi)
	scorDist = 0.0
	for a in range(len(coun)):
		scorDist += math.fabs(coun[a] - vertPer_Grid)
	scorSphe = 0.0
	for a in range(len(vertList)):
		magn = Math.Vect(spheLoca, vertList[a])
		magn = Math.VectMagn(magn)
		magn -= spheRadi
		if magn > 0.0:
			scorSphe += magn
	scorNext = scorDist + scorSphe

	print(scorNext, scorPrev)
	if scorNext < scorPrev:
		save = True

	#save = False
	if save:
		print("saving")
		bpy.ops.wm.save_mainfile(check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, compress=False, relative_remap=False)

main()

