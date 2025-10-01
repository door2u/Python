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
Node = Modu.Node

def Swap(val1, val2):
	temp = val1
	val1 = val2
	val2 = temp
	return val1, val2

def Inte(star, end_, prog):
	return star + prog * (end_ - star)

def RotaInte(stax, endx, stay, endy, staz, endz, prog, reve = False):
	import math
	import mathutils
	if reve:
		stax, endx = Swap(stax, endx)
		stay, endy = Swap(stay, endy)
		staz, endz = Swap(staz, endz)
	x = Inte(stax, endx, prog)
	y = Inte(stay, endy, prog)
	z = Inte(staz, endz, prog)
	eule = mathutils.Euler((math.radians(x), math.radians(y), math.radians(z)), 'XYZ')
	return eule.to_matrix()

def LocaInte(stax, endx, stay, endy, staz, endz, prog, reve = False):
	if reve:
		stax, endx = Swap(stax, endx)
		stay, endy = Swap(stay, endy)
		staz, endz = Swap(staz, endz)
	x = Inte(stax, endx, prog)
	y = Inte(stay, endy, prog)
	z = Inte(staz, endz, prog)
	return (x, y, z)

def Pose(pose, reve, inde, prog):
	import bge
	scen = bge.logic.getCurrentScene()
	a = 0
	for a in range(len(pose[inde])):
		obj1 = pose[inde][a][0]
		for b in range(len(pose[inde + 1])):
			obj2 = pose[inde + 1][b][0]
			if obj1 == obj2:
				rev_ = reve[inde][a]
				scen.objects[obj1].localOrientation = RotaInte(pose[inde][a][1][0], pose[inde + 1][b][1][0], pose[inde][a][1][1], pose[inde + 1][b][1][1], pose[inde][a][1][2], pose[inde + 1][b][1][2], prog, reve = rev_)
				break

def PoseAdd_(pose, inde, obje, valu, offs):
	pose[inde].append([obje, (valu[inde][len(pose[inde])][0] + offs[inde][len(pose[inde])][0], valu[inde][len(pose[inde])][1] + offs[inde][len(pose[inde])][1], valu[inde][len(pose[inde])][2] + offs[inde][len(pose[inde])][2])])
	return pose

def AnimPhas(pose, time, pare, reve, phas, inde, anim, end_):
	import bge
	# TODO
	import mathutils
	scen = bge.logic.getCurrentScene()
	time = time[inde]
	if anim <= time:
		Pose(pose, reve, inde, anim / time)
	else:
		if pare[inde] != []:
			orie = scen.objects[pare[inde][0]].worldOrientation
			scen.objects[pare[inde][0]].setParent(pare[inde][1])
			scen.objects[pare[inde][0]].worldOrientation = orie
		# set rotation to final position
		Pose(pose, reve, inde, 1.0)
		anim = 0.0
		inde += 1
		if phas == end_:
			phas = -1
			#bge.logic.KX_GAME_QUIT
		else:
			phas += 1
	return phas, inde, anim

