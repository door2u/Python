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

"""
# TODO
def Cho2(leng):
	retu = []
	# make limit list
	a = leng
	limi = []
	while a > 0:
		limi.append(a)
		a -= 1
	# make progress list
	prog = []
	for a in range(leng):
		prog.append(0)
	inde = 0
	cont = True
	while cont:
		sele = []
		for a in range(leng):
			sele.append(False)
		seam = []
		for a in range(leng):
			pro_ = 0
			for b in range(leng):
				if sele[b]:
					pro_ += 1
				else:
					break
			b = 0
			while b < prog[a]:
				pro_ += 1
				if sele[pro_] == False:
					b += 1
			if pro_ < leng:
				sele[pro_] = True

			seam.append([a, pro_])
		if cont:
			seamPrin = []
			for a in range(len(seam)):
				seamPrin.append(seam[a][1])
			retu.append(seamPrin)
			prog[inde] += 1
			while inde < leng and prog[inde] == limi[inde]:
				prog[inde] = 0
				inde += 1
				if inde < leng:
					prog[inde] += 1
			if inde == leng:
				cont = False
			inde = 0
	return retu
"""


breaTime = 10.0


def EdgeCoun():
	import bpy
	import time
	edgeCoun = []
	for a in range(len(bpy.context.object.data.vertices)):
		edgeCoun.append([])
	for a in range(len(bpy.context.object.data.edges)):
		edgeCoun[bpy.context.object.data.edges[a].key[0]].append(bpy.context.object.data.edges[a].key[1])
		edgeCoun[bpy.context.object.data.edges[a].key[1]].append(bpy.context.object.data.edges[a].key[0])
	return edgeCoun

def LoopGet_Loca(axis = 2, reverse = False, leng = 32):
	import bpy
	import time
	# get lowest z
	#print("her1")
	vert = Blen.Xyz_Most(axis = axis, reverse = reverse, inde = True)
	#print("her2")
	#Blen.VertSele([vert[3]])
	#vertList = Blen.VertList()
	edgeList = Blen.EdgeList()
	
	conn = Math.VertCon2(vert[3], edgeList, [])
	#print(vert[3], conn)
	for a in range(len(conn)):
		Blen.VertDese()
		Blen.VertSele([vert[3], conn[a]])
		Blen.Edit()
		bpy.ops.mesh.loop_multi_select()
		Blen.Edit()
		vertList = Blen.VertListSele()
		if len(vertList) == leng:
			break

		#print("1", time.clock())
		if time.clock() > breaTime:
			return 0

	Blen.VertDese()
	return vertList

def LoopOuts(loopCoun = 3, outs = True):
	import bpy
	import time
	loopList = []
	#print(len(loopList))
	a = 0
	while len(loopList) < loopCoun:
		edge = bpy.context.object.data.loops[a].edge_index
		edge = bpy.context.object.data.edges[edge]
		Blen.VertSele([edge.key[0], edge.key[1]])
		Blen.Edit()
		bpy.ops.mesh.loop_multi_select()
		Blen.Edit()
		vertList = Blen.VertListSele()

		#print("2", time.clock())
		if time.clock() > breaTime:
			return 0

		if len(vertList) == 46:
			exis = False
			for b in range(len(loopList)):
				if (vertList[0] in loopList[b]):
					exis = True
					break
			if exis == False:
				loopList.append(vertList)
		Blen.VertDese()
		a += 1
	vertList = Blen.VertList()
	radi = -1.0
	inde = -1
	for a in range(len(loopList)):
		dist = 0.0
		vert = []
		for b in range(len(loopList[a])):
			vert.append(vertList[loopList[a][b]])
		# get the radius to each vertex
		aver = Math.VectAver(vert)
		for b in range(len(vert)):
			dist += Math.VectMagn(Math.Vect(aver, vert[b]))

			#print("3", time.clock())
			if time.clock() > breaTime:
				return 0

		if outs:
			if dist > radi:
				radi = dist
				inde = a
		else:
			if inde == -1 or dist < radi:
				radi = dist
				inde = a

		#print("4", time.clock())
		if time.clock() > breaTime:
			return 0

	return loopList[inde]

def LoopGet_Inde(vert, coun, edgeList):
	import bpy
	import time
	retu = []
	conn = Math.VertCon2(vert, edgeList, [])
	for a in range(len(conn)):
		Blen.VertSele([vert, conn[a]])
		# TODO: add to Blen
		Blen.Edit()
		bpy.ops.mesh.loop_multi_select()
		Blen.Edit()
		retu = Blen.VertListSele()
		if len(retu) == coun:
			break

		#print("5", time.clock())
		if time.clock() > breaTime:
			return 0

	#vert = LoopGet_Inde()
	Blen.VertDese()
	return retu

def LoopGet_(leng = 32):
	import bpy
	import time
	a = 0
	while a < len(bpy.context.object.data.loops):
		edge = bpy.context.object.data.loops[a].edge_index
		edge = bpy.context.object.data.edges[edge]
		Blen.VertSele([edge.key[0], edge.key[1]])
		Blen.Edit()
		bpy.ops.mesh.loop_multi_select()
		Blen.Edit()
		vertList = Blen.VertListSele()
		if len(vertList) == leng:
			break
		a += 1

		#print("6", time.clock())
		if time.clock() > breaTime:
			return 0

	Blen.VertDese()
	return vertList

