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
	import random

	# TODO:
	# how to get started
	# [name the object something other than "obje"]
	# [select the root vertex]
	# [select tree]
	# if a new file is added, dire and pare must be deleted
	# is limi being correctly initialized
	# set spheLoca, spheRadi. these should be read from a file

	# TODO:
	# abitrary padding

	# TODO
	# get new branches to fit in old ones
	# leaves
	# get content directory working. back up low scores
	# move some functions, like BranSepa, to a library
	# fix up prep.py and test whole process

	# TODO
	# better. faster
	# averScor assumes a section is fully inside the sphere
	# can instances be executed with high priority
	# make a gene class for a tree from start to finish and anywhere inbetween

	#print()

	inte = 32
	# TODO
	#spheLoca = (0.0, 0.0, 4.5)
	#spheRadi = 2.4
	#spheLoca = (0.0, 0.0, 2.5)
	#spheRadi = 2.4
	spheLoca = (0.0, 0.0, 5.2)
	spheRadi = 2.7
	# how much to multiply (or penalize) vertices that fall outside of the sphere
	weig = 20.0
	pare = 0
	iterCoun = 100
	#iterCoun = 1
	limiSpre = 150.0
	# attempt limit. how many times should this script be run before direction is reversed
	atteLimi = 100 * (100 / iterCoun)

	dir_, branPare = DirePare()
	#x, y, z, objeIndeList = ScenVertList(exclList = ["obje.000"])
	x, y, z, objeIndeList = ScenVertList(exclList = ["obje.00000"])
	vertPer_Grid = len(x) * ((2.0 * spheRadi / (inte + 1)) ** 3.0) / ((4.0 / 3.0) * math.pi * spheRadi ** 3.0)
	objeCoun = len(bpy.data.objects)
	scorPrev, inde = Coun(x, y, z, inte, spheLoca[0] - spheRadi, spheLoca[0] + spheRadi, spheLoca[1] - spheRadi, spheLoca[1] + spheRadi, spheLoca[2] - spheRadi, spheLoca[2] + spheRadi, spheRadi, vertPer_Grid, weig, spheLoca, objeCoun)
	limiLowe, limi, limiUppe = Limi(scorPrev, limiSpre)
	#print(inde)

	# TODO
	iter = 0
	while iter < iterCoun or dir_ == ['1']:

		if len(bpy.context.scene.objects) == 1:
			branPare = BranSepa()
			#Pyth.LineTo__File([str(branPare)], "flor/tree_spre/pare")
			# TODO
			Pyth.LineTo__File([str(branPare)], "flor/dist/pare")

		if dir_ == ['0']:
			random.seed()
			rand = random.random()
			if len(inde) > 0 and rand < 0.5:
				random.seed()
				obje = random.randint(0, len(inde) - 1)
				obje = inde[obje]
				obje = objeIndeList[obje]
				# TODO: slow
				for a in range(len(bpy.context.scene.objects)):
					if bpy.context.scene.objects[a].name == obje:
						obje = a
						break
				#print(obje)
			else:
				#print("her2")
				obje = ObjePick(objeCoun)
		else:
			random.seed()
			#print(objeCoun)
			obje = random.randint(1, objeCoun - 1)

		#Blen.Sele("obje." + Blen.Pad_(obje))
		#print(obje)
		Blen.Sele("obje." + Pyth.Pad_(obje, 5))
		pivo = bpy.context.object.data.vertices[0].co
		scal, rota, loca = Blen.TranRead()
		pivo = Math.Tran3d__(pivo, scal, rota, loca)

		axis = AxisRand()
		random.seed()
		rota = 360.0 * random.random()

		chilList = ChilList(obje, branPare)
		Rota(chilList, pivo, rota, axis, "obje")

		#x, y, z, objeIndeList = ScenVertList(exclList = ["obje.000"])
		x, y, z, objeIndeList = ScenVertList(exclList = ["obje.00000"])
		scorNext, inde = Coun(x, y, z, inte, spheLoca[0] - spheRadi, spheLoca[0] + spheRadi, spheLoca[1] - spheRadi, spheLoca[1] + spheRadi, spheLoca[2] - spheRadi, spheLoca[2] + spheRadi, spheRadi, vertPer_Grid, weig, spheLoca, objeCoun)
		save = False
		print(iter, scorNext, scorPrev)
		if scorNext < scorPrev:
			save = True
		if dir_ == ['1'] and scorPrev != scorNext and scorNext < limiUppe:
			save = True
		if save:
			print("keeping")
			#x, y, z, objeIndeList = ScenVertList(exclList = ["obje.000"])
			x, y, z, objeIndeList = ScenVertList(exclList = ["obje.00000"])
			scorPrev = scorNext
		else:
			Rota(chilList, pivo, -1.0 * rota, axis, "obje")
		if dir_ == ['1'] and scorPrev >= limi:
			#Pyth.LineTo__File(['0'], "flor/tree_spre/dire")
			# TODO
			Pyth.LineTo__File(['0'], "flor/dist/dire")
			break
		iter += 1
	# TODO:
	# back up trees here
	# also create a skinned renderable version of the tree. maybe run angle fix script too
	if dir_ == ['0'] and scorPrev <= limiLowe:
		#Pyth.LineTo__File(['1'], "flor/tree_spre/dire")
		#Pyth.LineTo__File([str(scorPrev)], "flor/tree_spre/limi")
		# TODO
		Pyth.LineTo__File(['1'], "flor/dist/dire")
		Pyth.LineTo__File([str(scorPrev)], "flor/dist/limi")
		#bpy.data.objects["obje.000"].game.properties["atte"].value = 0
		bpy.data.objects["obje.00000"].game.properties["atte"].value = 0

		####
		# TODO:
		# test
		# is print still needed
		try:
			print(blenPath)
			bpy.ops.wm.save_as_mainfile(filepath = blenPath)
		except:
			pass
		####

	if dir_ == ['0']:
		#atte = bpy.data.objects["obje.000"].game.properties["atte"].value
		#if atte + 1 < atteLimi:
		#   bpy.data.objects["obje.000"].game.properties["atte"].value = atte + 1
		#else:
		#   bpy.data.objects["obje.000"].game.properties["atte"].value = 0
		atte = bpy.data.objects["obje.00000"].game.properties["atte"].value
		if atte + 1 < atteLimi:
			bpy.data.objects["obje.00000"].game.properties["atte"].value = atte + 1
		else:
			bpy.data.objects["obje.00000"].game.properties["atte"].value = 0
			#Pyth.LineTo__File(['1'], "flor/tree_spre/dire")
			# TODO
			Pyth.LineTo__File(['1'], "flor/dist/dire")
	print("saving")
	bpy.ops.wm.save_mainfile()

