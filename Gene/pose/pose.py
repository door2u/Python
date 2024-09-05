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

	

	# pick one or several bones

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

	paraDict = {}
	random.seed()
	boneCoun = random.randint(1, 10)
	paraDict.update({"boneCoun": boneCoun})
	a = 0
	indeList = []
	for bone in range(boneCoun):
		random.seed()
		rand = random.randint(0, len(tailDict) - 1)
		indeList.append(rand)
		paraDict.update({"bone." + Blen.Pad_(a): rand})
		a += 1

	a = 0
	for inde in indeList:
		rota = bpy.data.objects['Armature'].pose.bones[tailDict[inde]].rotation_euler
		random.seed()
		rand = random.random()
		if rand < 0.5:
			random.seed()
			rota[0] = random.random() * 2.0 * math.pi
		random.seed()
		rand = random.random()
		if rand < 0.5:
			random.seed()
			rota[1] = random.random() * 2.0 * math.pi
		random.seed()
		rand = random.random()
		if rand < 0.5:
			random.seed()
			rota[2] = random.random() * 2.0 * math.pi
		bpy.data.objects['Armature'].pose.bones[tailDict[inde]].rotation_euler = rota
		paraDict.update({"rota.x." + Blen.Pad_(a): rota[0]})
		paraDict.update({"rota.y." + Blen.Pad_(a): rota[1]})
		paraDict.update({"rota.z." + Blen.Pad_(a): rota[2]})
		a += 1

	# TODO: make this a separate script and comment
	exte = True
	#exte = False
	#try:
	#	paraDict = para
	#	exte = True
	#	direOut = dire + "out_" + os.sep + "pose_" + numb + "_para"
	#except:
	#	paraDict = Gene.ParaInit("pose_para")
	#	direOut = ""

	
	direOut = dire + "out_" + os.sep + "pose_" + numb + "_para"

	#print(paraDict)

	Gene.ParaWrit(para = paraDict, dire = direOut, exte = exte)

main()
