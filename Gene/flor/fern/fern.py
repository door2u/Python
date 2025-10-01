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

	# TODO

	import bpy
	import math
	import random

	exte = False
	try:
		paraDict = para
		exte = True
		direOut = dire + "out_" + os.sep + "fern_" + numb + "_para"
	except:
		# TODO: where else did this get messed up?
		# TODO: call this file to list?
		paraDict = Pyth.FileTo__Line("flor/fern/fern_para")
		paraDict = Pyth.LineTo__Dict(paraDict)
		paraDict = Gene.ParaInit(paraDict)
		direOut = ""

	# TODO
	paraDict = {}

	Gene.ParaWrit(para = paraDict, dire = direOut, exte = exte)

	offs = 0.004
	smoo = 1

	### create base shape
	Blen.Sele("Plane")
	random.seed()
	cuts = random.randint(0, 20)
	Blen.Edit()
	bpy.ops.mesh.subdivide(number_cuts = cuts)
	Blen.Edit()
	coun = len(Blen.Vertices())
	random.seed()
	ite_ = random.randint(0, 20)
	a = 0
	while a < ite_:
		random.seed()
		rand = random.randint(1, coun)
		# TODO: this could be a Gene function
		sele = []
		for b in range(coun):
			sele.append(False)
		seleList = []
		b = 0
		while b < rand:
			random.seed()
			ran_ = random.randint(0, coun - 1)
			if sele[ran_] == False:
				seleList.append(ran_)
				sele[ran_] = True
				b += 1
		Blen.VertSele(seleList)
		Blen.Edit()
		bpy.ops.transform.vertex_random(offset = offs)
		for b in range(smoo):
			bpy.ops.mesh.vertices_smooth(factor = 1)
		Blen.Edit()
		Blen.VertDese()
		a += 1
	scax = Math.RandRang(0.5, 1.5)
	scay = Math.RandRang(0.5, 1.5)
	Blen.Scal((scax, scay, 0.0))
	Blen.Appl()
	z = bpy.context.object.data.vertices[0].co.z
	Blen.Loca((0.0, 0.0, -z))
	Blen.Appl()
	Blen.OrigGeom()
	cent = bpy.context.object.location

	### distribute curves on base

	name = "Plane"
	random.seed()
	gridSpac = Math.RandRang(0.25, 0.5)
	#gridSpac = 1.5
	# distance to max scale
	#scalDist = 2.0

	####################

	Blen.Sele(name)
	# TODO: vertex select mode
	outl = VertOutl()
	# make an outline object
	Blen.Dupl()
	Blen.Name(name + ".outline")
	Blen.VertSele(outl)
	Blen.Edit()
	bpy.ops.mesh.select_all(action = 'INVERT')
	Blen.Edit()
	Blen.VertDele()
	# get object bounding box
	minx = Blen.Xyz_Most(axis = 0, reverse = False)
	maxx = Blen.Xyz_Most(axis = 0, reverse = True)
	miny = Blen.Xyz_Most(axis = 1, reverse = False)
	maxy = Blen.Xyz_Most(axis = 1, reverse = True)
	minz = Blen.Xyz_Most(axis = 2, reverse = False)
	maxz = Blen.Xyz_Most(axis = 2, reverse = True)
	minx += bpy.context.object.location[0]
	maxx += bpy.context.object.location[0]
	miny += bpy.context.object.location[1]
	maxy += bpy.context.object.location[1]
	minz += bpy.context.object.location[2]
	maxz += bpy.context.object.location[2]
	minx -= gridSpac
	maxx += gridSpac
	miny -= gridSpac
	maxy += gridSpac
	# get a list of sections by vertex
	sectList = []
	for a in range(len(bpy.context.object.data.vertices)):
		sectList.append(Sect(bpy.context.object.data.vertices[a].co.x + bpy.context.object.location[0], bpy.context.object.data.vertices[a].co.y + bpy.context.object.location[1], gridSpac, minx, miny))
	# list of edges that each vertex belongs to
	vertEdgeInde = []
	for vert in bpy.context.object.data.vertices:
		vertEdgeInde.append([])
	for a in range(len(bpy.context.object.data.edges)):
		edge = bpy.context.object.data.edges[a].key
		vertEdgeInde[edge[0]].append(a)
		vertEdgeInde[edge[1]].append(a)

	emptCoun = 0
	curx = minx
	while curx < maxx:
		in__ = False
		prex = None
		prey = None
		cury = miny
		while cury < maxy:
			x = curx
			x += Math.RandRang(-gridSpac / 2.0, gridSpac / 2.0)
			y = cury
			y += Math.RandRang(-gridSpac / 2.0, gridSpac / 2.0)
			if prex != None:
				sect = Sect(x, y, gridSpac, minx, miny)
				sectPrev = Sect(prex, prey, gridSpac, minx, miny)
				edgeList = []
				for a in range(len(sectList)):
					if sectList[a] == sect or sectList[a] == sectPrev:
						# get each edge of the vertex
						for edge in vertEdgeInde[a]:
							exis = False
							for d in range(len(edgeList)):
								if edgeList[d] == edge:
									exis = True
									break
							if exis == False:
								edgeList.append(edge)
								edg_ = bpy.context.object.data.edges[edge].key
								ver1 = edg_[0]
								ver2 = edg_[1]
								x1 = bpy.context.object.location[0] + bpy.context.object.data.vertices[ver1].co.x
								y1 = bpy.context.object.location[1] + bpy.context.object.data.vertices[ver1].co.y
								x2 = bpy.context.object.location[0] + bpy.context.object.data.vertices[ver2].co.x
								y2 = bpy.context.object.location[1] + bpy.context.object.data.vertices[ver2].co.y
								if Inte2d__((x1, y1), (x2, y2), (prex, prey), (x, y)):
									in__ = not in__
			if in__:

				Blen.Sele("BezierCurve")
				Blen.Dupl()
				Blen.Name("stem." + Blen.Pad_(emptCoun))
				Blen.Loca((x, y, 0.0))

				### adjust curves

				

				### set curve
				# TODO: make a function
				# base
				z2 = Math.RandRang(0.5, 1.0)
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[0].select_right_handle = True
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[0].handle_right = (0.0, 0.0, z2)
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[0].select_right_handle = False
				Blen.Edit()
				# center point
				x2 = Math.RandRang(0.25, 0.75)
				z2 = Math.RandRang(0.0, 1.0)
				bpy.context.object.data.splines[0].bezier_points[1].co = (x2, 0.0, z2)

				x2 = Math.RandRang(0.75, 1.0)
				z2 = Math.RandRang(0.0, 0.5)
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[1].select_right_handle = True
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[1].handle_right = (x2, 0.0, z2)
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[1].select_right_handle = False
				Blen.Edit()

				x2 = Math.RandRang(0.0, 0.25)
				z2 = Math.RandRang(0.5, 1.0)
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[1].select_left_handle = True
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[1].handle_left = (x2, 0.0, z2)
				Blen.Edit()
				bpy.context.object.data.splines[0].bezier_points[1].select_left_handle = False
				Blen.Edit()

				#Blen.Conv()

				### add leaves
				Blen.Dupl()
				Blen.Name("leaf_posi." + Blen.Pad_(emptCoun))
				bpy.context.object.data.bevel_object = None
				bpy.context.object.data.taper_object = None
				
				vertList = []
				
				inte = 100
				b = 0
				sum_ = inte * (inte + 1) / 2
				
				bpy.context.object.data.resolution_u = 10
				Blen.Conv()
				#Blen.VertSeleAll_()
				#leng = len(Blen.Vertices())
				#Blen.Edit()
				#while leng < int(sum_):
				#	bpy.ops.mesh.subdivide()
				#	#leng = len(Blen.Vertices())
				#	leng *= 2
				#	print(leng, sum_)
				#Blen.Edit()
				#for a in range(len(Blen.Vertices())):
				while True:
					#if a == b:
					#a = int(b / 10)
					a = int(float(b) / float(sum_) * 10.0)
					#print(a)
					angl = 0.0
					#loca = bpy.context.object.data.vertices[a].co
					prog = bpy.context.object.data.vertices[a].co
					if a != 0:
						#angl = bpy.context.object.data.vertices[a - 1].co
						#angl = Math.Vect(angl, prog)
						#angl = Math.VectAngl(angl, (0.0, 0.0, 1.0))

						#try:
						prog = Math.Vect(prog, bpy.context.object.data.vertices[a + 1].co)


						angl = Math.VectAngl(prog, (0.0, 0.0, 1.0))

						#prog = Math.VectScal(prog, float(inte) / float(sum_))
						prog = Math.VectScal(prog, float(b) / float(sum_) * 10.0 - a)
						prog = Math.VectAdd_(bpy.context.object.data.vertices[a].co, prog)
						#except:
						#	pass

						#vertList.append([loca, angl])
						vertList.append([prog, angl])
					b += inte
					if inte > 1:
						inte -= 1
					else:
						break

				Blen.Sele("stem." + Blen.Pad_(emptCoun))
				Blen.Conv()

				for a in range(len(vertList)):
					#print(a)
					Blen.Sele("Plane.001")
					Blen.Dupl()
					Blen.Loca((x + vertList[a][0][0], y + vertList[a][0][1], vertList[a][0][2]))
					Blen.RotaSet_((0.0, vertList[a][1], 0.0))
					# TODO: increase leaf density towards end
					scal = 1.0 - a / len(vertList)
					Blen.Scal((scal, scal, scal))
					Blen.Dupl()
					Blen.RotaSet_((0.0, 180.0 - vertList[a][1], 180.0))
					Blen.Join("Plane.002")
					Blen.Join("stem." + Blen.Pad_(emptCoun))
					Blen.Name("stem." + Blen.Pad_(emptCoun))
				Blen.Curs((x, y, 0.0))
				Blen.OrigCurs()
				
				# TODO: make this more consistent
				# set z rotation
				random.random()
				#z = 360.0 * random.random()
				#z = 0.0
				z = Math.Vect((x, y, 0.0), cent)
				z = math.atan2(z[1], z[0])
				#bpy.context.object.rotation_euler[2] = z * math.pi / 180.0
				bpy.context.object.rotation_euler[2] = z

				# scal
				scal = Math.RandRang(0.5, 1.5)
				Blen.Scal((scal, scal, scal))
				#Blen.Appl()

				

				emptCoun += 1
				Blen.Sele(name + ".outline")
			prex = x
			prey = y
			cury += gridSpac
		curx += gridSpac

	Blen.Sele(name + ".outline")
	Blen.Dele()

	

