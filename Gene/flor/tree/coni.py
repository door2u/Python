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

def BranSepa():

	import bpy

	obje = bpy.context.object.name

	founList = []
	for a in range(len(Blen.Vertices())):
		founList.append(False)
	# get first vertex
	vert = Blen.VertListSele()

	ver1 = -1
	ver2 = -1
	for ver_ in vert:
		conn = Blen.VertConn(ver_)
		if len(conn) == 1:
			ver1 = ver_
		else:
			ver2 = ver_

	vec1 = bpy.context.object.data.vertices[ver1].co
	vec2 = bpy.context.object.data.vertices[ver2].co
	vect = Math.Vect(vec1, vec2)
	vectList = [vect]

	vert = ver1
	founList[vert] = True
	branList = [[vert]]

	while (False in founList):
		a = 0
		leng = len(branList)
		while a < leng:
			vert = branList[a][len(branList[a]) - 1]
			vect = vectList[a]
			if vert != -1:
				# get connected
				conn = Blen.VertConn(vert)
				appe = False
				if len(conn) > 2:
					# get the location of this vertex
					vec1 = bpy.context.object.data.vertices[vert].co
					vertList = []
					for con_ in conn:
						if founList[con_] == False:
							founList[con_] = True
							vertList.append(con_)
							appe = True
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
						if ver_ == anglSmal:
							branList[a].append(ver_)
						else:
							branList.append([vert, ver_])
							leng = len(branList)
							vec1 = bpy.context.object.data.vertices[vert].co
							vec2 = bpy.context.object.data.vertices[ver_].co
							vectList.append(Math.Vect(vec1, vec2))
							
				else:
					# add the connected vertex to this branch
					for con_ in conn:
						if founList[con_] == False:
							founList[con_] = True
							branList[a].append(con_)
							appe = True

				if appe == False:
					branList[a].append(-1)

			a += 1

	adde = False
	for bran in branList:
		Blen.Sele(obje)
		bra_ = bran
		if bra_[len(bra_) - 1] == -1:
			bra_.pop()
		#print(bra_)
		vertList = Blen.VertLoca(bra_)
		Blen.Uplo([vertList, Math.EdgeLine(len(vertList) - 1), []])
		if adde:
			# TODO
			Blen.Sele("obje")
			Blen.Join("obje.001")
			#Blen.Sele("b")
			#Blen.Join("obje.001")
		if adde == False:
			adde = True
	Blen.Name("bran_temp")

def BranSkin():

	import bpy

	ringCoun = 8
	obje = "bran_temp"
	founList = []
	for a in range(len(Blen.Vertices())):
		founList.append(False)
	coun = 0
	adde = False
	while (False in founList):
		# get a connected line from start to end
		Blen.Sele(obje)
		for a in range(len(founList)):
			if founList[a] == False:
				conn = Blen.VertConn(a)
				if len(conn) == 1:
					vert = a
					break
		connList = [vert]
		founList[vert] = True
		begi = False
		while True:
			conn = Blen.VertConn(vert)
			appe = False
			for con_ in conn:
				if founList[con_] == False:
					if len(conn) == 1:
						# TODO: will the first one always be first
						if begi == False:
							begi = True
							for a in range(len(connList)):
								if connList[a] == vert:
									connList.pop(a)
									break
							connList.insert(0, vert)
					connList.append(con_)
					founList[con_] = True
					vert = con_
					appe = True
					break
			if appe == False:
				if adde:
					if len(connList) > 0:
						reve = True
						star = bpy.context.object.data.vertices[connList[0]].co
						for a in range(len(bpy.context.object.data.vertices)):
							vert = bpy.context.object.data.vertices[a]
							if a != connList[0]:
								if Math.VectSame(star, vert.co):
									reve = False
									break
						if reve:
							new_ConnList = []
							a = len(connList) - 1
							while a >= 0:
								new_ConnList.append(connList[a])
								a -= 1
							connList = new_ConnList

				vertList = []
				edgeList = []

				# get the angle
				a = 0
				while a < len(connList) - 1:
					vec1 = bpy.context.object.data.vertices[connList[a]].co
					vec2 = bpy.context.object.data.vertices[connList[a + 1]].co
					
					vece = bpy.context.object.data.vertices[connList[len(connList) - 1]].co
					vece = Math.Vect(vec1, vece)
					base = Math.VectMagn(vece) / 20.0
					anglVect = (0.0, 1.0, 0.0)
					if a == 0:
						vect = Math.Vect(vec1, vec2)
					else:
						# get a vector from previous to next
						vecp = bpy.context.object.data.vertices[connList[a - 1]].co
						vect = Math.Vect(vecp, vec2)
						
					eule = Math.VectTo__Eule3d__(vect)
					anglVect = Math.VectRota3d__(anglVect, eule)
					anglVect = Math.VectNorm(anglVect)
					anglVect = Math.VectScal(anglVect, base)

					leng = len(vertList)
					b = 0
					while b < ringCoun:
						anglVect = Math.Quat(anglVect, 360.0 / ringCoun, Math.VectNorm(vect))
						vertList.append(Math.VectAdd_(anglVect, vec1))
						if a < len(connList) - 2:
							edgeList.append((len(vertList) - 1, len(vertList) - 1 + ringCoun))
						if b != ringCoun - 1:
							edgeList.append((len(vertList) - 1, len(vertList)))
						else:
							edgeList.append((len(vertList) - 1, leng))
						b += 1
					a += 1

				vertList.append(bpy.context.object.data.vertices[connList[len(connList) - 1]].co)
				a = 0
				while a < ringCoun:
					edgeList.append((len(vertList) - 1, len(vertList) - 1 - ringCoun + a))
					a += 1

				# TODO: organize for ring select	
				
				Blen.Uplo([vertList, edgeList, []])
				coun += 1
				# TODO: make a poly list
				Blen.Edit()
				bpy.ops.mesh.edge_face_add()
				Blen.Edit()
			
				break

	for a in range(1, coun):
		Blen.Sele("obje." + Blen.Pad_(a))
		Blen.Join("obje")
		Blen.Name("obje")
	Blen.Name("bran")
	Blen.Sele("bran_temp")
	Blen.Dele()

