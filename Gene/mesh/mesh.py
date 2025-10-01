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

	# TODO:

	import bpy
	import random

	print()

	"""
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
	"""

	#Blen.Sele("matt.head")
	Blen.Sele("matt.hair")
	Blen.VertDese()

	# randomize
	coun = len(bpy.context.object.data.vertices)
	# face
	#offs = 0.004
	# matt.head
	#offs = 0.002
	# matt.hair
	offs = 0.01
	#smoo = 5
	#smoo = 1
	smoo = 0
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
	#Blen.VertGrou('Group', lis_ = grou)
	Blen.VertGrouSele('Group')
	Blen.Edit()
	Blen.Scal((1.0, 0.0, 1.0))
	Blen.Edit()
	Blen.CursTo__Sele(edit = True)
	loca = Blen.CursRead()
	#print(loca)
	Blen.Edit()
	# TODO
	bpy.ops.transform.translate(value=(0, -loca[1], 0), constraint_axis=(False, True, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
	Blen.Edit()

main()

