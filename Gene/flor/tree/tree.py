import importlib.util
import os

path = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Modu" + os.sep + "Modu.py"
spec = importlib.util.spec_from_file_location("Modu", path)
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

# vector profile
# form a vector orthogonal to dire (vector) at angle angl
def VectProf(angl, dir_):
	import math
	import random
	angl = math.radians(angl)
	y = math.cos(angl)
	z = math.sin(angl)
	eule = Math.VectTo__Eule3d__(dir_)
	vect = Math.VectRota3d__((0.0, y, z), eule)
	return Math.VectNorm(vect)

# angle distribute
# get an angle that splits the difference between the largest gap in a list. if the list is blank, generate a random angle.
# prob: integer probability 1.0 / (prob + 1) that a random angle will be chosen instead of a split angle
def AnglDist(anglList = [], prob = 2):
	import random
	random.seed()
	rand = random.randint(0, prob)
	if len(anglList) == 0 or rand == 0:
		random.seed()
		angl = 360.0 * random.random()
	else:
		anglList = sorted(anglList)
		a = 0
		inde = -1
		diff = 0.0
		while a < len(anglList) - 1:
			dif_ = anglList[a + 1] - anglList[a]
			if dif_ > diff:
				diff = dif_
				inde = a
			a += 1
		# check the difference from the last angle to the first angle
		dif_ = (anglList[0] + 0.0) - (anglList[a] - 360.0)
		if dif_ > diff:
			angl = anglList[0] - (dif_ / 2.0)
			if angl < 0.0:
				angl += 360.0
		else:
			angl = anglList[inde] + (diff / 2.0)
	anglList.append(angl)
	return angl, anglList

def Tape(vertList = [], radi = 1.0, tape = 1.0, mate = ""):
	import bpy
	Blen.Curv()
	if mate != "":
		Blen.MateSet_(mate)
	name = bpy.context.object.name
	a = 0
	for vert in vertList:
		Blen.CurvLoca(a, vert)
		a += 1
	Blen.CurvHand()
	Blen.Circ()
	Blen.Scal((radi, radi, radi))
	bpy.data.objects[name].data.bevel_object = bpy.context.object
	Blen.Curv(clea = False)
	bpy.data.objects[name].data.taper_object = bpy.context.object
	Blen.CurvLoca(1, (0.0, 0.0, 0.0))
	Blen.CurvLoca(0, (-1.0, -tape, 0.0))
	Blen.CurvHand()
	bpy.context.object.data.splines[0].bezier_points[0].handle_right = (-1.0, -tape, 0.0)
	bpy.context.object.data.splines[0].bezier_points[1].handle_left = (0.0, 0.0, 0.0)
	bpy.context.object.data.splines[0].bezier_points[1].handle_right = (0.0, 0.0, 0.0)

def Bran(vertList = [], edgeList = [], branList = [], tape = 1.0, trun = True):
	import bpy
	import math
	import random
	if len(branList) > 0:

		loca = branList[0][0]
		vert = branList[0][1]
		dir_ = branList[0][2]
		axis = branList[0][3]
		ang_ = branList[0][4]
		leng = branList[0][5]
		magn = branList[0][6]
		magnOrig = branList[0][7]
		prob = branList[0][8]
		randAngl = branList[0][9]
		vertRandDivi = branList[0][10]
		branLengDivi = branList[0][11]
		probDecr = branList[0][12]
		spre = branList[0][13]
		midp = branList[0][14]
		anglInit = branList[0][15]
		magnDecr = branList[0][16]
		magnCut_ = branList[0][17]
		beveProp = branList[0][18]
		tapeProp = branList[0][19]
		line = branList[0][20]

		# store the points that make up this branch so that a tapered curve can be positioned in its place
		tapeList = []
		# track the angle of each new branch so that they can be evenly distributed
		anglList = []
		magnRoot = magn
		up__ = (0.0, 0.0, 1.0)
		down = (0.0, 0.0, -1.0)
		star = True
		# root connect. a new vertex is not added at the root of a new branch since the vertex already exists, but an edge needs to be connected.
		rootConn = False
		dist = 0.0
		while dist < leng:
			random.seed()
			rand = random.random() * 360.0
			direNorm = VectProf(rand, dir_)
			dir_ = Math.Quat(dir_, randAngl, direNorm)
			# start
			#star = False
			# loca is equal to the root on the first iteration of a new branch
			#if loca == branList[0][0]:
			#	star = True
			if star and len(vertList) != 0:
				tapeList.append(loca)
			if not star or len(vertList) == 0:
				if len(vertList) != 0:
					#loca = Math.VectAdd_(loca, Math.VertRand(magn * vertRandDivi))
					loca = Math.VectAdd_(loca, Math.VectScal(dir_, magn))
					loca = Math.VectAdd_(loca, Math.VertRand(magn * vertRandDivi))
				tapeList.append(loca)
				vertList.append(loca)
			if len(vertList) > 1:
				if not star:
					if rootConn == False:
						edgeList.append((len(vertList) - 2, len(vertList) - 1))
					else:
						edgeList.append((vert, len(vertList) - 1))
						rootConn = False
				else:
					rootConn = True
			if not star:
				random.seed()
				rand = random.random()
				if rand > (magn / magnOrig) * prob:
					# progress. current proportion of distance along branch to total distance
					prog = dist / leng
					# get a length for the next branch
					if line == True:
						# remaining proportion of branch distance
						rema = ((leng - dist) / leng)
						branLeng = leng * rema * branLengDivi
					else:
						branLeng = ((1.0 / 2.0) ** 2.0 - (prog - 1.0 / 2.0) ** 2.0) ** 0.5
						branLeng *= leng
					# pick an angle	
					angl, anglList = AnglDist(anglList)
					branDire = VectProf(angl, dir_)
					branAxis = Math.VectCros3d__(branDire, up__)
					branDire = Math.Quat(branDire, anglInit, branAxis)
					ang_ = spre * prog - spre * midp
					branList.append([loca, len(vertList) - 1, branDire, branAxis, ang_, branLeng, magn, magnOrig, prob, randAngl, vertRandDivi, branLengDivi, probDecr, spre, midp, anglInit, magnDecr, magnCut_, beveProp, tapeProp, line])
			#loca = Math.VectAdd_(loca, Math.VectScal(dir_, magn))
			dist += magn
			magn *= magnDecr
			if axis != (0.0, 0.0, 0.0):
				direNew_ = Math.Quat(dir_, ang_, axis)
				# TODO: not working
				# prevent branch from passing the up or down vector
				upda = True
				vec1 = Math.Vect(up__, dir_)
				vec2 = Math.Vect(up__, direNew_)
				# if the vector from up to the old vector and the vector from up to the new vector changed direction, the new vector passed the up vector, so update. another way to put it is dont allow branches to curl. once they point straight up or down they stay up or down.
				if Math.VectDot_(vec1, vec2) < 0.0:
					upda = False
				vec1 = Math.Vect(down, dir_)
				vec2 = Math.Vect(down, direNew_)
				if Math.VectDot_(vec1, vec2) < 0.0:
					upda = False
				if upda == True:
					dir_ = direNew_
			# break if the distance between branch nodes gets too small
			if magn < magnCut_:
				print("break")
				break
			star = False
		# this branch has been processed, so remove it
		branList.pop(0)
		# add a taper bevel to the mesh line
		if len(tapeList) > 0:
			Tape(vertList = tapeList, radi = magnRoot * beveProp, tape = magnRoot * tapeProp, mate = "bark")
			Blen.Sele("BezierCurve")
			Blen.Conv()
			if bpy.context.object.type == 'MESH':
				# dissolve excess geometry
				Blen.Diss()
				if trun == True:
					Blen.Name("tree")
					trun = False
				else:
					Blen.Sele("tree")
					Blen.Join("BezierCurve")
		if len(branList) > 5000:
			print()
			print("exiting")
			print()
			branList = []
	return vertList, edgeList, branList, trun

