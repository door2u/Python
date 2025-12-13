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
	#vertList = []
	x = []
	y = []
	z = []
	for obje in bpy.context.scene.objects:
		if (obje.name in exclList) == False:
			Blen.Sele(obje.name)
			new_VertList = Blen.VertList()
			#vertList += new_VertList[1 : len(new_VertList)]
			#new_VertList = new_VertList[1 : len(new_VertList)]
			for a in range(1, len(new_VertList)):
				x.append(new_VertList[a][0])
				y.append(new_VertList[a][1])
				z.append(new_VertList[a][2])
	return x, y, z

def Coun(x, y, z, inte, minx, maxx, miny, maxy, minz, maxz, spheRadi, vertPer_Grid, weig, spheLoca):
	import math
	incr = (maxx - minx) / float(inte + 1)
	coun = []
	for a in range(inte ** 3):
		coun.append(0)
	scorSphe = 0.0
	scorDist = 0.0
	scorIdea = 0.0
	for a in range(len(x)):
		coux = int((x[a] - minx) / incr)
		couy = int((y[a] - miny) / incr)
		couz = int((z[a] - minz) / incr)
		inde = couz * (inte ** 2) + couy * inte + coux
		if inde < len(coun):
			magn = Math.Vect(spheLoca, (x[a], y[a], z[a]))
			magn = Math.VectMagn(magn)
			magn -= spheRadi
			if magn >= 0.0:
				scorSphe += magn * weig
				#inde = couz * (inte ** 2) + couy * inte + coux
				#if inde < len(coun):
				coun[inde] = vertPer_Grid
			else:
				coun[inde] += 1.0
		#		print("overflow", "index", inde, "of", len(coun), couz, couy, coux)
	for a in range(len(coun)):

		coux = int(math.fmod(a, inte))
		couy = int(math.fmod((a - coux) / inte, inte))
		couz = int(math.fmod((((a - coux) / inte) - couy) / inte, inte))
		#print(a, coux, couy, couz)
		# get minimum radius
		xsig = coux >= inte / 2.0
		ysig = couy >= inte / 2.0
		zsig = couz >= inte / 2.0
		if xsig == False:
			xmin = (coux + 1) * incr
			#xmax = coux * incr
		else:
			#xmax = (coux + 1) * incr
			xmin = coux * incr
		xmin = xmin - spheRadi
		#xmax = xmax - spheRadi
		if ysig == False:
			ymin = (couy + 1) * incr
			#ymax = couy * incr
		else:
			#ymax = (couy + 1) * incr
			ymin = couy * incr
		ymin = ymin - spheRadi
		#ymax = ymax - spheRadi
		if zsig == False:
			zmin = (couz + 1) * incr
			#zmax = couz * incr
		else:
			#zmax = (couz + 1) * incr
			zmin = couz * incr
		zmin = zmin - spheRadi
		#zmax = zmax - spheRadi
		mini = (xmin, ymin, zmin)
		miniMagn = Math.VectMagn(mini)
		#maxi = (xmax, ymax, zmax)
		#maxiMagn = Math.VectMagn(maxi)
		if miniMagn > spheRadi:
			#inde = couz * (inte ** 2) + couy * inte + coux
			#if inde < len(coun):
			coun[a] = vertPer_Grid

		scorDist += coun[a]
		scorIdea += vertPer_Grid
	scorDist = math.fabs(scorDist - scorIdea)
	scor = scorDist + scorSphe
	return scor

