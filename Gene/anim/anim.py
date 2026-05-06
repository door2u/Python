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

def PoseAdd_(pose, inde, obje, valu, offs):
	pose[inde].append([obje[inde][len(pose[inde])], (valu[inde][len(pose[inde])][0] + offs[inde][len(pose[inde])][0], valu[inde][len(pose[inde])][1] + offs[inde][len(pose[inde])][1], valu[inde][len(pose[inde])][2] + offs[inde][len(pose[inde])][2])])
	return pose

def main():

	import math
	import bpy
	import random

	mini = -10.0
	maxi = 10.0
	#mini = 0.0
	#maxi = 0.0
	#coun = 17

	paraDict = {}

	offsList = []

	# TODO: make a file that everything reads

	blen = True
	#try:
	#import bpy
	#except:
	#	blen = False
	#	import bge
	#	import mathutils
	#	cont = bge.logic.getCurrentController()
	#	scen = bge.logic.getCurrentScene()
	#	owne = cont.owner
	#import math

	# TODO:
	# specify a relative local position change
	# bge.logic.KX_GAME_QUIT

	name = "matt"
	Blen.Sele(name)
	animList = []
	fps_ = 60

	################

	# ready arrow
	key_Coun = 2
	valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl = AnimInit(key_Coun)
	time[0] = (1.0 * fps_)

	# star
	inde = 0
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, -136.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((0.0, -121.8, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)

	pose, reve = AnimFina(key_Coun, valu, pose, bone, reve)
	animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

	################

	# swing sword
	key_Coun = 4
	valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl = AnimInit(key_Coun)

	time[0] = 0.2
	time[1] = 0.3
	time[2] = 0.4

	inde = 0
	# ready pose
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "body")
	valu[inde].append((0.0, -84.1, -57.0))
	valu[inde].append((99.4, -8.1, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	inde += 1
	# pull back
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "hip_.r")
	bone[inde].append(name + "." + "knee.r")
	bone[inde].append(name + "." + "knee.l")
	bone[inde].append(name + "." + "body")
	valu[inde].append((-52.6, -139.0, -59.0))
	valu[inde].append((34.0, 13.7, -2.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, -10.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	inde += 1
	# swing
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "hip_.r")
	bone[inde].append(name + "." + "knee.r")
	bone[inde].append(name + "." + "knee.l")
	bone[inde].append(name + "." + "body")
	valu[inde].append((-52.6, -90.0, 80.0))
	valu[inde].append((55.0, 15.4, 2.0))
	valu[inde].append((0.0, 0.0, -90.0))
	valu[inde].append((0.0, -70.0, 0.0))
	valu[inde].append((0.0, 60.0, 0.0))
	valu[inde].append((0.0, 60.0, 0.0))
	valu[inde].append((0.0, 10.0, 30.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	#bodyHeig = owne["bodyHeig"]
	#scen.objects[owne.name + "." + "body"].localPosition = LocaInte(0.0, 0.0, 0.0, 0.0, bodyHeig, bodyHeig - 0.3, anim / time)
	inde += 1
	# return to ready pose
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "hip_.r")
	bone[inde].append(name + "." + "knee.r")
	bone[inde].append(name + "." + "knee.l")
	bone[inde].append(name + "." + "body")
	valu[inde].append((0.0, -84.1, -57.0))
	valu[inde].append((99.4, -8.1, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)

	pose, reve = AnimFina(key_Coun, valu, pose, bone, reve)
	for a in range(len(reve[inde])):
		reve[3][a] = True
	animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

	################

	# ready sword

	# TODO: put away
	#valu[inde].append((0.11219, -0.155, 1.45067))

	key_Coun = 3
	valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl = AnimInit(key_Coun)

	time[0] = 0.3
	time[1] = 0.3
	#pare[0] = [owne.name + "." + "swor", owne.name + "." + "wris.r"]
	pare[0] = [name + "." + "swor", name + "." + "wris.r"]

	inde = 0
	# start
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	inde += 1
	# hand to handle
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "swor")
	bone[inde].append(name + "." + "swor")
	valu[inde].append((0.0, 39.0, 0.0))
	valu[inde].append((0.0, -157.3, 16.3))
	valu[inde].append((0.0, 45.7, 0.0))
	valu[inde].append((-3.3, 25.3, 8.7))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(False)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	inde += 1
	# raise sword
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "swor")
	bone[inde].append(name + "." + "swor")
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, -90.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, -90.0, 0.0))
	valu[inde].append((0.07, 0.15, -0.05))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(False)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)

	pose, reve = AnimFina(key_Coun, valu, pose, bone, reve)
	animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

	################

	# TODO:
	# switch arrow 0 and 4. make a layer 2 object
	# cuts off fingers

	# TODO
	# keys need to have a beginning and an end, otherwise cant switch from relative to absolute. or need to store current rotation at the end of a pose

	# ready bow
	key_Coun = 11
	valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl = AnimInit(key_Coun)

	# TODO: frame count changes outcome
	time[0] = round(0.2 * fps_)
	time[1] = round(0.2 * fps_)
	time[2] = round(0.2 * fps_)
	time[3] = round(0.3 * fps_)
	time[4] = round(0.3 * fps_)
	time[5] = round(0.1 * fps_)
	time[6] = round(0.1 * fps_)
	time[7] = round(0.1 * fps_)
	time[8] = round(0.3 * fps_)
	time[9] = round(0.3 * fps_)
	time[10] = round(0.1 * fps_)

	pare[0] = [name + "." + "bow_", name + "." + "wris.r"]
	pare[4] = [name + "." + "bow_", name + "." + "wris.l"]
	if blen:
		dupl[5] = [name + "." + "arro.000", name + "." + "arro.011"]
		pare[5] = [name + "." + "arro.011", name + "." + "wris.r"]
	else:
		dupl[5] = [name + "." + "arro.000", name + "." + "arro.010"]
		pare[5] = [name + "." + "arro.010", name + "." + "wris.r"]

	# 0 - start
	inde = 0
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	# 1 - hand to handle
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, 0.0, 20.0))
	valu[inde].append((0.0, -78.5, 0.0))
	valu[inde].append((67.5, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(False)
	# 2 - clear head
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, -34.0, 20.0))
	valu[inde].append((0.0, -109.8, 0.0))
	valu[inde].append((68.4, 60.3, -3.4))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(False)
	# 3 - clear head
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, -34.0, 20.0))
	valu[inde].append((-45.0, -115.0, 13.0))
	valu[inde].append((68.4, 75.0, -3.4))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(False)
	# 4 - clear sword
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	bone[inde].append(name + "." + "elbo.r")
	bone[inde].append(name + "." + "wris.r")
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, 36.0, 20.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((87.0, 75.0, -32.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(False)
	# 5 - pass to other hand
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, -48.0, 20.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((-10.5, -20.0, 13.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((68.4, -22.3, -3.4))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((20.0, 20.0, -20.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	# 6 - hand to arrow
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, -136.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((0.0, -121.8, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	# 7 - draw arrow
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, -164.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((0.0, -26.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, -63.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	bone[inde].append(name + "." + "quiv")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	if blen:
		bone[inde].append(name + "." + "arro.011")
	else:
		bone[inde].append(owne["inde"])
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	# 8 - clear quiver
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, -90.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((0.0, -26.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, -63.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	bone[inde].append(name + "." + "quiv")
	valu[inde].append((0.0, 60.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	if blen:
		bone[inde].append(name + "." + "arro.011")
	else:
		bone[inde].append(owne["inde"])
	valu[inde].append((5.0, 8.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	# 9 - arrow to bow
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, -8.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "shou.l")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((0.0, -90.0, 24.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.l")
	valu[inde].append((0.0, -90.0, -23.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((0.0, 23.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	# TODO: should return this to start
	# TODO: should be timed for gravity
	bone[inde].append(name + "." + "quiv")
	valu[inde].append((0.0, -60.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	if blen:
		bone[inde].append(name + "." + "arro.011")
	else:
		bone[inde].append(owne["inde"])
	valu[inde].append((70.0, 20.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	# 10 - extend bow
	inde += 1
	bone[inde].append(name + "." + "shou.r")
	valu[inde].append((0.0, -50.0, -15.7))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "shou.l")
	valu[inde].append((0.0, -45.0, -13.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.r")
	valu[inde].append((100.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.l")
	valu[inde].append((0.0, -45.0, -30.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.r")
	valu[inde].append((-84.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, 40.0, 20.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "bow_")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	bone[inde].append(name + "." + "quiv")
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)
	if blen:
		bone[inde].append(name + "." + "arro.011")
	else:
		bone[inde].append(owne["inde"])
	valu[inde].append((0.0, -15.0, 0.0))
	typ_[inde].append(True)
	abso[inde].append(False)

	pose, reve = AnimFina(key_Coun, valu, pose, bone, reve)
	animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

	################

	# clear sword for bow

	key_Coun = 6
	valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl = AnimInit(key_Coun)
	time[0] = round(0.2 * fps_)
	time[1] = round(0.2 * fps_)
	time[2] = round(0.2 * fps_)
	time[3] = round(0.3 * fps_)
	time[4] = round(0.3 * fps_)
	time[5] = round(0.1 * fps_)
	pare[1] = [name + "." + "swor", name + "." + "wris.l"]
	pare[3] = [name + "." + "swor", name + "." + "body"]

	# start
	inde = 0
	bone[inde].append(name + "." + "shou.l")
	bone[inde].append(name + "." + "elbo.l")
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	# start
	inde += 1
	bone[inde].append(name + "." + "shou.l")
	bone[inde].append(name + "." + "elbo.l")
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	# hand to handle
	inde += 1
	bone[inde].append(name + "." + "shou.l")
	bone[inde].append(name + "." + "elbo.l")
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, -59.0, -16.0))
	valu[inde].append((-85.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, -16.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	# raise sword
	inde += 1
	bone[inde].append(name + "." + "shou.l")
	valu[inde].append((0.0, -140.0, -16.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "elbo.l")
	valu[inde].append((-30.0, 0.0, 60.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, 76.0, -10.0))
	typ_[inde].append(True)
	abso[inde].append(True)
	# hand to handle
	inde += 1
	bone[inde].append(name + "." + "shou.l")
	bone[inde].append(name + "." + "elbo.l")
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, -59.0, -16.0))
	valu[inde].append((-85.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, -16.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	# start
	inde += 1
	bone[inde].append(name + "." + "shou.l")
	bone[inde].append(name + "." + "elbo.l")
	bone[inde].append(name + "." + "wris.l")
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, -90.0, -23.0))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)

	pose, reve = AnimFina(key_Coun, valu, pose, bone, reve)
	animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

	################

	# draw arrow
	#star = 0
	#end_ = 0
	# swing sword
	#star = 1
	#end_ = 1
	# ready sword
	#star = 2
	#end_ = 2
	# draw bow
	#star = 3
	#end_ = 3
	# clear sword for bow
	#star = 4
	#end_ = 4

	star = 3
	end_ = 4
		
	# TODO: only need length of value arrays
	for c in range(star, end_ + 1):
		ind_ = c - star
		for a in range(len(animList[c][0])):
			for b in range(len(animList[c][0][a])):
				x = Math.RandRang(mini, maxi)
				y = Math.RandRang(mini, maxi)
				z = Math.RandRang(mini, maxi)
				BlenGame.Prop(propName = "offs." + str(ind_) + "." + str(a) + "." + str(b) + ".x", propType = 'FLOAT', propValu = x)
				BlenGame.Prop(propName = "offs." + str(ind_) + "." + str(a) + "." + str(b) + ".y", propType = 'FLOAT', propValu = y)
				BlenGame.Prop(propName = "offs." + str(ind_) + "." + str(a) + "." + str(b) + ".z", propType = 'FLOAT', propValu = z)
				paraDict.update({"offs." + str(ind_) + "." + str(a) + "." + str(b) + ".x" : x})
				paraDict.update({"offs." + str(ind_) + "." + str(a) + "." + str(b) + ".y" : y})
				paraDict.update({"offs." + str(ind_) + "." + str(a) + "." + str(b) + ".z" : z})

	direOut = dire + "out_" + os.sep + "anim" + "_" + numb + "_para"
	Gene.ParaWrit(para = paraDict, dire = direOut, exte = True)

	bpy.ops.wm.save_as_mainfile(filepath = dire + "out_" + os.sep + "anim" + "_" + numb + ".blend")

def AnimFina(key_Coun, valu, pose, bone, reve):
	offsList = []
	try:
		for a in range(len(valu)):
			offs = []
			for b in range(len(valu[a])):
				x = owne["offs." + str(a) + "." + str(b) + ".x"]
				y = owne["offs." + str(a) + "." + str(b) + ".y"]
				z = owne["offs." + str(a) + "." + str(b) + ".z"]
				offs.append((x, y, z))
			offsList.append(offs)
	except:
		for a in range(len(valu)):
			offs = []
			for b in range(len(valu[a])):
				offs.append((0.0, 0.0, 0.0))
			offsList.append(offs)
	for a in range(key_Coun):
		for b in range(len(valu[a])):
			reve[a].append(False)
			pose = PoseAdd_(pose, a, bone, valu, offsList)
	return pose, reve

def AnimInit(key_Coun):
	valu = []
	time = []
	pose = []
	pare = []
	reve = []
	typ_ = []
	bone = []
	abso = []
	dupl = []
	end_ = key_Coun - 2
	for a in range(key_Coun):
		valu.append([])
		time.append(0.0)
		pose.append([])
		pare.append([])
		reve.append([])
		typ_.append([])
		bone.append([])
		abso.append([])
		dupl.append([])
	return valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl

main()