def main():

	import bpy
	import math
	import random

	exte = False
	try:
		paraDict = para
		exte = True
		direOut = dire + "out_" + os.sep + "tree_" + numb + "_para"
	except:
		paraDict = Gene.ParaInit("tree_para")
		direOut = ""
	Gene.ParaWrit(para = paraDict, dire = direOut, exte = exte)

	# variables that change throughout
	star = (0.0, 0.0, 0.0)
	dir_ = (0.0, 0.0, 1.0)
	axis = (0.0, 0.0, 0.0)
	angl = 0.0
	magn = paraDict["heig"] / 10.0

	# variables that remain constant
	# (any of these variables could also be changed)

	# change the angle of each section of branch by randAngl degrees
	# randAngl
	# randomize the position of each vertex of the tree
	# this gets muliplied by magn, the distance between each vertex
	# (magn decreases as a branch moves towards the end)
	# vertRandDivi
	# length of a new branch in proportion to the old branch
	# branLengDivi
	# factor to decrease the probability of not branching at each node for a new branch
	# probDecr
	# angle spread from the start of a branch (or trunk) to the end for each new branch
	# branching from the trunk starts to bend towards the ground and ends bending up
	# spre
	# midpoint. this is where bending changes from bending towards the ground to bending upwards
	# midp
	# the end-facing angle of a new branch
	# anglInit
	# magn decrease. decrease the magnitude of the previous vertex to the new vertex by this amount
	# new branches inherit magn at their root
	# magnDecr
	# magnitude cutoff. end the branch if the magnitude reaches this amount
	magnCut_ = 0.001
	# set the bevel radius to this proportion of the branches original magnitude
	beveProp = 1.0 / 2.0
	# set the taper amount to this proportion of the branches original magnitude
	tapeProp = 1.0 / 2.0

	line = paraDict["line"]
	if line < 0.5:
		line = True
	else:
		line = False

	vertList = []
	edgeList = []
	branList = [[star, 0, dir_, axis, angl, paraDict["heig"], magn, magn, paraDict["prob"], paraDict["randAngl"], paraDict["vertRandDivi"], paraDict["branLengDivi"], paraDict["probDecr"], paraDict["spre"], paraDict["midp"], paraDict["anglInit"], paraDict["magnDecr"], magnCut_, beveProp, tapeProp, line]]
	trun = True
	while len(branList) > 0:
		vertList, edgeList, branList, trun = Bran(vertList = vertList, edgeList = edgeList, branList = branList, trun = trun)
	Blen.Uplo([vertList, edgeList, []])

	Blen.Sele("BezierCircle")
	bpy.context.object.scale = (1.0, 1.0, 1.0)
	Blen.Sele("BezierCurve.001")
	bpy.context.object.data.splines[0].bezier_points[0].handle_right = (-1.0, -magn * tapeProp / 2.0, 0.0)

main()