def main():
	import bpy
	import math
	import random
	# TODO
	# score assumes a section is fully inside the sphere
	# BranSepa messes up if object is named obje
	# get content directory working
	# read global vertices
	# set maximum points and randomize until maximum points are reached, then distribute again

	# TODO: experiment. sort an equation according to ooo

	print()

	inte = 32
	spheLoca = (0.0, 0.0, 4.5)
	spheRadi = 2.4
	cubeLoca = (0.0, 0.0, 4.5)
	cubeRadi = 2.4
	# how much to multiply (or penalize) vertices that fall outside of the sphere
	weig = 2.0
	pare = 0
	iterCoun = 100
	beehCoun = 5

	branPare = [-1, 0, 0, 1, 2, 3, 0, 3, 7, 0, 1, 2, 3, 9, 10, 11, 13, 15, 1, 2, 6, 9, 10, 11, 19, 20, 23, 25, 0, 1, 2, 10, 18, 19, 21, 29, 30, 31, 32, 34, 0, 2, 6, 9, 10, 11, 18, 19, 20, 21, 28, 30, 31, 32, 33, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 53, 55, 56, 57, 58, 1, 2, 6, 9, 19, 20, 28, 30, 32, 40, 43, 46, 47, 50, 55, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 87, 88, 89, 0, 1, 28, 32, 40, 41, 42, 43, 46, 71, 75, 78, 80, 81, 102, 104, 105, 107, 108, 109, 114, 116, 117, 0, 1, 2, 6, 9, 19, 28, 30, 40, 41, 42, 72, 73, 77, 80, 102, 103, 106, 107, 108, 109, 116, 125, 127, 128, 129, 131, 133, 135, 136, 137, 138, 139, 140, 142, 144, 145, 147, 149, 150, 151, 152, 6, 9, 30, 40, 41, 42, 43, 72, 73, 74, 77, 102, 104, 106, 127, 129, 131, 133, 134, 135, 136, 137, 138, 142, 147, 168, 169, 170, 171, 174, 175, 177, 178, 179, 180, 181, 183, 185, 186, 188, 191, 192, 194, 199, 0, 6, 28, 72, 73, 102, 104, 106, 127, 128, 129, 131, 133, 137, 140, 147, 167, 168, 171, 173, 174, 175, 176, 177, 179, 180, 182, 183, 184, 191, 211, 214, 215, 216, 217, 218, 219, 222, 225, 226, 227, 228, 232, 233, 235, 0, 9, 28, 40, 42, 43, 73, 74, 77, 102, 104, 128, 129, 133, 147, 167, 168, 170, 175, 176, 178, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 226, 227, 228, 257, 258, 259, 260, 262, 263, 265, 266, 267, 268, 269, 271, 272, 273, 275, 276, 277, 278, 279, 281, 282, 283, 285, 286, 287, 288, 292, 293, 294, 304, 312, 321, 0, 6, 9, 28, 40, 102, 106, 128, 131, 147, 167, 168, 170, 175, 178, 211, 212, 213, 215, 216, 217, 221, 222, 256, 257, 258, 259, 262, 263, 265, 267, 268, 269, 270, 271, 276, 279, 282, 312, 324, 327, 329, 331, 332, 333, 334, 335, 336, 338, 340, 341, 342, 345, 346, 347, 348, 349, 350, 353, 354, 355, 356, 357, 361, 363, 364, 365, 369, 390, 0, 28, 40, 74, 102, 104, 128, 129, 131, 167, 168, 170, 213, 216, 256, 257, 258, 259, 265, 267, 268, 273, 282, 324, 326, 327, 328, 329, 331, 332, 333, 335, 336, 341, 348, 349, 350, 353, 361, 365, 390, 393, 394, 395, 397, 399, 400, 401, 402, 403, 404, 405, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 422, 424, 425, 428, 429, 432, 434, 435, 436, 437, 444, 0, 40, 102, 133, 170, 212, 213, 257, 258, 259, 265, 324, 326, 327, 328, 332, 335, 336, 341, 365, 394, 395, 397, 399, 400, 401, 402, 403, 404, 405, 408, 409, 410, 411, 419, 432, 470, 471, 475, 476, 477, 478, 479, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 493, 494, 496, 497, 498, 500, 501, 502, 503, 505, 506, 507, 510, 523, 532, 534, 0, 40, 102, 131, 168, 213, 256, 257, 258, 259, 265, 268, 324, 327, 328, 365, 393, 394, 395, 397, 400, 401, 403, 404, 405, 409, 410, 432, 469, 471, 473, 475, 476, 477, 480, 482, 483, 488, 489, 490, 491, 505, 507, 539, 540, 541, 543, 544, 546, 547, 548, 549, 551, 552, 553, 555, 556, 557, 558, 560, 561, 562, 563, 564, 565, 567, 568, 569, 570, 571, 572, 574, 575, 576, 578, 580, 581, 582, 583, 584, 588, 589, 592, 593, 597, 0, 28, 40, 102, 170, 213, 258, 259, 326, 327, 328, 365, 393, 394, 395, 397, 405, 469, 470, 471, 473, 478, 482, 483, 488, 505, 507, 539, 540, 543, 546, 547, 548, 549, 552, 553, 554, 555, 556, 557, 558, 570, 583, 597, 627, 629, 630, 631, 633, 634, 636, 637, 638, 640, 641, 645, 647, 648, 649, 650, 651, 652, 655, 656, 658, 659, 660, 662, 663, 664, 665, 670, 671, 673, 0, 28, 213, 257, 258, 259, 327, 394, 397, 469, 470, 475, 477, 505, 507, 539, 540, 541, 547, 548, 552, 553, 556, 557, 558, 570, 597, 627, 630, 631, 633, 634, 635, 636, 637, 638, 641, 643, 649, 652, 664, 698, 699, 700, 702, 703, 704, 705, 706, 708, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 732, 733, 735, 738, 739, 744, 28, 213, 327, 328, 393, 394, 395, 470, 505, 539, 540, 541, 547, 548, 552, 553, 627, 630, 631, 633, 634, 637, 638, 652, 698, 702, 703, 704, 705, 711, 715, 716, 722, 774, 775, 776, 777, 779, 780, 782, 783, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 811, 812, 258, 259, 394, 395, 469, 540, 630, 631, 633, 634, 702, 703, 704, 705, 714, 776, 777, 780, 782, 784, 785, 838, 840, 841, 842, 843, 844, 845, 847, 849, 850, 851, 852, 854, 258, 259, 327, 328, 394, 471, 505, 704, 777, 780, 784, 838, 873, 876, 877, 878, 879, 880, 881, 328, 394, 395, 540, 838, 892]
	x, y, z = ScenVertList(exclList = ["obje.000"])
	# TODO: make center / radius the same
	vertCoun = len(x)
	spheVolu = (4.0 / 3.0) * math.pi * spheRadi ** 2.0
	sectVolu = (2.0 * cubeRadi / (inte + 1)) ** 3.0
	vertPer_Grid = vertCoun * sectVolu / spheVolu
	scorPrev = Coun(x, y, z, inte, cubeLoca[0] - cubeRadi, cubeLoca[0] + cubeRadi, cubeLoca[1] - cubeRadi, cubeLoca[1] + cubeRadi, cubeLoca[2] - cubeRadi, cubeLoca[2] + cubeRadi, spheRadi, vertPer_Grid, weig, spheLoca)
	objeCoun = len(bpy.data.objects)
	iter = 0
	while iter < iterCoun:
		# hard-coded above for effeciency
		#branPare = BranSepa()
		#print(branPare)
		#obje = 0
		#while branPare[obje] != pare:
		#random.seed()
		#obje = random.randint(1, objeCoun - 1)

		random.seed()
		obje = random.random()
		#obje = 2.0 ** obje - 1.0
		#obje = (3.0 ** obje - 1.0) / 2.0
		obje = (4.0 ** obje - 1.0) / 3.0
		obje = round(obje * float(objeCoun - 2))
		obje += 1
		#print(obje, objeCoun - 1)

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
		x, y, z = ScenVertList(exclList = ["obje.000"])
		scorNext = Coun(x, y, z, inte, cubeLoca[0] - cubeRadi, cubeLoca[0] + cubeRadi, cubeLoca[1] - cubeRadi, cubeLoca[1] + cubeRadi, cubeLoca[2] - cubeRadi, cubeLoca[2] + cubeRadi, spheRadi, vertPer_Grid, weig, spheLoca)
		save = False
		print(scorNext, scorPrev)
		if scorNext < scorPrev:
			save = True
		if save or iter < beehCoun:
			print("saving")
			bpy.ops.wm.save_mainfile(check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, compress=False, relative_remap=False)
			x, y, z = ScenVertList(exclList = ["obje.000"])
			scorPrev = scorNext
		else:
			a = 0
			while a < len(chilList):
				Blen.Sele("obje." + Blen.Pad_(chilList[a]))
				for b in range(len(bpy.context.object.data.vertices)):
					vect = bpy.context.object.data.vertices[b].co
					vect = Math.Vect(pivo, vect)
					vect = Math.Quat(vect, -1.0 * rota, Math.VectNorm((axix, axiy, axiz)))
					vect = Math.VectAdd_(pivo, vect)
					bpy.context.object.data.vertices[b].co = vect
				a += 1
		iter += 1

main()

