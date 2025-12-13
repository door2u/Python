
"""
def PythLink(Pyth = None):
	return Pyth
"""
def MathLink(Math = None):
	return Math
def BlenLink(Blen = None):
	return Blen
def BlenGameLink(BlenGame = None):
	return BlenGame
"""
def BlenCommLink(blenComm = None):
	return blenComm
def BlenDireLink(blenDire = None):
	return blenDire
def GeneDireLink(geneDire = None):
	return geneDire
def GeneContLink(geneCont = None):
	return geneCont
def HeadLink(Head = None):
	return Head
"""

# TODO:
# make naming definitions
# make a tall version for each node

# comp.bool. [0 or 1] . [inst]
#	comp.bool.fals. [inst]
#	comp.bool.true. [inst]
#	comp.bool. [0 or 1] . [inst] .mou1
#	comp.bool. [0 or 1] . [inst] .mou2
#	comp.bool. [0 or 1] . [inst] .mou3
#	comp.bool. [0 or 1] . [inst] .mou4

# comp.ifeq. [inst]
#	comp.ifeq. [inst] .mou1
#	comp.ifeq. [inst] .mou2
#	comp.ifeq. [inst] .mou3
#	comp.ifeq. [inst] .mou4
#	comp.ifeq. [inst] .fil3
#	comp.ifeq. [inst] .fil4
#	comp.ifeq. [inst] .spr1
#	comp.ifeq. [inst] .spr2
#	comp.ifeq. [inst] .swit

# comp.elbo. [inst]
#	comp.elbo. [inst] .thr1
#	comp.elbo. [inst] .thr2

# comp.spli. [inst]
#	comp.spli. [inst] .thr1
#	comp.spli. [inst] .thr2
#	comp.spli. [inst] .thr3

# comp.func
#	comp.func.valu
#	comp.func.mou1
#	comp.func.mou2
#	comp.func.mou3
#	comp.func.mou4
#	comp.func.mou5
#	comp.func.mou6
#	comp.func.mou7
#	comp.func.mou8

#		comp.1100. [inst] .sym1
#		comp.1100. [inst] .sym2
#		comp.1100. [inst] .sym3
#		comp.1100. [inst] .sym4

#		inve.1100. [inst] .sym1
#		inve.1100. [inst] .sym2
#		inve.1100. [inst] .sym3
#		inve.1100. [inst] .sym4

#		togg.1100. [inst] .sym1
#		togg.1100. [inst] .sym2
#		togg.1100. [inst] .sym3
#		togg.1100. [inst] .sym4

def Node(comp, impo, tall, inst):
	Blen = BlenLink()
	node = ""
	moun = ""
	grou = "loca"
	flip = False
	if impo == 0:
		node = "in__"
		moun = "mou1"
	elif impo == 1:
		if comp != "ifeq":
			node = "out_"
		else:
			node = "in__"
			flip = True
		moun = "mou2"
	elif impo == 2:
		node = "t_in"
		moun = "mou3"
	elif impo == 3:
		node = "tout"
		moun = "mou4"

	elif impo == 4:
		node = "in__"
		moun = "mou9"
		grou = "loc1"
		flip = True

	elif impo == 5:
		node = "out_"
		moun = "mou9"
		grou = "loc2"

	elif impo == 8:
		node = "in__"
		moun = "mo10"
		grou = "loc1"

	elif impo == 9:
		node = "out_"
		moun = "mo10"
		grou = "loc2"
		flip = True

	elif impo == 10:
		node = "out_"
		moun = "mou1"
		flip = True

	dic_ = Blen.Impo(blenFile = "scen/comp/node/" + node + ".blend")
	Blen.Sele(moun)
	if impo != 4 and impo != 8:
		Blen.Name("comp." + comp + "." + tall + "." + Blen.Pad_(inst) + "." + moun)
	Blen.VertDese()
	Blen.VertGrouSele(grou)
	moun = Blen.VertListSele()
	moun = Blen.VertLoca(moun)
	# TODO:
	# dont have some components renamed by blender and some renamed manually
	#	maybe take "comp" and instance off of child objects
	
	# TODO: not consistent
	Blen.Sele(node + ".000")
	Blen.Name("comp." + comp + "." + tall + "." + Blen.Pad_(inst) + "." + node)
	Blen.Loca(moun[0])
	if flip:
		# TODO: apply?
		Blen.Rota((0.0, 0.0, 180.0))
	pare = "comp." + comp + "." + tall
	if comp != "func":
		pare += "." + "000"
	Blen.Pare(pare)