def main():

	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner

	name = "matt"

	# TODO:
	# need to animate multiple actions. (left arm / right arm). make a list to add poselist to
	# then make an action list to add actions to

	animList = []

	# ready arrow
	key_Coun = 2
	valu = []
	time = []
	pose = []
	pare = []
	reve = []
	for a in range(key_Coun):
		valu.append([])
		time.append(0.0)
		pose.append([])
		pare.append([])
		reve.append([])

	time[0] = 1.0
	inde = 0
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	inde += 1
	valu[inde].append((0.0, -136.0, 0.0))
	valu[inde].append((0.0, -121.8, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))

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

	inde = 0
	pose = PoseAdd_(pose, inde, name + "." + "shou.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.r", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.r", valu, offsList)
	
	for a in range(key_Coun):
		for b in range(len(valu[a])):
			reve[a].append(False)

	end_ = 40 + 0

	animList.append([pose, time, pare, reve, end_])

	################

	# TODO:
	# switch side
	# attach shield to hip or shoulder or something
	# rotate bow out of sword

	# ready bow
	key_Coun = 6

	valu = []
	time = []
	pose = []
	pare = []
	reve = []
	for a in range(key_Coun):
		valu.append([])
		time.append(0.0)
		pose.append([])
		pare.append([])
		reve.append([])

	#time[0] = 0.05
	#time[1] = 0.05
	#time[2] = 0.1
	#time[3] = 0.15
	#time[4] = 0.2

	time[0] = 0.05
	time[1] = 1.0
	time[2] = 1.0
	time[3] = 1.0
	time[4] = 1.0

	inde = 0
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	inde += 1
	valu[inde].append((17.5, -15.0, -4.0))
	valu[inde].append((-20.0, -92.0, -28.5))
	valu[inde].append((-31.2, 0.0, -6.3))
	inde += 1
	valu[inde].append((0.0, -15.0, 0.0))
	valu[inde].append((-45.0, -134.5, -6.0))
	valu[inde].append((15.142509031295777, 77.83781256675721, -45.94693546295166))
	#valu[inde].append((-96.98304539310416, 26.86925150445699, -60.068446742064964))
	valu[inde].append((-23.6, -1.5, 0.0))
	inde += 1
	valu[3].append((12.767421627044676, -19.107391473278405, -13.359359169006346))
	valu[3].append((12.20978593826294, -134.93702101707458, 0.5044281005859377))
	valu[3].append((19.116707611083985, 73.08039083480836, -64.33842449188232))
	#valu[3].append((-102.76148610698661, 39.45585228494405, -61.454979525573265))
	valu[inde].append((-23.6, -1.5, 0.0))
	inde += 1
	valu[inde].append((13.9, -45.0, -14.2))
	valu[inde].append((0.0, -90.0, 16.8))
	valu[inde].append((80.0, 35.0, 30.0))
	valu[inde].append((-80.0, 60.0, -120.0))
	inde += 1
	valu[inde].append((30.0, -40.5, -14.2))
	valu[inde].append((0.0, -40.0, 0.0))
	valu[inde].append((20.0, 0.0, 40.0))
	valu[inde].append((-80.0, 40.0 + 360.0, -100.0))

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

	inde = 0
	pose = PoseAdd_(pose, inde, name + "." + "shou.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.l", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.l", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "bow_", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "bow_", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "bow_", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "bow_", valu, offsList)

	pare[0] = [owne.name + "." + "bow_", owne.name + "." + "wris.l"]

	for a in range(key_Coun):
		for b in range(len(valu[a])):
			reve[a].append(False)

	#end_ = 30 + 4
	end_ = 30 + 1

	animList.append([pose, time, pare, reve, end_])

	################

	# swing sword
	key_Coun = 4

	valu = []
	time = []
	pose = []
	pare = []
	reve = []
	for a in range(key_Coun):
		valu.append([])
		time.append(0.0)
		pose.append([])
		pare.append([])
		reve.append([])

	time[0] = 0.2
	time[1] = 0.3
	time[2] = 0.4
	inde = 0
	# ready pose
	valu[inde].append((0.0, -84.1, -57.0))
	valu[inde].append((99.4, -8.1, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	inde += 1
	# pull back
	valu[inde].append((-52.6, -139.0, -59.0))
	valu[inde].append((34.0, 13.7, -2.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, -10.0))
	inde += 1
	# swing
	valu[inde].append((-52.6, -90.0, 80.0))
	valu[inde].append((55.0, 15.4, 2.0))
	valu[inde].append((0.0, 0.0, -90.0))
	valu[inde].append((0.0, -70.0, 0.0))
	valu[inde].append((0.0, 60.0, 0.0))
	valu[inde].append((0.0, 60.0, 0.0))
	valu[inde].append((0.0, 10.0, 30.0))
	#bodyHeig = owne["bodyHeig"]
	#scen.objects[owne.name + "." + "body"].localPosition = LocaInte(0.0, 0.0, 0.0, 0.0, bodyHeig, bodyHeig - 0.3, anim / time)
	inde += 1
	# return to ready pose
	valu[inde].append((0.0, -84.1, -57.0))
	valu[inde].append((99.4, -8.1, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))

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

	inde = 0
	pose = PoseAdd_(pose, inde, name + "." + "shou.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "body", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "hip_.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "knee.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "knee.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "body", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "hip_.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "knee.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "knee.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "body", valu, offsList)
	#pose = PoseAdd_(pose, inde, name + "." + "body", valu, offsList)
	inde += 1
	pose = PoseAdd_(pose, inde, name + "." + "shou.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "elbo.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "wris.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "hip_.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "knee.r", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "knee.l", valu, offsList)
	pose = PoseAdd_(pose, inde, name + "." + "body", valu, offsList)

	for a in range(len(reve[inde])):
		reve[3][a] = True

	for a in range(key_Coun):
		for b in range(len(valu[a])):
			reve[a].append(False)

	end_ = 20 + 2

	animList.append([pose, time, pare, reve, end_])

	################

	phas = owne["animPhas"]
	anim = owne["animTime"]
	# TODO
	inde = owne["pose"]

	# draw arrow - 40
	#animInde = 0
	# draw bow - 30
	animInde = 1
	# swing sword - 20
	#animInde = 2

	set_Phas = owne["set_Phas"]
	if set_Phas:
		owne["set_Phas"] = False
		if animInde == 0:
			phas = 40
		if animInde == 1:
			phas = 30
		if animInde == 2:
			phas = 20

	if phas != -1:

		# swing sword
		# TODO
		if phas == 20 and anim == 0.01666666753590107:
			scen.objects[name + ".swor"].setParent(name + ".wris.r")
			eule = mathutils.Euler((0.0, -math.pi / 2.0, 0.0), 'XYZ')
			scen.objects[name + ".swor"].worldOrientation = eule.to_matrix()
			posi = scen.objects[name + ".wris.r"].worldPosition
			scen.objects[name + ".swor"].worldPosition = posi

		#phas, inde, anim = AnimPhas(pose, time, pare, reve, phas, inde, anim, end_)
		phas, inde, anim = AnimPhas(animList[animInde][0], animList[animInde][1], animList[animInde][2], animList[animInde][3], phas, inde, anim, animList[animInde][4])

	owne["animPhas"] = phas
	owne["animTime"] = anim
	owne["pose"] = inde

main()

