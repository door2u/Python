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

	# create 17 * 3 random values
	Blen.Sele("matt")
	mini = -10.0
	maxi = 10.0
	#mini = 0.0
	#maxi = 0.0
	#coun = 17

	paraDict = {}

	offsList = []

	key_Coun = 4
	bow_Anim = []
	for a in range(key_Coun):
		bow_Anim.append([])
	inde = 0
	bow_Anim[inde].append((0.0, -84.1, -57.0))
	bow_Anim[inde].append((99.4,  -8.1,  0.0))
	bow_Anim[inde].append((0.0,  0.0,  0.0))
	inde += 1
	bow_Anim[inde].append((-52.6, -139.0, -59.0))
	bow_Anim[inde].append((34.0,  13.7, -2.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0,  0.0,  -10.0))
	inde += 1
	bow_Anim[inde].append((-52.6, -90.0, 80.0))
	bow_Anim[inde].append((55.0, 15.4, 2.0))
	bow_Anim[inde].append((0.0, 0.0, -90.0))
	bow_Anim[inde].append((0.0, -70.0, 0.0))
	bow_Anim[inde].append((0.0, 60.0, 0.0))
	bow_Anim[inde].append((0.0, 60.0, 0.0))
	bow_Anim[inde].append((0.0, 10.0, 30.0))
	inde += 1
	bow_Anim[inde].append((0.0, -84.1, -57.0))
	bow_Anim[inde].append((99.4,  -8.1,  0.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0, 0.0, 0.0))
	bow_Anim[inde].append((0.0,  0.0,  0.0))
	for a in range(len(bow_Anim)):
		for b in range(len(bow_Anim[a])):
			x = Math.RandRang(mini, maxi)
			y = Math.RandRang(mini, maxi)
			z = Math.RandRang(mini, maxi)
			BlenGame.Prop(propName = "offs." + str(a) + "." + str(b) + ".x", propType = 'FLOAT', propValu = x)
			BlenGame.Prop(propName = "offs." + str(a) + "." + str(b) + ".y", propType = 'FLOAT', propValu = y)
			BlenGame.Prop(propName = "offs." + str(a) + "." + str(b) + ".z", propType = 'FLOAT', propValu = z)
			paraDict.update({"offs." + str(a) + "." + str(b) + ".x" : x})
			paraDict.update({"offs." + str(a) + "." + str(b) + ".y" : y})
			paraDict.update({"offs." + str(a) + "." + str(b) + ".z" : z})

	"""
	for a in range(coun):
		x = Math.RandRang(mini, maxi)
		y = Math.RandRang(mini, maxi)
		z = Math.RandRang(mini, maxi)
		offsList.append((x, y, z))
		variName = "offs." + str(a) + ".x"
		if (variName in bpy.context.object.game.properties) == False:
			BlenGame.Prop(propName = variName, propType = 'FLOAT', propValu = x)
		else:
			BlenGame.PropSet_(propName = variName, propValu = x)
		variName = "offs." + str(a) + ".y"
		if (variName in bpy.context.object.game.properties) == False:
			BlenGame.Prop(propName = variName, propType = 'FLOAT', propValu = y)
		else:
			BlenGame.PropSet_(propName = variName, propValu = y)
		variName = "offs." + str(a) + ".z"
		if (variName in bpy.context.object.game.properties) == False:
			BlenGame.Prop(propName = variName, propType = 'FLOAT', propValu = z)
		else:
			BlenGame.PropSet_(propName = variName, propValu = z)
	"""

	#direOut = dire + "out_" + os.sep + pref + "_" + numb + "_para"
	direOut = dire + "out_" + os.sep + "anim" + "_" + numb + "_para"
	Gene.ParaWrit(para = paraDict, dire = direOut, exte = True)

	bpy.ops.wm.save_as_mainfile(filepath = dire + "out_" + os.sep + "anim" + "_" + numb + ".blend")

main()