# return a vertex list that outlines a mesh
def VertOutl():
	import bpy
	# list of edges that each vertex belongs to
	vertEdgeInde = []
	for vert in bpy.context.object.data.vertices:
		vertEdgeInde.append([])
	for a in range(len(bpy.context.object.data.edges)):
		edge = bpy.context.object.data.edges[a].key
		vertEdgeInde[edge[0]].append(a)
		vertEdgeInde[edge[1]].append(a)
	# count occurences of edges in polygons
	edgeCoun = []
	for edge in bpy.context.object.data.edges:
		edgeCoun.append(0)
	for poly in bpy.context.object.data.polygons:
		keys = poly.edge_keys
		for key_ in keys:
			for a in range(len(vertEdgeInde[key_[0]])):
				for b in range(len(vertEdgeInde[key_[1]])):
					if vertEdgeInde[key_[0]][a] == vertEdgeInde[key_[1]][b]:
						edgeCoun[vertEdgeInde[key_[0]][a]] += 1
	outl = []
	for a in range(len(edgeCoun)):
		if edgeCoun[a] == 1:
			outl.append(a)
	vertList = []
	for a in range(len(outl)):
		vertList.append(bpy.context.object.data.edges[outl[a]].key[0])
		vertList.append(bpy.context.object.data.edges[outl[a]].key[1])
	# purge duplicates
	vertList = sorted(vertList)
	a = len(vertList) - 1
	while a >= 1:
		if vertList[a - 1] == vertList[a]:
			vertList.pop(a)
		a -= 1
	return vertList

