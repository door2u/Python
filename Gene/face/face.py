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


#breaTime = 10.0

"""
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
"""

def GrouInde(grouName, overlap_):
	retu = 0
	while retu < len(overlap_):
		if overlap_[retu][0] == grouName:
			break
		retu += 1
	return retu

def GrouOver(grouName, overlap_, inde):
	retu = 0
	while retu < len(overlap_[inde]):
		if overlap_[inde][retu] == grouName:
			break
		retu += 1
	return retu

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
	#loca = (0.0, 0.0, 0.27293)

	# overlap: which groups border the group in index 0
	overlap_ = []
	overlap_.append(["neck", "chin", "jaw"])
	overlap_.append(["chin", "neck", "jaw", "mouth", "cheeks_lower"])
	overlap_.append(["jaw", "neck", "chin", "mouth", "cheeks_lower"])
	overlap_.append(["mouth", "chin", "lips", "jaw", "nose", "cheeks_lower"])
	overlap_.append(["lips", "mouth"])
	overlap_.append(["cheeks_lower", "chin", "mouth", "cheeks_upper", "nose", "jaw"])
	overlap_.append(["cheeks_upper", "cheeks_lower", "nose", "eyesockets", "brow"])
	overlap_.append(["nose", "eyesockets", "mouth", "cheeks_lower", "cheeks_upper", "brow"])
	overlap_.append(["eyesockets", "eyes", "nose", "brow", "cheeks_upper"])
	overlap_.append(["eyes", "eyesockets"])
	overlap_.append(["brow", "eyesockets", "nose", "cheeks_upper", "forehead"])
	overlap_.append(["forehead", "brow"])

	# pick features from libr
	os.system("python3 /home/christopher/Documents/prog/Pyth/Gene/face/face_expo.py")

	#return 0

	"""
	# read seam data
	seam = []
	for a in range(len(overlap_)):
		line = Pyth.FileTo__Line("face/seam/seam")
		for b in range(len(line)):
			line[b] = line[b].split(" ")
			seam.append([float(line[b][0]), float(line[b][1]), float(line[b][2]), int(line[b][3]), line[b][4]])
	"""

	vertEdgeList = []

	grouList = []
	# import geometry
	for a in range(len(overlap_)):

		vertEdgeList.append([])

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

		# get vert edge list: edges that belong to vertices
		for b in range(len(vertList)):
			vertEdgeList[a].append([])
		for b in range(len(edgeList)):
			vertEdgeList[a][edgeList[b][0]].append(b)
			vertEdgeList[a][edgeList[b][1]].append(b)

		# TODO:
		#"""
		# mirror
		bpy.ops.object.modifier_add(type='MIRROR')
		#bpy.context.object.modifiers["Mirror"].use_x = False
		#bpy.context.object.modifiers["Mirror"].use_y = True
		#"""
		# TODO
		# move up
		#Blen.Loca(loca)
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
		# TODO
		if a != 4:
			Blen.MateSet_("skin")
		else:
			Blen.MateSet_("lip_lower")
		"""
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
		"""

	tole = 0.0001

	####

	# stitch

	seam = []
	nodeList = []
	# TODO: can vertList be used
	ver_List = []
	for a in range(len(overlap_)):
		seam.append([])
		nodeList.append([])
		ver_List.append([])
		for b in range(1, len(overlap_[a])):

			sea1 = Pyth.FileTo__Line("face/seam/" + overlap_[a][0] + "_" + overlap_[a][b])
			node = []
			ver_ = []
			for c in range(len(sea1)):
				sea1[c] = sea1[c].split(" ")
				node.append([])
				ver_.append(int(sea1[c][3]))
				d = 4
				while d < len(sea1[c]):
					node[c].append([int(sea1[c][d]), int(sea1[c][d + 1])])
					d += 2
				sea1[c] = (float(sea1[c][0]), float(sea1[c][1]), float(sea1[c][2]))

			seam[a].append(sea1[:])
			nodeList[a].append(node[:])
			ver_List[a].append(ver_[:])

	for a in range(len(seam)):
		for b in range(len(seam[a])):

			g2 = GrouInde(overlap_[a][b + 1], overlap_)
			g1 = GrouOver(overlap_[a][0], overlap_, g2)
			sea1 = seam[a][b][:]
			sea2 = seam[g2][g1 - 1][:]
			nod1 = nodeList[a][b]
			nod2 = nodeList[g2][g1 - 1]

			# TODO: grouping is screwed up in ver_List. a and g2 is backwards

			sea1, nod1, typ1 = Seam(sea1, overlap_[a][0], vertEdgeList[a], ver_List[g2][g1 - 1][:], nod1, debu = [a, b, "sea1"])
			nodeList[a][b] = nod1[:]
			if sea1 == 0:
				print(a, b)
				print("exited 1")
				return 0

			sea2, nod2, typ2 = Seam(sea2, overlap_[g2][0],  vertEdgeList[g2], ver_List[a][b][:], nod2, debu = [a, b, "sea2"])
			nodeList[g2][g1 - 1] = nod2[:]
			if sea2 == 0:
				print(a, b)
				print("exited 2")
				return 0

			# some seams may need to be reversed. loop seams need to be aligned
			# TODO: maybe need a type for seams that overlap on both ends
			if typ1 == 0:
				sta1 = sea1[0]
				sta2 = sea2[0]
				end2 = sea2[len(sea2) - 1]
				if Math.VectMagn(Math.Vect(sta1, end2)) < Math.VectMagn(Math.Vect(sta1, sta2)):
					se_2 = []
					c = len(sea2) - 1
					while c >= 0:
						se_2.append(sea2[c])
						c -= 1
					sea2 = se_2[:]
			# TODO
			if typ1 == 1:
				pass
				"""
				clos = 0.0
				closInde = -1
				#print(star)
				#sta1 = sea1[0]
				#sta2 = sea2[0]
				c = 0
				while c < len(sea1):
					diff = 0.0
					for d in range(c, len(sea2)):
						vect = Math.Vect(sea1[c], sea2[d])
						diff += Math.VectMagn(vect)
					for d in range(c):
						vect = Math.Vect(sea1[c], sea2[d])
						diff += Math.VectMagn(vect)
					if diff < clos or closInde == -1:
						clos = diff
						closInde = c
					c += 1
				se_2 = []
				#c = len(sea2) - 1
				#c = 0
				#while c < len(sea2):
				for c in range(len(sea2)):
					inde = c + closInde
					if inde >= len(sea2): inde -= len(sea2)
					se_2.append(sea2[inde])
					#c += 1
				sea2 = se_2[:]
				#return 0
				"""

			for c in range(len(sea1)):
				Blen.Sele(overlap_[a][0])
				# TODO: slow
				ind1 = Blen.VertIndeBy__Loca((sea1[c][0], sea1[c][1], sea1[c][2]), exac = False)
				Blen.Sele(overlap_[g2][0])
				ind2 = Blen.VertIndeBy__Loca((sea2[c][0], sea2[c][1], sea2[c][2]), exac = False)
				if ind1 != -1 and ind2 != -1:
					vert = [(sea1[c][0], sea1[c][1], sea1[c][2]), (sea2[c][0], sea2[c][1], sea2[c][2])]
					objeList = [[overlap_[a][0], ind1], [overlap_[g2][0], ind2]]

					# find nodes
					# TODO: not working
					#for d in range(len(nod1[c])):
					#	if nod1[c][d] != []:

					"""
					e = GrouInde(overlap_[a][nod1[c][d][0]], overlap_)
					f = GrouOver(overlap_[a][0], overlap_, e)
					#print("a", a, "e", e, "f", f)
					#print(node[c][d][1])
					#print(len(seam[e][f - 1]))
					vert.append(seam[e][f - 1][nod1[c][d][1]])
					Blen.Sele(overlap_[e][0])
					inde = Blen.VertIndeBy__Loca((seam[e][f - 1][nod1[c][d][1]][0], seam[e][f - 1][nod1[c][d][1]][1], seam[e][f - 1][nod1[c][d][1]][2]), exac = True)
					objeList.append([overlap_[e][0], inde])
					"""

					"""
					for e in range(len(seam) - 1):
						for g in range(e + 1, len(seam)):
							for f in range(len(seam[e])):
								for h in range(len(seam[g])):
									for i in range(len(seam[e][f])):
										for j in range(len(seam[g][h])):
											if seam[e][f][i][0] == seam[g][h][j][0] and seam[e][f][i][1] == seam[g][h][j][1] and seam[e][f][i][2] == seam[g][h][j][2]:
												#i = GrouInde(overlap_[a][nod1[c][d][0]], overlap_)
												k = GrouInde(overlap_[a][nod1[c][d][0]], overlap_)
												#j = GrouOver(overlap_[a][0], overlap_, i)
												#vert.append(seam[i][j - 1][nod1[c][d][1]])
												#vert.append(seam[g][h][nod1[c][d][1]])
												#vert.append(seam[g][h])
												#Blen.Sele(overlap_[i][0])
												Blen.Sele(overlap_[k][0])
												#inde = Blen.VertIndeBy__Loca((seam[i][j - 1][nod1[c][d][1]][0], seam[i][j - 1][nod1[c][d][1]][1], seam[i][j - 1][nod1[c][d][1]][2]), exac = True)
												#inde = Blen.VertIndeBy__Loca((seam[g][h][nod1[c][d][1]][0], seam[g][h][nod1[c][d][1]][1], seam[g][h][nod1[c][d][1]][2]), exac = True)
												#print(seam[g][h])
												#inde = Blen.VertIndeBy__Loca(seam[g][h], exac = True)
												inde = Blen.VertIndeBy__Loca(seam[g][h][j], exac = True)
												#objeList.append([overlap_[i][0], inde])
												objeList.append([overlap_[k][0], inde])
					"""

					vert = Math.VectAver(vert)

					# TODO: update nodes also
					# TODO: need to update the same vertex in other seam lists
			
					for d in range(len(seam)):
						for e in range(len(seam[d])):
							for f in range(len(seam[d][e])):
								if seam[d][e][f] == sea1[c]:
									seam[d][e][f] = vert
								if seam[d][e][f] == sea2[c]:
									seam[d][e][f] = vert
					for d in range(len(objeList)):
						Blen.Sele(objeList[d][0])
						bpy.context.object.data.vertices[objeList[d][1]].co = vert
				else:
					print(a, b, c, ind1, ind2)

	####






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

	# join all separate pieces
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
	Blen.VertDoub(threshold = 0.0001)
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

	# TODO: all center vertices might have moved
	# center group
	import math
	grou = []
	for a in range(len(bpy.context.object.data.vertices)):
		#if bpy.context.object.data.vertices[a].co.y == 0.0:
		if math.fabs(bpy.context.object.data.vertices[a].co.x) < tole:
			grou.append(a)

	if len(grou) > 0:
		Blen.VertSele(grou)
		Blen.Edit()
		bpy.ops.mesh.loop_multi_select()
		Blen.Edit()
		grou = Blen.VertListSele()

	# randomize
	coun = len(bpy.context.object.data.vertices)
	#offs = 0.004
	#offs = 0.0005
	offs = 0.00025
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
	if len(grou) > 0:
		Blen.VertGrou('Group', lis_ = grou)
		Blen.VertGrouSele('Group')
		Blen.Edit()
		#Blen.Scal((1.0, 0.0, 1.0))
		Blen.Scal((0.0, 1.0, 1.0))
		Blen.Edit()
		Blen.CursTo__Sele(edit = True)
		loca = Blen.CursRead()
		Blen.Edit()
		# TODO
		#bpy.ops.transform.translate(value=(0, -loca[1], 0), constraint_axis=(False, True, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
		bpy.ops.transform.translate(value=(-loca[0], 0, 0), constraint_axis=(True, False, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
		Blen.Edit()

	# eyes
	Blen.Impo(blenFile = "/home/christopher/Documents/prog/gene/face/othe.blend", empt = True)

def Seam(seam, obje, vertEdgeList, ver_, node, debu = []):

	typ_ = 0
	prin = True
	prin = False
	
	if prin: print("debu", debu)
	Blen.Sele(obje)
	if prin: print(obje)
	if prin: print("vertEdgeList", vertEdgeList)

	ve__List = []
	for a in range(len(seam)):
		# TODO: why doesnt exact work
		if prin: print(seam[a])
		ve__List.append(Blen.VertIndeBy__Loca(seam[a], exac = False))

	if prin: print(len(ver_), len(ve__List))
	if prin: print(ve__List)

	if len(ver_) > 1:
		edgeList = Blen.EdgeList()
		if prin: print(edgeList)
		# get the edge list for the seam
		sea1Edge = []
		whoops = False
		for c in range(len(ver_)):
			vertEdge = vertEdgeList[ver_[c]][:]
			if prin: print(c, vertEdge)
			d = len(vertEdge) - 1
			while d >= 0:
				edge = vertEdge[d]
				pop_ = False
				if prin: print("edge", edgeList[edge], "edge index", edge)
				if edgeList[edge][0] == ver_[c]:
					if prin: print(edge, edgeList[edge])
					if (edgeList[edge][1] in ver_) == False:
						pop_ = True
				if edgeList[edge][1] == ver_[c]:
					if prin: print("her2", edge, edgeList[edge])
					if (edgeList[edge][0] in ver_) == False:
						pop_ = True
				if pop_:
					vertEdge.pop(d)
				d -= 1
			if vertEdge == []:
				if prin: print("whoops")
				if prin: print(len(seam))
				if prin: print("ver_", ver_)
				whoops = True
				break
			if prin: print("popped", vertEdge)
			sea1Edge.append(vertEdge[:])

		if whoops:
			sea1Edge = []
			for c in range(len(ver_)):
				vertEdge = vertEdgeList[ve__List[c]][:]
				d = len(vertEdge) - 1
				while d >= 0:
					edge = vertEdge[d]
					pop_ = False
					if prin: print("edge", edgeList[edge], "edge index", edge)
					if edgeList[edge][0] == ve__List[c]:
						if prin: print(edge, edgeList[edge])
						if (edgeList[edge][1] in ve__List) == False:
							pop_ = True
					if edgeList[edge][1] == ve__List[c]:
						if prin: print("her2", edge, edgeList[edge])
						if (edgeList[edge][0] in ve__List) == False:
							pop_ = True
					if pop_:
						vertEdge.pop(d)
					d -= 1
				if vertEdge == []:
					if prin: print("error: vertEdge list empty")
					if prin: print(len(seam))
					if prin: print("ve__List", ve__List)
					Blen.VertSele(ve__List)
					return [0, [0], 0]
				if prin: print("popped", vertEdge)
				sea1Edge.append(vertEdge[:])

		for c in range(len(sea1Edge)):
			sea1Edge[c].append(c)
		se_1Edge = []
		end_ = len(sea1Edge)
		if prin: print(sea1Edge)
		for c in range(len(sea1Edge)):
			# TODO: seam might not end at 2 if pieces overlap on both sides
			if len(sea1Edge[c]) == 2:
				se_1Edge.append(sea1Edge[c])
				sea1Edge.pop(c)
				break
		if len(se_1Edge) > 0:
			edge = se_1Edge[0][0]
		else:
			edge = sea1Edge[0][0]
			typ_ = 1
		if prin: print(sea1Edge)
		# TODO: is this where the script is getting stuck and why
		atteLimi = 1000
		atte = 0
		leng = 1
		while leng < end_:
			for c in range(len(sea1Edge)):
				if sea1Edge[c][0] == edge:
					se_1Edge.append(sea1Edge[c])
					edge = sea1Edge[c][1]
					# TODO: does this need to be popped
					sea1Edge.pop(c)
					leng = len(se_1Edge)
					break
				if len(sea1Edge[c]) > 2 and sea1Edge[c][1] == edge:
					se_1Edge.append(sea1Edge[c])
					edge = sea1Edge[c][0]
					sea1Edge.pop(c)
					leng = len(se_1Edge)
					break
			atte += 1
			if atte > atteLimi:
				print("error: attempt limit exceeded")
				return [0, [0], 0]
			#print(leng, end_)
		se_1 = []
		nod1 = []
		for c in range(len(se_1Edge)):
			vert = seam[se_1Edge[c][len(se_1Edge[c]) - 1]]
			if (vert in se_1) == False:
				se_1.append(vert)
				nod1.append(node[se_1Edge[c][len(se_1Edge[c]) - 1]])
		seam = se_1[:]
		node = nod1[:]

	return seam, node, typ_

main()

