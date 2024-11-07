import importlib.util
import os

spec = importlib.util.spec_from_file_location("Modu", os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Modu" + os.sep + "Modu.py")
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

def main():

	import random
	import math
	import bpy

	leng = 24

	markCoun = 0
	tailDict = []
	tailDict.append(Blen.Pad_(markCoun) + "." + "spin.m." + Blen.Pad_(1))
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "spin.m." + Blen.Pad_(0))
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "neck.m")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "head.m")
	markCoun += 1
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "coll.l")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "shou.l")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "elbo.l")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "wris.l")
	markCoun += 1
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "pelv.l")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "hip_.l")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "knee.l")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "ankl.l")
	markCoun += 1
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "coll.r")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "shou.r")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "elbo.r")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "wris.r")
	markCoun += 1
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "pelv.r")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "hip_.r")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "knee.r")
	markCoun += 1
	tailDict.append(Blen.Pad_(markCoun) + "." + "ankl.r")

	# count number of files in library
	# TODO: pass directory
	librDire = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Gene" + os.sep + "pose" + os.sep + "libr" + os.sep
	fileList = os.listdir(librDire)
	fileCoun = len(fileList) / 3 - 1
	random.seed()
	ran1 = random.randint(0, fileCoun)
	ran2 = ran1
	while ran2 == ran1:
		random.seed()
		ran2 = random.randint(0, fileCoun)

	# read para file
	par1 = librDire + "pose_" + Pyth.Pad_(ran1, 4) + "_para"
	par1 = Pyth.FileTo__Line(par1)
	par1 = Pyth.LineTo__Dict(par1, conf = 0)
	par2 = librDire + "pose_" + Pyth.Pad_(ran2, 4) + "_para"
	par2 = Pyth.FileTo__Line(par2)
	par2 = Pyth.LineTo__Dict(par2, conf = 0)

	random.seed()
	conf = random.randint(0, 3)
	#conf = 0

	# load par1
	boneCoun = par1["boneCoun"]

	# TODO: inefficient
	use_Bone = []
	for a in range(len(tailDict)):
		use_Bone.append([False, -1])
		for b in range(boneCoun):
			inde = par1["bone." + Pyth.Pad_(b, 3)]
			if inde == a:
				use_Bone[a] = [True, b]

	
	for a in range(len(tailDict)):
		#for b in range(len(tailDict)):
		#for b in range(boneCoun):
			#indeStri = "bone." + Pyth.Pad_(b, 3)
			#if indeStri in par1:
			#inde = par1[indeStri]
		if use_Bone[a][0] == True:
			#if inde == a:
			x = par1["rota.x." + Pyth.Pad_(use_Bone[a][1], 3)]
			y = par1["rota.y." + Pyth.Pad_(use_Bone[a][1], 3)]
			z = par1["rota.z." + Pyth.Pad_(use_Bone[a][1], 3)]
			bpy.data.objects['Armature'].pose.bones[tailDict[inde]].rotation_euler = (x, y, z)
			bpy.data.objects['Armature'].pose.bones[tailDict[inde]].keyframe_insert("rotation_euler")
		else:
			# TODO: make this a function
			if conf == 0 or conf == 1:
				inde = a
				x = y = z = 0.0
				bpy.data.objects['Armature'].pose.bones[tailDict[inde]].rotation_euler = (x, y, z)
				bpy.data.objects['Armature'].pose.bones[tailDict[inde]].keyframe_insert("rotation_euler")

	# advance frames
	bpy.context.scene.frame_current = leng

	

	# load par2
	boneCoun = par2["boneCoun"]

	use_Bone = []
	for a in range(len(tailDict)):
		use_Bone.append([False, -1])
		for b in range(boneCoun):
			inde = par2["bone." + Pyth.Pad_(b, 3)]
			if inde == a:
				use_Bone[a] = [True, b]

	for a in range(len(tailDict)):
		#indeStri = "bone." + Pyth.Pad_(a, 3)
		#if indeStri in par2:
			#inde = par2[indeStri]
		if use_Bone[a][0] == True:
			x = par2["rota.x." + Pyth.Pad_(use_Bone[a][1], 3)]
			y = par2["rota.y." + Pyth.Pad_(use_Bone[a][1], 3)]
			z = par2["rota.z." + Pyth.Pad_(use_Bone[a][1], 3)]
			bpy.data.objects['Armature'].pose.bones[tailDict[inde]].rotation_euler = (x, y, z)
			bpy.data.objects['Armature'].pose.bones[tailDict[inde]].keyframe_insert("rotation_euler")
		else:
			if conf == 0 or conf == 2:
				inde = a
				x = y = z = 0.0
				bpy.data.objects['Armature'].pose.bones[tailDict[inde]].rotation_euler = (x, y, z)
				bpy.data.objects['Armature'].pose.bones[tailDict[inde]].keyframe_insert("rotation_euler")

	# TODO: 
	# do this with Gene
	# write iden
	exte = True
	paraDict = {}
	paraDict.update({"ran1": ran1})
	paraDict.update({"ran2": ran2})
	paraDict.update({"conf": conf})
	direOut = dire + "out_" + os.sep + pref + "_" + numb + "_para"
	Gene.ParaWrit(para = paraDict, dire = direOut, exte = exte)

	bpy.ops.wm.save_as_mainfile(filepath = dire + "out_" + os.sep + pref + "_" + numb + ".blend")

	# render
	#geneDire = "/home/christopher/Documents/prog/Gene/"
	#vide = geneDire + dire + "out_" + os.sep + pref + "_" + numb
	#syst = Blen.Batc(dire + "out_" + os.sep + pref + "_" + numb + ".blend")
	#syst += Blen.RendVide(vide, leng)
	#os.system(syst)

main()