def DirePare():
	#if os.path.exists("flor/tree_spre/dire"):
	#   dire = Pyth.FileTo__Line("flor/tree_spre/dire")
	# TODO
	if os.path.exists("flor/dist/dire"):
		dire = Pyth.FileTo__Line("flor/dist/dire")
	else:
		dire = ['0']
		#Pyth.LineTo__File(['0'], "flor/tree_spre/dire")
		# TODO
		Pyth.LineTo__File(['0'], "flor/dist/dire")
	#if os.path.exists("flor/tree_spre/pare"):
	# TODO
	if os.path.exists("flor/dist/pare"):
		#branPare = Pyth.FileTo__Line("flor/tree_spre/pare")
		# TODO
		branPare = Pyth.FileTo__Line("flor/dist/pare")
		branPare = branPare[0]
		####
		branPare = branPare.split("[")
		branPare = branPare[1]
		branPare = branPare.split("]")
		branPare = branPare[0]
		###
		branPare = branPare.split(",")
		for a in range(len(branPare)):
			branPare[a] = int(branPare[a])
	else:
		branPare = BranSepa()
		Pyth.LineTo__File([str(branPare)], "flor/dist/pare")
	return dire, branPare

def Limi(scorPrev, limiSpre):
	#if os.path.exists("flor/tree_spre/limi"):
	#   limiLowe = Pyth.FileTo__Line("flor/tree_spre/limi")
	# TODO
	if os.path.exists("flor/dist/limi"):
		limiLowe = Pyth.FileTo__Line("flor/dist/limi")
		limiLowe = float(limiLowe[0])
	else:
		limiLowe = scorPrev - limiSpre
		#Pyth.LineTo__File([str(limiLowe)], "flor/tree_spre/limi")
		# TODO
		Pyth.LineTo__File([str(limiLowe)], "flor/dist/limi")
	limi = limiLowe + limiSpre
	limiUppe = limi + 20.0
	return limiLowe, limi, limiUppe