def LoopComm(loo1, loo2):
	import time
	retu = -1
	brea = False
	for a in range(len(loo1)):
		for b in range(len(loo2)):
			if loo1[a] == loo2[b]:
				retu = loo1[a]
				brea = True
				break
		if brea:
			break
	return retu

def Loo3Fini(loo1, loo2, loo3, edgeList):
	import bpy
	import time
	conn = Math.VertCon2(loo3[len(loo3) - 1], edgeList, [])
	for a in range(len(conn)):
		if (conn[a] in loo3) == False:
			loo3.append(conn[a])

		#print("7", time.clock())
		if time.clock() > breaTime:
			return 0

	Blen.VertSele(loo3)
	Blen.Edit()
	bpy.ops.mesh.loop_multi_select()
	Blen.Edit()
	loop = Blen.VertListSele()
	Blen.VertDese()
	for a in range(len(loop)):
		if (loop[a] in loo1) == False and (loop[a] in loo2) == False and (loop[a] in loo3) == False:
			loo3.append(loop[a])

		#print("8", time.clock())
		if time.clock() > breaTime:
			return 0

	return loo3

def LoopStar(vertList, meth = -2):
	import bpy
	import math
	import time
	edgeCoun = EdgeCoun()
	retu = []
	for a in range(len(vertList)):
		if len(edgeCoun[vertList[a]]) == 2:
			retu.append(vertList[a])

		#print("9", time.clock())
		if time.clock() > breaTime:
			return 0

	if meth == 0:
		retu = retu[0]
	if int(math.fabs(meth)) == 1:
		axis = 0
	if int(math.fabs(meth)) == 2:
		axis = 1
	if int(math.fabs(meth)) == 3:
		axis = 2
	loc1 = tuple(bpy.context.object.data.vertices[retu[0]].co)
	loc2 = tuple(bpy.context.object.data.vertices[retu[1]].co)
	if meth < 0:
		if loc1[axis] < loc2[axis]:
			retu = retu[0]
		else:
			retu = retu[1]
	else:
		if loc1[axis] > loc2[axis]:
			retu = retu[0]
		else:
			retu = retu[1]
	return retu

def LoopSort(star, coun, loop, edgeList, exclList = []):
	import time
	retu = [star]
	conn = Math.VertCon2(star, edgeList, [])
	while len(retu) < coun:
		for a in range(len(conn)):
			if (conn[a] in loop) and (conn[a] in retu) == False and (conn[a] in exclList) == False:
				retu.append(conn[a])
				conn = Math.VertCon2(conn[a], edgeList, [])
				break

			#print("10", time.clock())
			if time.clock() > breaTime:
				return 0

		#print("10_2", time.clock())
		if time.clock() > breaTime:
			print("broke")
			return 0

	return retu

def LoopEyes(looa, edgeList, widt, leng = 46, spli = -3, meth = 1):
	import bpy
	import math
	import time
	if int(math.fabs(spli)) == 1:
		axis = 0
	if int(math.fabs(spli)) == 2:
		axis = 1
	if int(math.fabs(spli)) == 3:
		axis = 2
	poin = -1.0
	inde = -1
	for a in range(len(looa)):
		loca = tuple(bpy.context.object.data.vertices[looa[a]].co)
		if spli < 0:
			if inde == -1 or loca[axis] < poin:
				poin = loca[axis]
				inde = a
		else:
			if inde == -1 or loca[axis] > poin:
				poin = loca[axis]
				inde = a

		#print("11", time.clock())
		if time.clock() > breaTime:
			return 0

	looa = LoopSort(looa[inde], leng, looa, edgeList)
	best = -1.0
	inde = -1
	if meth == 0:
		axis = 1
	else:
		axis = 2
	a = 0
	while a + widt < leng:
		loo_ = looa[a : a + widt]
		mini = None
		maxi = None
		for b in range(len(loo_)):
			loo_[b] = tuple(bpy.context.object.data.vertices[loo_[b]].co)
			if mini == None or loo_[b][axis] < mini:
				mini = loo_[b][axis]
			if maxi == None or loo_[b][axis] > maxi:
				maxi = loo_[b][axis]
		size = maxi - mini
		loca = Math.VectAver(loo_)
		if size > 0.0001:
			scor = loca[2] / size
		# TODO: else?
		if inde == -1 or scor > best:
			best = scor
			inde = a
		a += 1

		#print("12", time.clock())
		if time.clock() > breaTime:
			return 0

	looa = looa[inde : inde + widt]
	return looa

def StarSegm(loop, edgeList, meth = -2):
	import bpy
	import math
	import time
	if meth == 0:
		retu = retu[0]
	if int(math.fabs(meth)) == 1:
		axis = 0
	if int(math.fabs(meth)) == 2:
		axis = 1
	if int(math.fabs(meth)) == 3:
		axis = 2
	star = []
	for a in range(len(loop)):
		conn = Math.VertCon2(loop[a], edgeList, [])
		connCoun = 0
		for b in range(len(conn)):
			if conn[b] in loop:
				#star.append(a)
				connCoun += 1
		if connCoun == 1:
			star.append(a)

		#print("13", time.clock())
		if time.clock() > breaTime:
			return 0

	#print(star)
	loca = []
	loca.append(tuple(bpy.context.object.data.vertices[loop[star[0]]].co))
	loca.append(tuple(bpy.context.object.data.vertices[loop[star[1]]].co))
	# TODO: meth
	if meth < 0:
		if loca[0][axis] < loca[1][axis]:
			star = loop[star[0]]
		else:
			star = loop[star[1]]
	else:
		if loca[0][axis] > loca[1][axis]:
			star = loop[star[0]]
		else:
			star = loop[star[1]]
	return star