def Impo(in__Inst, out_Inst, t_inInst, toutInst, boolInst, ifeqInst, toggInst, elboInst, spliInst, holeInst):
	import bpy
	Math = MathLink()
	Blen = BlenLink()
	BlenGame = BlenGameLink()
	impoList = []
	for obje in bpy.context.scene.objects:
		name = obje.name
		name = name.split(".")
		if len(name) > 3:
			if name[0] == "impo" and name[1] == "comp":
				impoList.append(obje.name)

	for obje in impoList:
		name = obje
		name = name.split(".")
		if len(name) > 3:
			if name[0] == "impo" and name[1] == "comp":
				obj_ = Blen.Sele(obje)
				#print("obj_", obj_)
				if obj_ != None:
					rota = tuple(bpy.context.object.rotation_euler)
					#print(rota)
					loca = Blen.LocaRead()
					if name[2] == "in__":
						dic_ = Blen.Impo(blenFile = "scen/comp/node/in__.blend")
						# TODO: copy import instance
						Blen.Name("comp.in__." + Blen.Pad_(in__Inst))
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "in__")
						in__Inst += 1
					if name[2] == "out_":
						dic_ = Blen.Impo(blenFile = "scen/comp/node/out_.blend")
						Blen.Name("comp.out_." + Blen.Pad_(out_Inst))
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "out_")
						out_Inst += 1
					if name[2] == "t_in":
						dic_ = Blen.Impo(blenFile = "scen/comp/node/t_in.blend")
						Blen.Name("comp.t_in." + Blen.Pad_(t_inInst))
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "t_in")
						t_inInst += 1
					if name[2] == "tout":
						dic_ = Blen.Impo(blenFile = "scen/comp/node/tout.blend")
						Blen.Name("comp.tout." + Blen.Pad_(toutInst))
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "tout")
						toutInst += 1
					if name[2] == "bool":
						#pass
						#"""
						# read options
						tall = name[3]
						# TODO: manage instances. flatten, etc.
						inst = name[4]
						node = name[5]
						valu = name[6]
						dic_ = Blen.Impo(blenFile = "scen/comp/bool/bool." + tall + ".blend")
						if node[0] == "1":
							Node("bool", 0, tall, boolInst)
						elif node[0] != "4":
							Blen.Sele("mou1")
							Blen.Dele()
						if node[0] == "3":
							Node("bool", 8, tall, boolInst)
							Node("bool", 9, tall, boolInst)
						else:
							Blen.Sele("mo10")
							Blen.Dele()
						if node[0] == "4":
							Node("bool", 10, tall, boolInst)
						if node[1] == "1":
							Node("bool", 1, tall, boolInst)
						else:
							Blen.Sele("mou2")
							Blen.Dele()
						if node[2] == "1":
							Node("bool", 2, tall, boolInst)
						else:
							Blen.Sele("mou3")
							Blen.Dele()
						if node[3] == "1":
							Node("bool", 3, tall, boolInst)
						else:
							Blen.Sele("mou4")
							Blen.Dele()
						# import valu
						#impo = ""
						#if valu == "0":
						#	impo = "fals"
						#if valu == "1":
						#	impo = "true"
						#dic_ = Blen.Impo(blenFile = "scen/comp/bool/" + impo + ".blend")
						Blen.Sele("comp.bool." + tall + ".000")
						BlenGame.Prop(propName = "valu", propType = 'BOOL')
						dic_ = Blen.Impo(blenFile = "scen/comp/bool/fals.blend")
						Blen.Name("comp.bool." + tall + "." + Blen.Pad_(boolInst) + ".0")
						Blen.Pare("comp.bool." + tall + ".000")
						if valu == "1":
							Blen.Sele("comp.bool." + tall + "." + Blen.Pad_(boolInst) + ".0")
							bpy.context.object.hide = True
							bpy.context.object.hide_render = True
							Blen.Sele("comp.bool." + tall + ".000")
							BlenGame.PropSet_(propName = "valu", propValu = True)
						dic_ = Blen.Impo(blenFile = "scen/comp/bool/true.blend")
						Blen.Name("comp.bool." + tall + "." + Blen.Pad_(boolInst) + ".1")
						Blen.Pare("comp.bool." + tall + ".000")
						if valu == "0":
							Blen.Sele("comp.bool." + tall + "." + Blen.Pad_(boolInst) + ".1")
							bpy.context.object.hide = True
							bpy.context.object.hide_render = True
							
						Blen.Sele("comp.bool." + tall + ".000")
						#Blen.Name("comp.bool." + tall + "." + Blen.Pad_(boolInst) + "." + node + "." + valu)
						Blen.Name("comp.bool." + tall + "." + Blen.Pad_(boolInst) + "." + node)
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "bool")
						boolInst += 1



						#"""
					if name[2] == "ifeq":
						# read options
						tall = name[3]
						# TODO: manage instances. flatten, etc.
						inst = name[4]
						node = name[5]
						#valu = name[6]
						dic_ = Blen.Impo(blenFile = "scen/comp/ifeq." + tall + ".blend")
						if node[0] == "1":
							Node("ifeq", 0, tall, ifeqInst)
						else:
							Blen.Sele("mou1")
							Blen.Dele()
						if node[1] == "1":
							Node("ifeq", 1, tall, ifeqInst)
							#Node("ifeq", 0, tall, ifeqInst)
						else:
							Blen.Sele("mou2")
							Blen.Dele()
						if node[2] == "1":
							Node("ifeq", 2, tall, ifeqInst)
							# TODO: delete fill?
							Blen.Sele("fil3")
							Blen.Dele()
						else:
							Blen.Sele("mou3")
							Blen.Dele()
						if node[3] == "1":
							Node("ifeq", 3, tall, ifeqInst)
							# TODO: delete fill?
							Blen.Sele("fil4")
							Blen.Dele()
						else:
							Blen.Sele("mou4")
							Blen.Dele()
						nam_ = "comp.func.ifeq." + tall + "." + Blen.Pad_(ifeqInst) + "." + node
						Blen.Sele("spr1")
						Blen.Name(nam_ + "." + "spr1")
						Blen.Sele("spr2")
						Blen.Name(nam_ + "." + "spr2")
						Blen.Sele("swit")
						Blen.Name(nam_ + "." + "swit")
						Blen.Sele("comp.ifeq." + tall + ".000")
						Blen.Name(nam_)
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "ifeq")
						ifeqInst += 1
					if name[2] == "togg":
						# read options
						tall = name[3]
						inst = name[4]
						node = name[5]
						dic_ = Blen.Impo(blenFile = "scen/comp/func." + tall + ".blend")
						Blen.Sele("mou1")
						Blen.Dele()
						Blen.Sele("mou2")
						Blen.Dele()
						Blen.Sele("mou3")
						Blen.Dele()
						Blen.Sele("mou4")
						Blen.Dele()
						Blen.Sele("mou5")
						Blen.Dele()
						Blen.Sele("mou6")
						Blen.Dele()
						Blen.Sele("mou7")
						Blen.Dele()
						Blen.Sele("mou8")
						Blen.Dele()
						Node("func", 4, tall, toggInst)
						Node("func", 5, tall, toggInst)
						# import symbol
						dic_ = Blen.Impo(blenFile = "scen/comp/togg/togg.blend")
						nam_ = "comp.func.togg." + tall + "." + Blen.Pad_(toggInst) + ".03000000"
						Blen.Sele("sym1")
						Blen.Name(nam_ + "." + "sym1")
						Blen.Pare("comp.func." + tall)
						Blen.Sele("sym2")
						Blen.Name(nam_ + "." + "sym2")
						Blen.Pare("comp.func." + tall)
						Blen.Sele("sym3")
						Blen.Name(nam_ + "." + "sym3")
						Blen.Pare("comp.func." + tall)
						Blen.Sele("sym4")
						Blen.Name(nam_ + "." + "sym4")
						Blen.Pare("comp.func." + tall)
						# rename valu
						Blen.Sele("valu")
						Blen.Name(nam_ + "." + "valu")
						Blen.Pare("comp.func." + tall)
						# select function
						Blen.Sele("comp.func." + tall)
						Blen.Name(nam_)
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "togg")
						toggInst += 1
					if name[2] == "elbo":
						tall = name[3]
						inst = name[4]
						dic_ = Blen.Impo(blenFile = "scen/comp/elbo." + tall + ".blend")
						nam_ = "comp.elbo." + tall + "." + Blen.Pad_(elboInst)
						Blen.Sele("thr1")
						Blen.Name(nam_ + "." + "thr1")
						Blen.Sele("thr2")
						Blen.Name(nam_ + "." + "thr2")
						Blen.Sele("elbo." + tall + "." + "000")
						Blen.Name(nam_)
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "elbo")
						elboInst += 1
					if name[2] == "spli":
						tall = name[3]
						inst = name[4]
						dic_ = Blen.Impo(blenFile = "scen/comp/spli." + tall + ".blend")
						nam_ = "comp.spli." + tall + "." + Blen.Pad_(spliInst)
						Blen.Sele("thr1")
						Blen.Name(nam_ + "." + "thr1")
						Blen.Sele("thr2")
						Blen.Name(nam_ + "." + "thr2")
						Blen.Sele("thr3")
						Blen.Name(nam_ + "." + "thr3")
						Blen.Sele("spli." + tall + "." + "000")
						Blen.Name(nam_)
						BlenGame.Prop(propName = "objeType", propType = 'STRING', propValu = "spli")
						spliInst += 1
					# TODO: have to cut out a part of the ground
					if name[2] == "hole":
						dic_ = Blen.Impo(blenFile = "scen/comp/hole.blend")
						Blen.Name("comp.hole." + Blen.Pad_(holeInst))
						BlenGame.Prop(propName = "obje", propType = 'STRING')
						BlenGame.Prop(propName = "objeType", propType = 'STRING')
						holeInst += 1
					# rotate
					Blen.RotaSet_(Math.VectDegr(rota))
					Blen.Loca(loca)
					#Blen.Name(name)

					#if ifeqInst == 2:
					#	return 0

	# delete import objects
	dele = True
	#dele = False
	if dele:
		for obje in impoList:
			name = obje
			name = name.split(".")
			if len(name) > 3:
				if name[0] == "impo" and name[1] == "comp":
					obj_ = Blen.Sele(obje)
					if obj_ != None:
						Blen.Dele()

	return in__Inst, out_Inst, t_inInst, toutInst, boolInst, ifeqInst, toggInst, elboInst, spliInst, holeInst

def Rena():
	import bpy
	Blen = BlenLink()
	for obje in bpy.context.scene.objects:
		name = obje.name
		name = name.split(".")
		if len(name) > 3:
			if name[0] == "impo" and name[1] == "comp":
				Blen.Sele(obje.name)
				"""
				if name[2] == "bool":
					inst = name[3]
					node = name[4]
					valu = name[5]
					tall = name[6]
					Blen.Name("impo.comp.bool." + tall + "." + inst + "." + node + "." + valu)
				"""
				if name[2] == "togg":
					inst = name[3]
					node = name[4]
					Blen.Name("impo.comp." + name[2] + "." + "0" + "." + inst + "." + node)