def Coun(x, y, z, inte, minx, maxx, miny, maxy, minz, maxz, spheRadi, vertPer_Grid, weig, spheLoca, objeCoun, use_MagnScor = True, use_SpreScor = True, use_AverScor = True):
	import math
	incr = (maxx - minx) / float(inte)
	coun = []
	indeList = []
	for a in range(inte ** 3):
		coun.append(0)
		indeList.append([])
	scorSphe = 0.0
	scorAver = 0.0
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
				coun[inde] = vertPer_Grid
			else:
				coun[inde] += 1.0
				indeList[inde].append(a)
	scorAverTest = 0.0
	if use_AverScor:
		scorAverTestList = []
		for a in range(len(coun)):
			coux = int(math.fmod(a, inte))
			couy = int(math.fmod((a - coux) / inte, inte))
			couz = int(math.fmod((((a - coux) / inte) - couy) / inte, inte))
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
			if miniMagn > spheRadi: coun[a] = float(vertPer_Grid)
			scorAver += coun[a]
			scorIdea += vertPer_Grid
			scorAverTest += math.fabs(float(coun[a]) - vertPer_Grid)
			scorAverTestList.append([math.fabs(float(coun[a]) - vertPer_Grid), indeList[a]])
		# TODO: which is better. scorAver distributes bad scores. scorAverTest scores each cell individually
		scorAver = math.fabs(scorAver - scorIdea)
		scorAver = scorAverTest

		scorAverTestList = sorted(scorAverTestList, reverse = True)
		import random
		inde = []
		trie = 100
		try_ = 0
		while inde == []:
			random.seed()
			obje = random.random()
			obje = (4.0 ** obje - 1.0) / 3.0
			obje = round(obje * float(len(scorAverTestList) - 2))
			obje += 1
			inde = scorAverTestList[obje][1]
			# TODO: is this still needed
			#"""
			try_ += 1
			if try_ >= trie:
				random.seed()
				obje = random.random()
				obje = (4.0 ** obje - 1.0) / 3.0
				obje = round(obje * float(objeCoun - 2))
				obje += 1
				inde = [obje]
			#"""

	#scorAver = 0.0
	if use_SpreScor:
		spreScor, inde = SpreScor(coun, inte, indeList)
	else:
		spreScor = 0.0
	scor = scorAver + scorSphe + spreScor

	if use_SpreScor == False and use_AverScor == False:
		inde = []

	return scor, inde