#def Stic(sticList):
def Stic(obj1, loo1, obj2, loo2, leng):
	import bpy
	import time
	# TODO: make sure list lengths are the same
	#for a in range(len(sticList[0][1])):
	star = 0
	end_ = len(loo1)
	#if leng > 0:
	if leng == 1 or leng == 2:
		#star += 1
		end_ -= 1
	#if leng == 2:
	if leng > 1:
		#end_ -= 1
		star += 1
	for a in range(star, end_):
		loca = []
		#for b in range(len(sticList)):
		#for b in range(2):
		#Blen.Sele(sticList[b][0])
		Blen.Sele(obj1)
		#loca.append(tuple(bpy.context.object.data.vertices[sticList[b][1][a]].co))
		loca.append(tuple(bpy.context.object.data.vertices[loo1[a]].co))
		Blen.Sele(obj2)
		loca.append(tuple(bpy.context.object.data.vertices[loo2[a]].co))
		loca = Math.VectAver(loca)
		#for b in range(len(sticList)):
		Blen.Sele(obj1)
		bpy.context.object.data.vertices[loo1[a]].co = loca
		Blen.Sele(obj2)
		bpy.context.object.data.vertices[loo2[a]].co = loca

		#print("14", time.clock())
		if time.clock() > breaTime:
			return 0


