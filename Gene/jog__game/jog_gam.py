import importlib.util
import os

path = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Pyth" + os.sep + "Modu" + os.sep + "Modu.py"
spec = importlib.util.spec_from_file_location("Modu", path)
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

def main():

	import math
	import bpy
	import random

	pi = math.pi
	fps_ = 30

	random.seed()
	spee = 1.0 + 2.0 * random.random()
	random.seed()
	armsRadi = 0.1 + 0.2 * random.random()
	random.seed()
	legsRadi = 0.3 + 0.6 * random.random()
	random.seed()
	armsRati = 0.5 * random.random()
	#armsRati = 0.0
	random.seed()
	ampl = 0.01 + 0.04
	random.seed()
	tilt = 8.0 + 8.0 * random.random()

	random.seed()
	seed = random.randint(0, 100000)
	random.seed()
	offset = 0.2 * random.random()
	Blen.Sele("pathLegs")

	Blen.VertSeleAll_()
	Blen.Edit()
	bpy.ops.transform.vertex_random(offset = offset, seed = seed)
	bpy.ops.mesh.vertices_smooth()
	Blen.Edit()
	
	random.seed()
	seed = random.randint(0, 100000)
	random.seed()
	offset = 0.2 * random.random()
	Blen.Sele("pathArms")
	Blen.VertSeleAll_()
	Blen.Edit()
	bpy.ops.transform.vertex_random(offset = offset, seed = seed)
	bpy.ops.mesh.vertices_smooth()
	Blen.Edit()

	#name = "beam"
	name = "matt"
	# TODO: will this give an exact loop?
	#end_ = 30

	# TODO: make this a function. make sure it works generally
	shouPosi = (bpy.data.objects[name + ".shou.l"].location[0], bpy.data.objects[name + ".shou.l"].location[1], bpy.data.objects[name + ".shou.l"].location[2])
	elboPosi = (bpy.data.objects[name + ".elbo.l"].location[0], bpy.data.objects[name + ".elbo.l"].location[1], bpy.data.objects[name + ".elbo.l"].location[2])
	wrisPosi = (bpy.data.objects[name + ".wris.l"].location[0], bpy.data.objects[name + ".wris.l"].location[1], bpy.data.objects[name + ".wris.l"].location[2])
	handPosi = (bpy.data.objects[name + ".hand.l"].location[0], bpy.data.objects[name + ".hand.l"].location[1], bpy.data.objects[name + ".hand.l"].location[2])
	bice = Math.VectMagn(Math.Vect(shouPosi, elboPosi))
	fore = Math.VectMagn(Math.Vect(wrisPosi, elboPosi))
	hip_Posi = (bpy.data.objects[name + ".hip_.l"].location[0], bpy.data.objects[name + ".hip_.l"].location[1], bpy.data.objects[name + ".hip_.l"].location[2])
	kneePosi = (bpy.data.objects[name + ".knee.l"].location[0], bpy.data.objects[name + ".knee.l"].location[1], bpy.data.objects[name + ".knee.l"].location[2])
	anklPosi = (bpy.data.objects[name + ".ankl.l"].location[0], bpy.data.objects[name + ".ankl.l"].location[1], bpy.data.objects[name + ".ankl.l"].location[2])
	footPosi = (bpy.data.objects[name + ".foot.l"].location[0], bpy.data.objects[name + ".foot.l"].location[1], bpy.data.objects[name + ".foot.l"].location[2])
	thig = Math.VectMagn(Math.Vect(hip_Posi, kneePosi))
	shin = Math.VectMagn(Math.Vect(footPosi, kneePosi))

	angl = (1.0, 0.0)

	Blen.Sele(name + "." + "body")
	body_height = Blen.LocaRead()
	body_height = body_height[2]
	#body_height = 0.0

	#Blen.Sele(name + "." + "body")
	Blen.Rota((0.0, tilt, 0.0))
	#Blen.Key_Rota(None, None)
	bpy.context.object.keyframe_insert("rotation_euler")

	pathLegs = []
	Blen.Sele("pathLegs")
	a = 0
	while a < len(bpy.context.object.data.vertices):
		vert = bpy.context.object.data.vertices[a]
		pathLegs.append(tuple(vert.co))
		a += 1
	pathArms = []
	Blen.Sele("pathArms")
	a = 0
	while a < len(bpy.context.object.data.vertices):
		vert = bpy.context.object.data.vertices[a]
		pathArms.append(tuple(vert.co))
		a += 1

	for a in range(len(pathLegs)):
		pathLegs[a] = (pathLegs[a][0], 0.0, pathLegs[a][2])
	for a in range(len(pathArms)):
		pathArms[a] = (pathArms[a][0], 0.0, pathArms[a][2])

	a = bpy.context.scene.frame_current
	# TODO:
	#star = 11
	#star = 2
	star = 0
	while a < end_:

		t = a / fps_

		Blen.Cycl(name = name, axle = name + ".axle.arms.l", t = t, radi = armsRadi, spee = spee, uppe = name + ".shou.l", lowe = name + ".elbo.l", end_ = name + ".hand.l", righ = False, arms = True, armsRati = armsRati, uppeLeng = bice, loweLeng = fore, faci = angl, pathStar = star, path = pathArms)
		#Blen.Key_Rota(name + ".shou.l", None)
		#Blen.Key_Rota(name + ".elbo.l", None)
		Blen.Sele(name + ".shou.l")
		bpy.context.object.keyframe_insert("rotation_euler")
		Blen.Sele(name + ".elbo.l")
		bpy.context.object.keyframe_insert("rotation_euler")

		Blen.Cycl(name = name, axle = name + ".axle.arms.r", t = t, radi = armsRadi, spee = spee, uppe = name + ".shou.r", lowe = name + ".elbo.r", end_ = name + ".hand.r", righ = True, arms = True, armsRati = armsRati, uppeLeng = bice, loweLeng = fore, faci = angl, pathStar = star, path = pathArms)	
		#Blen.Key_Rota(name + ".shou.r", None)
		#Blen.Key_Rota(name + ".elbo.r", None)
		Blen.Sele(name + ".shou.r")
		bpy.context.object.keyframe_insert("rotation_euler")
		Blen.Sele(name + ".elbo.r")
		bpy.context.object.keyframe_insert("rotation_euler")

		Blen.Cycl(name = name, axle = name + ".axle.legs.l", t = t, radi = legsRadi, spee = spee, uppe = name + ".hip_.l", lowe = name + ".knee.l", end_ = name + ".foot.l", righ = False, arms = False, armsRati = armsRati, uppeLeng = thig, loweLeng = shin, faci = angl, pathStar = star, path = pathLegs)	
		#Blen.Key_Rota(name + ".hip_.l", None)
		#Blen.Key_Rota(name + ".knee.l", None)
		Blen.Sele(name + ".hip_.l")
		bpy.context.object.keyframe_insert("rotation_euler")
		Blen.Sele(name + ".knee.l")
		bpy.context.object.keyframe_insert("rotation_euler")

		Blen.Cycl(name = name, axle = name + ".axle.legs.r", t = t, radi = legsRadi, spee = spee, uppe = name + ".hip_.r", lowe = name + ".knee.r", end_ = name + ".foot.r", righ = True, arms = False, armsRati = armsRati, uppeLeng = thig, loweLeng = shin, faci = angl, pathStar = star, path = pathLegs)	
		#Blen.Key_Rota(name + ".hip_.r", None)
		#Blen.Key_Rota(name + ".knee.r", None)
		Blen.Sele(name + ".hip_.r")
		bpy.context.object.keyframe_insert("rotation_euler")
		Blen.Sele(name + ".knee.r")
		bpy.context.object.keyframe_insert("rotation_euler")

		Blen.Sele(name + ".body")
		z = body_height + ampl * math.sin(spee * t * 4.0 * math.pi)
		bpy.context.object.location = (bpy.context.object.location[0], bpy.context.object.location[1], z)
		#bpy.ops.anim.keyframe_insert(type='Location', confirm_success=False)
		bpy.context.object.keyframe_insert("location")

		bpy.context.scene.frame_current += 1
		a += 1

	# TODO: 
	# do this with Gene
	# write iden
	exte = True
	paraDict = {}
	paraDict.update({"spee": spee})
	paraDict.update({"armsRadi": armsRadi})
	paraDict.update({"legsRadi": legsRadi})
	paraDict.update({"armsRati": armsRati})
	paraDict.update({"ampl": ampl})
	paraDict.update({"tilt": tilt})

	#direOut = dire + "out_" + os.sep + pref + "_" + numb + "_para"
	direOut = dire + "out_" + os.sep + "jog_" + "_" + numb + "_para"
	Gene.ParaWrit(para = paraDict, dire = direOut, exte = exte)

	#bpy.ops.wm.save_as_mainfile(filepath = dire + "out_" + os.sep + pref + "_" + numb + ".blend")
	bpy.ops.wm.save_as_mainfile(filepath = dire + "out_" + os.sep + "jog_" + "_" + numb + ".blend")

main()