# spread score
def SpreScor(coun, inte, indeList):
	import math
	#spreScor = 0.0
	#spreSco1 = 0.0
	#maxiValu = 0.0
	#maxiInde = -1
	spreScorList = []
	for a in range(len(coun)):
		spreScorList.append([0.0, indeList[a]])
		if coun[a] > 0:
			# get surrounding 26 sections, or those that exist
			coux = int(math.fmod(a, inte))
			couy = int(math.fmod((a - coux) / inte, inte))
			couz = int(math.fmod((((a - coux) / inte) - couy) / inte, inte))
			"""
			baseList = [3, 3, 3]
			if len(baseList) > 0: end_ = baseList[0]
			b = 1
			while b < len(baseList):
				end_ *= baseList[b]
				b += 1
			b = 0
			while b < end_:
				# TODO: slow
				counList = Math.Coun(baseList, b)
				if counList != [1, 1, 1]:
					if counList[2] == 0: x = coux - 1
					if counList[2] == 1: x = coux
					if counList[2] == 2: x = coux + 1
					if counList[1] == 0: y = couy - 1
					if counList[1] == 1: y = couy
					if counList[1] == 2: y = couy + 1
					if counList[0] == 0: z = couz - 1
					if counList[0] == 1: z = couz
					if counList[0] == 2: z = couz + 1
					if x >= 0 and x < inte and y >= 0 and y < inte and z >= 0 and z < inte:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
				b += 1
			"""
			x = coux - 1
			if x >= 0:
				inde = couz * (inte ** 2) + couy * inte + x
				# TODO: which is better
				#spreScor += scorAverTestList[inde][0]
				spreScorList[a][0] += coun[inde]
				y = couy - 1
				if y >= 0:
					inde = couz * (inte ** 2) + y * inte + x
					spreScorList[a][0] += coun[inde]
					z = couz - 1
					if z >= 0:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
					z = couz + 1
					if z < inte:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
				y = couy + 1
				if y < inte:
					inde = couz * (inte ** 2) + y * inte + x
					spreScorList[a][0] += coun[inde]
					z = couz - 1
					if z >= 0:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
					z = couz + 1
					if z < inte:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
				z = couz - 1
				if z >= 0:
					inde = z * (inte ** 2) + couy * inte + x
					spreScorList[a][0] += coun[inde]
				z = couz + 1
				if z < inte:
					inde = z * (inte ** 2) + couy * inte + x
					spreScorList[a][0] += coun[inde]
			x = coux + 1
			if x < inte:
				inde = couz * (inte ** 2) + couy * inte + x
				spreScorList[a][0] += coun[inde]
				y = couy - 1
				if y >= 0:
					inde = couz * (inte ** 2) + y * inte + x
					spreScorList[a][0] += coun[inde]
					z = couz - 1
					if z >= 0:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
					z = couz + 1
					if z < inte:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
				y = couy + 1
				if y < inte:
					inde = couz * (inte ** 2) + y * inte + x
					spreScorList[a][0] += coun[inde]
					z = couz - 1
					if z >= 0:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
					z = couz + 1
					if z < inte:
						inde = z * (inte ** 2) + y * inte + x
						spreScorList[a][0] += coun[inde]
				z = couz - 1
				if z >= 0:
					inde = z * (inte ** 2) + couy * inte + x
					spreScorList[a][0] += coun[inde]
				z = couz + 1
				if z < inte:
					inde = z * (inte ** 2) + couy * inte + x
					spreScorList[a][0] += coun[inde]
			y = couy - 1
			if y >= 0:
				inde = couz * (inte ** 2) + y * inte + coux
				spreScorList[a][0] += coun[inde]
				z = couz - 1
				if z >= 0:
					inde = z * (inte ** 2) + y * inte + coux
					spreScorList[a][0] += coun[inde]
				z = couz + 1
				if z < inte:
					inde = z * (inte ** 2) + y * inte + coux
					spreScorList[a][0] += coun[inde]
			y = couy + 1
			if y < inte:
				inde = couz * (inte ** 2) + y * inte + coux
				spreScorList[a][0] += coun[inde]
				z = couz - 1
				if z >= 0:
					inde = z * (inte ** 2) + y * inte + coux
					spreScorList[a][0] += coun[inde]
				z = couz + 1
				if z < inte:
					inde = z * (inte ** 2) + y * inte + coux
					spreScorList[a][0] += coun[inde]
			z = couz - 1
			if z >= 0:
				inde = z * (inte ** 2) + couy * inte + coux
				spreScorList[a][0] += coun[inde]
			z = couz + 1
			if z < inte:
				inde = z * (inte ** 2) + couy * inte + coux
				spreScorList[a][0] += coun[inde]
	spreScor = 0.0
	for a in range(len(spreScorList)):
		spreScor += spreScorList[a][0]

	spreScorList = sorted(spreScorList, reverse = True)
	import random
	inde = []
	trie = 100
	try_ = 0
	while inde == []:
		random.seed()
		obje = random.random()
		obje = (4.0 ** obje - 1.0) / 3.0
		obje = round(obje * float(len(spreScorList) - 2))
		obje += 1
		inde = spreScorList[obje][1]
	# TODO: arbitrary-ish
	spreWeig = 2.0 / float(inte)
	spreScor *= spreWeig
	return spreScor, inde

def ObjePick(objeCoun):
	import random
	random.seed()
	obje = random.random()
	# these interpolations increasingly favor smaller numbers
	#obje = 2.0 ** obje - 1.0
	#obje = (3.0 ** obje - 1.0) / 2.0
	obje = (4.0 ** obje - 1.0) / 3.0
	obje = round(obje * float(objeCoun - 2))
	obje += 1
	return obje