def main():

	# TODO:

	# dont use a vertList for seams. try making vertex groups
	# find out whats causing seams
	# eyes material
	# check if new faces work

	# move data to gene
	# manage para files instead of overwriting them
	# make a howto or readme. what do all the scripts do

	# fix Gene.Make()

	import bpy
	import random
	import time

	# TODO
	loca = (0.0, 0.0, 0.27293)

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

	# pick features from libr
	os.system("python3 /home/christopher/Documents/prog/Pyth/Gene/face/face_expo.py")

	# read seam data
	seam = []
	for a in range(len(overlap_)):
		line = Pyth.FileTo__Line("face/seam/seam")
		for b in range(len(line)):
			line[b] = line[b].split(" ")
			seam.append([float(line[b][0]), float(line[b][1]), float(line[b][2]), int(line[b][3]), line[b][4]])

	grouList = []
	# import geometry
	for a in range(len(overlap_)):
		# read mesh data from file
		line = Pyth.FileTo__Line("face/expo/" + str(a) + "_vert")
		vertList = []
		for b in range(len(line)):
			vert = line[b]
			vert = vert.split("(")
			vert = vert[1]
			vert = vert.split(")")
			vert = vert[0]
			vert = vert.split(",")
			vertList.append((float(vert[0]), float(vert[1]), float(vert[2])))
		line = Pyth.FileTo__Line("face/expo/" + str(a) + "_edge")
		line = line[0]
		line = line.split("[")
		line = line[1]
		line = line.split("]")
		line = line[0]
		edgeList = ""
		b = 0
		while b < len(line):
			if line[b] != "(" and line[b] != ")":
				edgeList += line[b]
			b += 1
		line = edgeList
		line = line.split(",")
		edgeList = []
		b = 0
		while b < len(line):
			edgeList.append((int(line[b]), int(line[b + 1])))
			b += 2
		line = Pyth.FileTo__Line("face/expo/" + str(a) + "_poly")
		line = line[0]
		polyList = []
		b = 1
		while b < len(line):
			while b < len(line) and line[b] != "[":
				b += 1
			b += 1
			poly = []
			while b < len(line) and line[b] != "]":
				numb = ""
				while b < len(line) and line[b].isnumeric():
					numb += line[b]
					b += 1
				if numb != "":
					poly.append(int(numb))
				if b < len(line) and line[b] == "]":
					break
				b += 1
			polyList.append(poly)
		polyList.pop(len(polyList) - 1)
		# copy into new blend
		Blen.Uplo([vertList, edgeList, polyList])
		Blen.Name(overlap_[a][0])
		# TODO:
		# mirror
		bpy.ops.object.modifier_add(type='MIRROR')
		bpy.context.object.modifiers["Mirror"].use_x = False
		bpy.context.object.modifiers["Mirror"].use_y = True
		# TODO
		# move up
		Blen.Loca(loca)
		# shade smooth
		Blen.VertSeleAll_()
		Blen.Edit()
		bpy.ops.mesh.faces_shade_smooth()
		Blen.Edit()
		Blen.VertDese()
		# create group
		#Blen.VertSeleAll_()
		#vertList = Blen.VertListSele()
		#for b in range(len(vertList)):
		#	vertList[b] = tuple(bpy.context.object.data.vertices[vertList[b]].co)
		#Blen.VertDese()
		#grouList.append(vertList)
		# apply material
		if a != 4 and a != 9:
			Blen.MateSet_("skin")
		else:
			if a == 4:
				Blen.MateSet_("liner")
				Blen.MateSet_("lip_lower")
				Blen.MateSet_("lip_upper")
				Blen.MateSet_("skin")
				# lip liner
				vertList = [0, 2, 3, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 48, 49, 50, 51, 53, 54, 55, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67]
				Blen.VertDese()
				Blen.VertSele(vertList)
				Blen.Edit()
				bpy.context.object.active_material_index = 0
				bpy.ops.object.material_slot_assign()
				Blen.Edit()
				# lip lower
				vertList = [24, 27, 30, 33, 53, 54, 55, 64, 65, 66, 67, 80, 81, 82, 83, 89, 90, 91, 92, 93, 94, 95, 104, 105, 106, 107, 113, 114, 115, 116, 117, 118, 119, 128, 129, 130, 131, 137, 138, 139, 140, 141, 142, 143, 152, 153, 154, 155, 161, 162, 163, 164, 165, 166, 167, 176, 177, 178, 179, 185, 186, 187, 188, 189, 190, 191, 192]
				Blen.VertDese()
				Blen.VertSele(vertList)
				Blen.Edit()
				bpy.context.object.active_material_index = 1
				bpy.ops.object.material_slot_assign()
				Blen.Edit()
				# lip upper
				vertList = [1, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 72, 73, 74, 75, 76, 77, 78, 79, 84, 85, 86, 87, 88, 89, 96, 97, 98, 99, 100, 101, 102, 103, 108, 109, 110, 111, 112, 113, 120, 121, 122, 123, 124, 125, 126, 127, 132, 133, 134, 135, 136, 137, 144, 145, 146, 147, 148, 149, 150, 151, 156, 157, 158, 159, 160, 161, 168, 169, 170, 171, 172, 173, 174, 175, 180, 181, 182, 183, 184, 185, 192]				
				Blen.VertDese()
				Blen.VertSele(vertList)
				Blen.Edit()
				bpy.context.object.active_material_index = 2
				bpy.ops.object.material_slot_assign()
				Blen.Edit()
				# skin
				vertList = [25, 26, 28, 29, 31, 32, 34, 35, 48, 49, 50, 57, 58, 59, 60, 61, 62, 63, 68, 69, 70, 71]
				Blen.VertDese()
				Blen.VertSele(vertList)
				Blen.Edit()
				bpy.context.object.active_material_index = 3
				bpy.ops.object.material_slot_assign()
				Blen.Edit()
			if a == 9:
				# TODO: skin
				Blen.MateSet_("liner")

	

	tole = 0.0001
	"""
	# stitch
	grouDict = {}
	for a in range(len(overlap_)):
		grouDict.update({overlap_[a][0]:a})
	#grouExtr = []
	#for a in range(len(overlap_)):
	#	grouExtr.append([])
	tole = 0.0001
	a = 0
	while a < len(seam):
		sea_ = []
		sea_.append(seam[a])
		a += 1
		while a < len(seam) and seam[a][0] == sea_[0][0] and seam[a][1] == sea_[0][1] and seam[a][2] == sea_[0][2]:
			sea_.append(seam[a])
			a += 1
		vect = []
		for b in range(len(sea_)):
			Blen.Sele(sea_[b][4])
			vect.append(tuple(bpy.context.object.data.vertices[sea_[b][3]].co))
		vect = Math.VectAver(vect)
		for b in range(len(sea_)):
			Blen.Sele(sea_[b][4])
			#loca = Math.Vect(tuple(bpy.context.object.data.vertices[sea_[b][3]].co), vect)

			# update group list
			for c in range(len(grouList[grouDict[sea_[b][4]]])):
				#print("c 1"
				#if grouList[grouDict[sea_[b][4]]][c] == tuple(bpy.context.object.data.vertices[sea_[b][3]].co):
				if Math.VectMagn(Math.Vect(grouList[grouDict[sea_[b][4]]][c], tuple(bpy.context.object.data.vertices[sea_[b][3]].co))) <= tole:
					grouList[grouDict[sea_[b][4]]][c] = vect

			#Blen.VertDese()
			#Blen.VertSele([sea_[b][3]])
			#Blen.VertTran(loca)
			#Blen.VertDese()

			bpy.context.object.data.vertices[sea_[b][3]].co = vect

	"""

	























	###################

	node = [{}, {}, {}, {}, {}, {}, {}]
	node[0].update({"brow" : -1})
	node[0].update({"nose" : -1})
	node[0].update({"eyesockets" : -1})
	node[1].update({"brow" : -1})
	node[1].update({"eyesockets" : -1})
	node[1].update({"cheeks_upper" : -1})
	node[2].update({"nose" : -1})
	node[2].update({"eyesockets" : -1})
	node[2].update({"cheeks_upper" : -1})
	node[3].update({"nose" : -1})
	node[3].update({"cheeks_upper" : -1})
	node[3].update({"cheeks_lower" : -1})
	node[4].update({"nose" : -1})
	node[4].update({"cheeks_lower" : -1})
	node[4].update({"mouth" : -1})
	node[5].update({"cheeks_lower" : -1})
	node[5].update({"mouth" : -1})
	node[5].update({"chin" : -1})
	node[5].update({"jaw" : -1})
	node[6].update({"chin" : -1})
	node[6].update({"jaw" : -1})
	node[6].update({"neck" : -1})

	loop = {}
	loop.update({"forehead" : []})
	loop.update({"brow" : []})
	loop.update({"nose" : []})
	loop.update({"eyesockets" : []})
	loop.update({"eyes" : []})
	loop.update({"cheeks_upper" : []})
	loop.update({"cheeks_lower" : []})
	loop.update({"mouth" : []})
	loop.update({"lips" : []})
	loop.update({"chin" : []})
	loop.update({"jaw" : []})
	loop.update({"neck" : []})
	
	# forehead / brow
	Blen.Sele("forehead")
	edgeList = Blen.EdgeList()
	# TODO: probably dont need leng
	# TODO: change reverse to posi / nega
	loop["forehead"].append(LoopGet_Loca(leng = 38))
	loo1 = LoopGet_Loca(axis = 1, leng = 15)
	star = LoopComm(loop["forehead"][0], loo1)
	loop["forehead"][0] = LoopSort(star, len(loop["forehead"][0]), loop["forehead"][0], edgeList)

	#print("15", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("brow")
	edgeList = Blen.EdgeList()
	# top
	loo1 = LoopGet_Loca(reverse = True, leng = 38)
	loo2 = LoopGet_Loca(axis = 1, leng = 4)
	star = LoopComm(loo1, loo2)
	loop["brow"].append(LoopSort(star, len(loo1), loo1, edgeList))

	# bottom
	loo1 = LoopGet_Loca(leng = 36)
	star = LoopStar(loo1)
	loo1 = LoopSort(star, len(loo1), loo1, edgeList)
	# seg 1
	# TODO: this could be two different functions, a sort, and loop[a:b]
	loop["brow"].append(LoopSort(star, 13, loo1, edgeList))
	node[0]["brow"] = loop["brow"][1][len(loop["brow"][1]) - 1]
	star = loop["brow"][1][len(loop["brow"][1]) - 1]
	# seg 2
	loop["brow"].append(LoopSort(star, 13, loo1, edgeList))
	star = loop["brow"][2][len(loop["brow"][2]) - 1]
	node[1]["brow"] = star
	loop["brow"].append(LoopSort(star, 12, loo1, edgeList, exclList = loop["brow"][2]))
	loop["brow"][3] = Loo3Fini(loop["brow"][1], loop["brow"][2], loop["brow"][3], edgeList)

	#print("16", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("nose")
	edgeList = Blen.EdgeList()
	loop["nose"].append(LoopGet_Loca(reverse = True, leng = 13))
	star = LoopStar(loop["nose"][0])
	loop["nose"][0] = LoopSort(star, len(loop["nose"][0]), loop["nose"][0], edgeList)
	node[0]["nose"] = loop["nose"][0][len(loop["nose"][0]) - 1]
	loo1 = LoopGet_Loca(reverse = True, axis = 1, leng = 38)
	loo1 = LoopSort(loop["nose"][0][len(loop["nose"][0]) - 1], len(loo1), loo1, edgeList)
	loop["nose"].append(loo1[0 : 9])
	loop["nose"].append(loo1[8 : 15])
	node[2]["nose"] = loop["nose"][len(loop["nose"]) - 1][0]
	node[3]["nose"] = loop["nose"][len(loop["nose"]) - 1][len(loop["nose"][len(loop["nose"]) - 1]) - 1]
	loop["nose"].append(loo1[14 : 21])
	node[4]["nose"] = loop["nose"][len(loop["nose"]) - 1][len(loop["nose"][len(loop["nose"]) - 1]) - 1]
	mini = -1.0
	star = -1
	for a in range(len(loop["nose"][3])):
		loca = tuple(bpy.context.object.data.vertices[loop["nose"][3][a]].co)
		if star == -1 or loca[1] < mini:
			mini = loca[1]
			star = a
	star = loop["nose"][3][star]
	loop["nose"][3] = LoopSort(star, len(loop["nose"][3]), loop["nose"][3], edgeList)

	#print("17", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("eyes")
	edgeList = Blen.EdgeList()
	loop["eyes"].append(LoopOuts(loopCoun = 3, outs = True))
	loop["eyes"][0] = LoopSort(loop["eyes"][0][0], len(loop["eyes"][0]), loop["eyes"][0], edgeList)

	Blen.Sele("eyesockets")
	edgeList = Blen.EdgeList()
	loo1 = LoopOuts(loopCoun = 3)
	loop["eyesockets"].append(LoopEyes(loo1, edgeList, 13))
	star = StarSegm(loop["eyesockets"][0], edgeList)
	loop["eyesockets"][0] = LoopSort(star, len(loop["eyesockets"][0]), loop["eyesockets"][0], edgeList)
	node[0]["eyesockets"] = loop["eyesockets"][0][0]
	node[1]["eyesockets"] = loop["eyesockets"][0][len(loop["eyesockets"][0]) - 1]
	loop["eyesockets"].append(LoopEyes(loo1, edgeList, 9, spli = 2, meth = 0))
	# TODO: meth
	star = StarSegm(loop["eyesockets"][1], edgeList, meth = 3)
	loop["eyesockets"][1] = LoopSort(star, len(loop["eyesockets"][1]), loop["eyesockets"][1], edgeList)
	node[2]["eyesockets"] = loop["eyesockets"][1][len(loop["eyesockets"][1]) - 1]
	loop["eyesockets"].append([])
	for a in range(len(loo1)):
		if (loo1[a] in loop["eyesockets"][0]) == False and (loo1[a] in loop["eyesockets"][1]) == False:
			loop["eyesockets"][2].append(loo1[a])
	loop["eyesockets"][2].append(loop["eyesockets"][0][len(loop["eyesockets"][0]) - 1])
	loop["eyesockets"][2].append(loop["eyesockets"][1][len(loop["eyesockets"][1]) - 1])
	loop["eyesockets"][2] = LoopSort(loop["eyesockets"][1][len(loop["eyesockets"][1]) - 1], len(loop["eyesockets"][2]), loop["eyesockets"][2], edgeList)
	loop["eyesockets"].append(LoopOuts(loopCoun = 3, outs = False))
	loop["eyesockets"][3] = LoopSort(loop["eyesockets"][3][0], len(loop["eyesockets"][3]), loop["eyesockets"][3], edgeList)
	mini = -1.0
	inde = -1
	a = 0
	while a < 46:
		Blen.Sele("eyesockets")
		loop["eyesockets"][3] = LoopSort(loop["eyesockets"][3][a], len(loop["eyesockets"][3]), loop["eyesockets"][3], edgeList)
		min_ = 0.0
		for b in range(len(loop["eyesockets"][3])):
			Blen.Sele("eyesockets")
			loc1 = tuple(bpy.context.object.data.vertices[loop["eyesockets"][3][b]].co)
			Blen.Sele("eyes")
			loc2 = tuple(bpy.context.object.data.vertices[loop["eyes"][0][b]].co)
			min_ += Math.VectMagn(Math.Vect(loc1, loc2))
		if inde == -1 or min_ < mini:
			mini = min_
			inde = a
		a += 1
	Blen.Sele("eyesockets")
	loop["eyesockets"][3] = LoopSort(loop["eyesockets"][3][inde], len(loop["eyesockets"][3]), loop["eyesockets"][3], edgeList)
	loop["eyesockets"][3] = LoopSort(loop["eyesockets"][3][int(46 / 2)], len(loop["eyesockets"][3]), loop["eyesockets"][3], edgeList)	

	Blen.Sele("cheeks_upper")
	edgeList = Blen.EdgeList()
	loop["cheeks_upper"].append(LoopGet_Loca(reverse = True, leng = 15))
	star = LoopStar(loop["cheeks_upper"][0], meth = 1)
	loop["cheeks_upper"][0] = LoopSort(star, len(loop["cheeks_upper"][0]), loop["cheeks_upper"][0], edgeList)
	node[1]["cheeks_upper"] = loop["cheeks_upper"][0][0]
	loop["cheeks_upper"].append(LoopGet_(leng = 27))
	star = LoopStar(loop["cheeks_upper"][1], meth = -2)
	loop["cheeks_upper"][1] = LoopSort(star, len(loop["cheeks_upper"][1]), loop["cheeks_upper"][1], edgeList)
	node[2]["cheeks_upper"] = loop["cheeks_upper"][1][0]
	loop["cheeks_upper"].append(LoopGet_Loca(reverse = False, axis = 1, leng = 7))
	star = LoopStar(loop["cheeks_upper"][2])
	loop["cheeks_upper"][2] = LoopSort(star, len(loop["cheeks_upper"][2]), loop["cheeks_upper"][2], edgeList)
	node[3]["cheeks_upper"] = loop["cheeks_upper"][2][len(loop["cheeks_upper"][2]) - 1]
	loop["cheeks_upper"].append(LoopGet_Loca(reverse = False, axis = 2, leng = 30))
	star = LoopStar(loop["cheeks_upper"][3])
	loop["cheeks_upper"][3] = LoopSort(star, len(loop["cheeks_upper"][3]), loop["cheeks_upper"][3], edgeList)

	#print("19", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("cheeks_lower")
	edgeList = Blen.EdgeList()
	# top
	loo1 = LoopGet_Loca(reverse = True, leng = 36)
	star = LoopStar(loo1)
	loo1 = LoopSort(star, len(loo1), loo1, edgeList)
	loop["cheeks_lower"].append(loo1[0:7])
	loop["cheeks_lower"].append(loo1[6:len(loo1)])
	Blen.VertSele(loop["cheeks_lower"][1])
	node[3]["cheeks_lower"] = loo1[6]
	node[4]["cheeks_lower"] = loo1[0]
	# bottom
	loop["cheeks_lower"].append(LoopGet_Loca(leng = 32))
	star = LoopStar(loop["cheeks_lower"][2])
	loop["cheeks_lower"][2] = LoopSort(star, len(loop["cheeks_lower"][2]), loop["cheeks_lower"][2], edgeList)
	# left
	loop["cheeks_lower"].append(LoopGet_Loca(axis = 1, leng = 13))
	star = LoopStar(loop["cheeks_lower"][3])
	loop["cheeks_lower"][3] = LoopSort(star, len(loop["cheeks_lower"][3]), loop["cheeks_lower"][3], edgeList)
	node[5]["cheeks_lower"] = loop["cheeks_lower"][2][0]

	Blen.Sele("mouth")
	edgeList = Blen.EdgeList()
	# inside
	loop["mouth"].append(LoopGet_(leng = 24))
	star = LoopStar(loop["mouth"][0], meth = 3)
	loop["mouth"][0] = LoopSort(star, len(loop["mouth"][0]), loop["mouth"][0], edgeList)
	# outside plus top mid
	loo1 = LoopGet_Loca(leng = 26)
	star = LoopComm(loo1, loop["mouth"][0])
	loo1 = LoopSort(star, 26, loo1, edgeList)
	loo1 = loo1[2:len(loo1)]
	# loop cheek
	loop["mouth"].append(loo1[0:13])
	loop["mouth"].append(loo1[12:len(loo1)])
	node[4]["mouth"] = loop["mouth"][1][0]
	node[5]["mouth"] = loop["mouth"][1][len(loop["mouth"][1]) - 1]

	#print("20", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("lips")
	edgeList = Blen.EdgeList()
	loop["lips"].append(LoopGet_Loca(reverse = True, leng = 24))
	star = LoopStar(loop["lips"][0], meth = 3)
	loop["lips"][0] = LoopSort(star, len(loop["lips"][0]), loop["lips"][0], edgeList)

	#print("21", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("chin")
	edgeList = Blen.EdgeList()
	# top
	loop["chin"].append(LoopGet_Loca(reverse = True, leng = 12))
	# TODO: reversing
	star = LoopStar(loop["chin"][0], meth = 2)
	#star = LoopStar(loop["chin"][0])
	loop["chin"][0] = LoopSort(star, len(loop["chin"][0]), loop["chin"][0], edgeList)
	node[5]["chin"] = loop["chin"][0][0]
	# bottom
	loop["chin"].append(LoopGet_Loca(leng = 12))
	star = LoopStar(loop["chin"][1])
	loop["chin"][1] = LoopSort(star, len(loop["chin"][1]), loop["chin"][1], edgeList)
	# side
	loop["chin"].append(LoopGet_Loca(axis = 1, reverse = True, leng = 8))
	star = LoopStar(loop["chin"][2], meth = 3)
	loop["chin"][2] = LoopSort(star, len(loop["chin"][2]), loop["chin"][2], edgeList)
	node[6]["chin"] = loop["chin"][2][len(loop["chin"][2]) - 1]

	#print("22", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("jaw")
	edgeList = Blen.EdgeList()
	# top
	loop["jaw"].append(LoopGet_Loca(reverse = True, leng = 32))
	star = LoopStar(loop["jaw"][0])
	node[5]["jaw"] = star
	loop["jaw"][0] = LoopSort(star, len(loop["jaw"][0]), loop["jaw"][0], edgeList)
	# bottom
	loop["jaw"].append(LoopGet_Loca(leng = 32))
	star = LoopStar(loop["jaw"][1])
	node[6]["jaw"] = star
	loop["jaw"][1] = LoopSort(star, len(loop["jaw"][1]), loop["jaw"][1], edgeList)
	# side
	loop["jaw"].append(LoopGet_Loca(axis = 1, leng = 8))
	star = LoopStar(loop["jaw"][2])
	loop["jaw"][2] = LoopSort(star, len(loop["jaw"][2]), loop["jaw"][2], edgeList)

	#print("23", time.clock())
	if time.clock() > breaTime:
		return 0

	Blen.Sele("neck")
	edgeList = Blen.EdgeList()
	loo1 = LoopGet_Loca(reverse = True, leng = 43)
	star = LoopStar(loo1)
	loo1 = LoopSort(star, len(loo1), loo1, edgeList)
	loop["neck"].append(loo1[0 : 12])
	node[6]["neck"] = loop["neck"][0][len(loop["neck"][0]) - 1]
	loop["neck"].append(loo1[11 : len(loo1)])
	for a in range(len(node)):
		loca = []
		for key in node[a]:
			Blen.Sele(key)
			loca.append(tuple(bpy.context.object.data.vertices[node[a][key]].co))
		loca = Math.VectAver(loca)
		for key in node[a]:
			Blen.Sele(key)
			bpy.context.object.data.vertices[node[a][key]].co = loca

	#print("24", time.clock())
	if time.clock() > breaTime:
		return 0

	# stitch

	obj1 = "forehead"
	loo1 = loop[obj1][0]
	obj2 = "brow"
	loo2 = loop[obj2][0]
	leng = 0
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("25", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "brow"
	loo1 = loop[obj1][1]
	obj2 = "nose"
	loo2 = loop[obj2][0]
	leng = 0
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("26", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "brow"
	loo1 = loop[obj1][2]
	obj2 = "eyesockets"
	loo2 = loop[obj2][0]
	leng = 2
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("27", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "brow"
	loo1 = loop[obj1][3]
	obj2 = "cheeks_upper"
	loo2 = loop[obj2][0]
	leng = 3
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("28", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "nose"
	loo1 = loop[obj1][1]
	obj2 = "eyesockets"
	loo2 = loop[obj2][1]
	leng = 1
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("29", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "eyesockets"
	loo1 = loop[obj1][2]
	obj2 = "cheeks_upper"
	loo2 = loop[obj2][1]
	leng = 1
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("30", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "eyesockets"
	loo1 = loop[obj1][3]
	obj2 = "eyes"
	loo2 = loop[obj2][0]
	leng = 0
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("31", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "nose"
	loo1 = loop[obj1][2]
	obj2 = "cheeks_upper"
	loo2 = loop[obj2][2]
	leng = 2
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("32", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "cheeks_upper"
	loo1 = loop[obj1][3]
	obj2 = "cheeks_lower"
	loo2 = loop[obj2][1]
	leng = 3
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("33", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "nose"
	loo1 = loop[obj1][3]
	obj2 = "cheeks_lower"
	loo2 = loop[obj2][0]
	leng = 2
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("34", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "mouth"
	loo1 = loop[obj1][0]
	obj2 = "lips"
	loo2 = loop[obj2][0]
	leng = 0
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("35", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "mouth"
	loo1 = loop[obj1][1]
	obj2 = "cheeks_lower"
	loo2 = loop[obj2][3]
	leng = 2
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("36", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "cheeks_lower"
	loo1 = loop[obj1][2]
	obj2 = "jaw"
	loo2 = loop[obj2][0]
	leng = 3
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("37", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "mouth"
	loo1 = loop[obj1][2]
	obj2 = "chin"
	loo2 = loop[obj2][0]
	leng = 3
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("38", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "chin"
	loo1 = loop[obj1][2]
	obj2 = "jaw"
	loo2 = loop[obj2][2]
	leng = 2
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("39", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "chin"
	loo1 = loop[obj1][1]
	obj2 = "neck"
	loo2 = loop[obj2][0]
	leng = 1
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("40", time.clock())
	if time.clock() > breaTime:
		return 0

	obj1 = "jaw"
	loo1 = loop[obj1][1]
	obj2 = "neck"
	loo2 = loop[obj2][1]
	leng = 3
	Stic(obj1, loo1, obj2, loo2, leng)

	#print("41", time.clock())
	if time.clock() > breaTime:
		return 0

	##################################























	











	# record group positions
	grouList = []
	for a in range(len(overlap_)):
		Blen.Sele(overlap_[a][0])
		Blen.VertSeleAll_()
		vertList = Blen.VertListSele()
		for b in range(len(vertList)):
			vertList[b] = tuple(bpy.context.object.data.vertices[vertList[b]].co)
		Blen.VertDese()
		grouList.append(vertList)

	Blen.Sele("neck")
	Blen.Join("jaw")
	Blen.Join("chin")
	Blen.Join("mouth")
	Blen.Join("lips")
	Blen.Join("cheeks_lower")
	Blen.Join("nose")
	Blen.Join("cheeks_upper")
	Blen.Join("eyesockets")
	Blen.Join("eyes")
	Blen.Join("brow")
	Blen.Join("forehead")
	Blen.Name("face")

	# remove doubles
	Blen.VertSeleAll_()
	Blen.VertDoub()
	Blen.VertDese()

	# create groups
	for a in range(len(bpy.context.object.data.vertices)):
		for b in range(len(grouList)):
			for c in range(len(grouList[b])):
				if type(grouList[b][c]) == tuple and Math.VectMagn(Math.Vect(grouList[b][c], tuple(bpy.context.object.data.vertices[a].co))) <= tole:
					grouList[b][c] = a
	for a in range(len(grouList)):
		b = len(grouList[a]) - 1
		while b >= 0:
			if type(grouList[a][b]) == tuple:
				grouList[a].pop(b)
			b -= 1
	for a in range(len(grouList)):
		Blen.VertGrou(overlap_[a][0], lis_ = grouList[a])

	# center group
	grou = []
	for a in range(len(bpy.context.object.data.vertices)):
		if bpy.context.object.data.vertices[a].co.y == 0.0:
			grou.append(a)

	Blen.VertSele(grou)
	Blen.Edit()
	bpy.ops.mesh.loop_multi_select()
	Blen.Edit()
	grou = Blen.VertListSele()

	# randomize
	coun = len(bpy.context.object.data.vertices)
	offs = 0.004
	smoo = 5
	random.seed()
	rand = random.randint(1, coun)
	sele = []
	for a in range(coun):
		sele.append(False)
	seleList = []
	a = 0
	while a < rand:
		random.seed()
		ran_ = random.randint(0, coun - 1)
		if sele[ran_] == False:
			seleList.append(ran_)
			sele[ran_] = True
			a += 1

	Blen.VertSele(seleList)
	Blen.Edit()
	bpy.ops.transform.vertex_random(offset = offs)
	for a in range(smoo):
		bpy.ops.mesh.vertices_smooth(factor = 1)
	Blen.Edit()
	Blen.VertDese()
	Blen.VertGrou('Group', lis_ = grou)
	Blen.VertGrouSele('Group')
	Blen.Edit()
	Blen.Scal((1.0, 0.0, 1.0))
	Blen.Edit()
	Blen.CursTo__Sele(edit = True)
	loca = Blen.CursRead()
	Blen.Edit()
	# TODO
	bpy.ops.transform.translate(value=(0, -loca[1], 0), constraint_axis=(False, True, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
	Blen.Edit()


main()