def Sect(x, y, gridSpac, minx, miny):
	retu = ()
	a = 0
	while a * gridSpac + minx - gridSpac / 2.0 < x:
		a += 1
	a -= 1
	b = 0
	while b * gridSpac + miny - gridSpac / 2.0 < y:
		b += 1
	b -= 1
	retu = (a, b)
	return retu

# TODO:
# reduce this
# use 2d cross
def Inte2d__(sta1, end1, sta2, end2):
	import math
	retu = False
	v1 = Math.Vect(sta1, end1)
	norm = Math.VectNorm(v1)
	v2 = Math.Vect(sta2, end2)
	angl = math.atan2(v2[1], v2[0])
	angl -= math.pi / 2.0
	x = math.cos(angl)
	y = math.sin(angl)
	dist = Math.DistTo__Inte((sta1[0], sta1[1], 0.0), (norm[0], norm[1], 0.0), (sta2[0], sta2[1], 0.0), (x, y, 0.0))
	if type(dist) == float and dist > 0.0:
		norm = Math.VectScal(norm, dist)
		norm = Math.VectAdd_(norm, sta1)
		retu = True
		mag1 = Math.VectMagn(v1)
		mag2 = Math.VectMagn(v2)
		v1n = Math.Vect(sta1, norm)
		if Math.VectMagn(v1n) > mag1:
			retu = False
		if Math.VectDot_(Math.VectNorm(v1), Math.VectNorm(v1n)) < 0.999:
			retu = False
		v2n = Math.Vect(sta2, norm)
		if Math.VectMagn(v2n) > mag2:
			retu = False
		if Math.VectDot_(Math.VectNorm(v2), Math.VectNorm(v2n)) < 0.999:
			retu = False
	return retu

main()