def Rota(chilList, pivo, rota, axis, objeName):
	import bpy
	import math
	a = 0
	while a < len(chilList):
		#Blen.Sele(objeName + "." + Blen.Pad_(chilList[a]))
		Blen.Sele(objeName + "." + Pyth.Pad_(chilList[a], 5))
		scal, rot_, loca = Blen.TranRead()
		for b in range(len(bpy.context.object.data.vertices)):
			vect = bpy.context.object.data.vertices[b].co
			vect = Math.Tran3d__(vect, scal, rot_, loca)
			vect = Math.Vect(pivo, vect)
			vect = Math.Quat(vect, rota, axis)
			vect = Math.VectAdd_(pivo, vect)
			vect = Math.Tran3d__Reve(vect, scal, rot_, loca)
			bpy.context.object.data.vertices[b].co = vect
		a += 1

def ChilList(obje, branPare):
	chilList = [obje]
	a = 0
	while a < len(branPare):
		if (a in chilList) == False and (branPare[a] in chilList):
			chilList.append(a)
			a = -1
		a += 1
	return chilList

def AxisRand():
	import random
	random.seed()
	axix = -1.0 + 2.0 * random.random()
	random.seed()
	axiy = -1.0 + 2.0 * random.random()
	random.seed()
	axiz = -1.0 + 2.0 * random.random()
	return Math.VectNorm((axix, axiy, axiz))

# this function expects a selected object, and the lowest trunk vertex selected in edit mode
def BranSepa(name = "obje"):
	import bpy
	retu = []
	obje = bpy.context.object.name
	coun = 0
	if obje != name:
		# get first vertex
		ver_List = Blen.VertListSele()
		vert = ver_List[0]
		# select more continually, invert and delete to clear floating branches
		while True:
			Blen.Edit()
			bpy.ops.mesh.select_more()
			Blen.Edit()
			vertListNext = Blen.VertListSele()
			if len(vertListNext) == len(ver_List):
				break
			ver_List = vertListNext[:]
		Blen.Edit()
		bpy.ops.mesh.select_all(action = 'INVERT')
		bpy.ops.mesh.delete(type = 'VERT')
		Blen.Edit()
		# founList checks if all vertices are accounted for
		founList = []
		for a in range(len(Blen.Vertices())):
			founList.append(False)
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
			#print(len(branPare))
			#print(branList[len(branList) - 1])
			#print(founList)
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
			for a in range(len(branList)):
				Blen.Sele(obje)
				bra_ = branList[a]
				if bra_[len(bra_) - 1] == -1:
					bra_.pop()
				vertList = Blen.VertLoca(bra_)
				Blen.Uplo([vertList, Math.EdgeLine(len(vertList) - 1), []])
				# TODO: what if Uplo() default name changes
				# TODO: abitrary padding
				#if bpy.context.object.name == "obje" or bpy.context.object.name == name:
				if coun == 0:
					#Blen.Name(name + ".000")
					Blen.Name(name + ".00000")
					BlenGame.Prop(propName = "atte", propType= 'INT')
					coun += 1
				else:
					#if coun > 1:
					Blen.Name(name + "." + Pyth.Pad_(coun, 5))
					coun += 1
		Blen.Sele(obje)
		Blen.Dele()
	else:
		print("object must have a different name than 'name' parameter \"" + name + "\"")
	return retu

def ScenVertList(exclList = []):
	import bpy
	import math
	x = []
	y = []
	z = []
	objeIndeList = []
	#for obje in bpy.context.scene.objects:
	for obje in bpy.data.objects:
		if (obje.name in exclList) == False and obje.hide_select == False:
			Blen.Sele(obje.name)
			scal = Blen.ScalRead()
			rota = Blen.RotaRead()
			#rota = (math.radians(rota[0]), math.radians(rota[1]), math.radians(rota[2]))
			loca = Blen.LocaRead()
			new_VertList = Blen.VertList()
			for a in range(1, len(new_VertList)):
				vert = new_VertList[a]
				vert = Math.Tran3d__(vert, scal, rota, loca)
				x.append(vert[0])
				y.append(vert[1])
				z.append(vert[2])
				objeIndeList.append(obje.name)
	return x, y, z, objeIndeList

main()