def main():

	import bpy
	import random

	print()

	exte = False
	try:
		paraDict = para
		exte = True
		direOut = dire + "out_" + os.sep + "coni_" + numb + "_para"
		#direOut = direThis + "out_" + os.sep + "coni_" + numb + "_para"
	except:
		# TODO: where else did this get messed up?
		# TODO: call this file to list?
		paraDict = Pyth.FileTo__Line("coni_para")
		paraDict = Pyth.LineTo__Dict(paraDict)
		paraDict = Gene.ParaInit(paraDict)
		direOut = ""

	# TODO
	paraDict = {}

	Gene.ParaWrit(para = paraDict, dire = direOut, exte = exte)

	# TODO: para
	libr = "/home/christopher/Documents/prog/gene/flor/coni/libr_sort/"
	heigMaxi = 10.0
	heigMini = 2.0
	pickMaxi = 40

	anglMini = -20
	anglMaxi = 40

	######################

	fileList = os.listdir(libr)
	# get rid of files that arent blend
	a = len(fileList) - 1
	while a >= 0:
		fil_ = fileList[a]
		fil_ = fil_.split(".")
		if len(fil_) > 0:
			if fil_[len(fil_) - 1] != "blend":
				fileList.pop(a)
		a -= 1
	fileList = sorted(fileList)
	size = len(fileList)
	# pick rand to set tree height
	random.seed()
	rand = random.random()
	# range of files to be picked from
	limi = int(rand * size)
	# number of files to be picked
	pick = int(rand * pickMaxi)
	# pick
	indeList = []
	a = pick - 1
	while a >= 0:
		# TODO: always picks 0? pick some range between previous and next
		fil_ = int(a * limi / pick)
		indeList.append(fil_)
		a -= 1
	trunList = [(0.0, 0.0, 0.0)]
	# tree height
	heigTree = heigMini + rand * (heigMaxi - heigMini)
	anglList = []
	a = 0
	while a < pick:
		fil_ = fileList[indeList[a]]
		fil_ = libr + fil_
		Blen.Impo(blenFile = fil_)
		# TODO
		Blen.Sele("mate")
		Blen.Dele()
		Blen.Sele("obje")
		
		# TODO:
		bpy.ops.object.modifier_remove(modifier = "Skin")
		Blen.Appl()
		# pick z curve
		leng = bpy.context.object.dimensions[0]
		angl = anglMini + a * (anglMaxi - anglMini) / pick
		for b in range(len(bpy.context.object.data.vertices)):
			prog = bpy.context.object.data.vertices[b].co.x / leng
			prog *= angl
			bpy.context.object.data.vertices[b].co = Math.Quat(bpy.context.object.data.vertices[b].co, prog, (0.0, -1.0, 0.0))
		Blen.Name("bran")
		# TODO: skin
		#Blen.VertDese()
		#Blen.VertSele([0, 1])
		Blen.VertSele([0])
		BranSepa()
		Blen.Sele("bran")
		Blen.Dele()
		Blen.Sele("bran_temp")
		BranSkin()
		Blen.Sele("bran")
		# pick height
		heig = heigMini + a * (heigMaxi - heigMini) / pick
		bpy.context.object.location[2] = heig
		trunList.append((0.0, 0.0, heig))
		# pick angle
		angl, anglList = AnglDist(anglList)
		bpy.context.object.rotation_euler[2] = angl
		Blen.Name("bran." + Blen.Pad_(a))
		Blen.MateSet_("bark")
		#break
		a += 1
	trunList.append((0.0, 0.0, heigMini + a * (heigMaxi - heigMini) / pick))
	edgeList = Math.EdgeLine(len(trunList) - 1)
	Blen.Uplo([trunList, edgeList, []])

	# TODO
	Blen.VertSele([0])
	BranSepa()
	Blen.Sele("obje")
	Blen.Dele()
	Blen.Sele("bran_temp")
	BranSkin()
	Blen.Sele("bran")
	Blen.Name("trun")
	Blen.MateSet_("bark")

main()

