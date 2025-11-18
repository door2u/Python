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

def RotaInte(stax, endx, stay, endy, staz, endz, prog, blen, reve = False):
	import math
	if blen == False:
		import mathutils
	if reve:
		stax, endx = Swap(stax, endx)
		stay, endy = Swap(stay, endy)
		staz, endz = Swap(staz, endz)
	x = Inte(stax, endx, prog)
	y = Inte(stay, endy, prog)
	z = Inte(staz, endz, prog)
	if blen:
		# TODO: r or d
		eule = (math.radians(x), math.radians(y), math.radians(z))
	else:
		eule = mathutils.Euler((math.radians(x), math.radians(y), math.radians(z)), 'XYZ')
		eule = eule.to_matrix()
	return eule

def LocaInte(stax, endx, stay, endy, staz, endz, prog, reve = False):
	if reve:
		stax, endx = Swap(stax, endx)
		stay, endy = Swap(stay, endy)
		staz, endz = Swap(staz, endz)
	x = Inte(stax, endx, prog)
	y = Inte(stay, endy, prog)
	z = Inte(staz, endz, prog)
	return (x, y, z)

def Pose(pose, reve, inde, anim, time, typ_, abso, blen):
	if blen:
		import bpy
	else:
		import bge
		scen = bge.logic.getCurrentScene()
	import math
	for a in range(len(pose[inde])):
		obj1 = pose[inde][a][0]
		typ1 = typ_[inde][a]
		abs1 = abso[inde][a]
		for b in range(len(pose[inde + 1])):
			obj2 = pose[inde + 1][b][0]
			typ2 = typ_[inde + 1][b]
			abs2 = abso[inde + 1][b]
			if obj1 == obj2 and typ1 == typ2:
				rev_ = reve[inde][a]
				if typ1:
					if abs2:
						if blen:
							#print(obj1)
							bpy.data.objects[obj1].rotation_euler = RotaInte(pose[inde][a][1][0], pose[inde + 1][b][1][0], pose[inde][a][1][1], pose[inde + 1][b][1][1], pose[inde][a][1][2], pose[inde + 1][b][1][2], anim / time, blen, reve = rev_)
						else:
							scen.objects[obj1].localOrientation = RotaInte(pose[inde][a][1][0], pose[inde + 1][b][1][0], pose[inde][a][1][1], pose[inde + 1][b][1][1], pose[inde][a][1][2], pose[inde + 1][b][1][2], anim / time, blen, reve = rev_)
					# TODO: location equivalent
					else:
						if blen:
							# TODO
							bpy.ops.object.select_all(action = 'DESELECT')
							#print(anim, time, obj1, a, b, math.radians(pose[inde + 1][b][1][0]) / time, math.radians(pose[inde + 1][b][1][1]) / time, math.radians(pose[inde + 1][b][1][2]) / time)
							bpy.data.objects[obj1].select = True
							bpy.ops.transform.rotate(value = math.radians(pose[inde + 1][b][1][0]) / time, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation = 'LOCAL')
							bpy.ops.transform.rotate(value = math.radians(pose[inde + 1][b][1][1]) / time, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation = 'LOCAL')
							bpy.ops.transform.rotate(value = math.radians(pose[inde + 1][b][1][2]) / time, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation = 'LOCAL')
							bpy.data.objects[obj1].select = False
						else:
							scen.objects[obj1].applyRotation((math.radians(pose[inde + 1][b][1][0]) / time, math.radians(pose[inde + 1][b][1][1]) / time, math.radians(pose[inde + 1][b][1][2]) / time), True)
				else:
					if blen:
						bpy.data.objects[obj1].location = LocaInte(pose[inde][a][1][0], pose[inde + 1][b][1][0], pose[inde][a][1][1], pose[inde + 1][b][1][1], pose[inde][a][1][2], pose[inde + 1][b][1][2], anim / time, blen, reve = rev_)
					else:
						scen.objects[obj1].localPosition = LocaInte(pose[inde][a][1][0], pose[inde + 1][b][1][0], pose[inde][a][1][1], pose[inde + 1][b][1][1], pose[inde][a][1][2], pose[inde + 1][b][1][2], anim / time, blen, reve = rev_)
				break

def PoseAdd_(pose, inde, obje, valu, offs):
	pose[inde].append([obje[inde][len(pose[inde])], (valu[inde][len(pose[inde])][0] + offs[inde][len(pose[inde])][0], valu[inde][len(pose[inde])][1] + offs[inde][len(pose[inde])][1], valu[inde][len(pose[inde])][2] + offs[inde][len(pose[inde])][2])])
	return pose

def AnimPhas(pose, time, pare, reve, phas, inde, anim, end_, typ_, abso, dupl, blen):
	if blen:
		import bpy
	else:
		import bge
		import mathutils
		scen = bge.logic.getCurrentScene()
	import math
	time = time[inde]
	# TODO: check for off-by-one gaps
	#if anim <= time:
	#print(anim, time)
	if anim >= 0 and anim < time - 2:
		#print(anim, time)
		#Pose(pose, reve, inde, anim, time, typ_, abso, blen)
		Pose(pose, reve, inde, anim, time - 1, typ_, abso, blen)
		anim += 1
	else:
		# lock relative rotations in
		for a in range(len(pose[inde])):
			if inde != 0 and typ_[inde][a] and abso[inde][a] == False:
				for b in range(len(pose[inde - 1])):
					if pose[inde][a][0] == pose[inde - 1][b][0]:
						pose[inde][a][1] = (pose[inde - 1][b][1][0] + pose[inde][a][1][0], pose[inde - 1][b][1][1] + pose[inde][a][1][1], pose[inde - 1][b][1][2] + pose[inde][a][1][2])
						abso[inde][a] = True
		# set to final position
		Pose(pose, reve, inde, time - 1, time - 1, typ_, abso, blen)
		# set last rotation to absolute, so new rotations are always relative to an absolute rotation
		# TODO: test. maybe make a function
		for a in range(len(pose[inde])):
			if typ_[inde][a]:
				if blen:
					orie = bpy.data.objects[pose[inde][a][0]].rotation_euler
				else:
					orie = scen.objects[pose[inde][a][0]].worldOrientation
					orie = orie.to_euler()
				orie = (math.degrees(orie[0]), math.degrees(orie[1]), math.degrees(orie[2]))
				pose[inde][a][1] = orie
		#Pose(pose, reve, inde, time - 1, time - 1, typ_, abso, blen)
		if dupl[inde] != []:
			if blen:
				posi = bpy.data.objects[dupl[inde][0]].location
				orie = bpy.data.objects[dupl[inde][0]].rotation_euler
				# TODO
				bpy.ops.object.select_all(action = 'DESELECT')
				bpy.data.objects[dupl[inde][0]].select = True
				bpy.context.scene.objects.active = bpy.data.objects[dupl[inde][0]]
				bpy.ops.object.duplicate_move()
				bpy.data.objects[dupl[inde][0]].select = False
				bpy.data.objects[dupl[inde][1]].select = False
				# TODO?
				bpy.context.scene.objects.active = None
				bpy.data.objects[dupl[inde][1]].location = posi
				bpy.data.objects[dupl[inde][1]].rotation_euler = orie
			else:
				posi = scen.objects[dupl[inde][0]].worldPosition
				orie = scen.objects[dupl[inde][0]].worldOrientation
				obje = scen.addObject(dupl[inde][1], dupl[inde][1])
				# TODO: get character name
				# TODO: do this in temp.py
				scen.objects["matt"]["inde"] = len(scen.objects) - 1
				scen.objects[dupl[inde][1]].worldPosition = posi
				scen.objects[dupl[inde][1]].worldOrientation = orie
		if pare[inde] != []:
			# TODO: scale
			if blen:
				posi = bpy.data.objects[pare[inde][0]].location
				orie = bpy.data.objects[pare[inde][0]].rotation_euler
				# TODO
				bpy.ops.object.select_all(action = 'DESELECT')
				bpy.context.scene.objects.active = bpy.data.objects[pare[inde][1]]
				bpy.data.objects[pare[inde][0]].select = True
				bpy.ops.object.parent_set(keep_transform = True)
				bpy.data.objects[pare[inde][0]].location = posi
				bpy.data.objects[pare[inde][0]].rotation_euler = orie
				bpy.context.scene.objects.active = None
				bpy.data.objects[pare[inde][0]].select = False
			else:
				posi = scen.objects[pare[inde][0]].worldPosition
				orie = scen.objects[pare[inde][0]].worldOrientation
				scen.objects[pare[inde][0]].setParent(pare[inde][1])
				scen.objects[pare[inde][0]].worldPosition = posi
				scen.objects[pare[inde][0]].worldOrientation = orie
		inde += 1
		# TODO: maybe dont need phas
		if phas == end_:
			anim = -1
		else:
			"""
			# TODO: test. maybe make a function
			for a in range(len(pose[inde])):
				if typ_[inde][a]
					if abso[inde][a]:
						for b in range(len(pose[inde - 1])):
							if abso[inde - 1][b] == False and pose[inde][a][0] == pose[inde - 1][b][0]:
								if blen:
									orie = bpy.data.objects[pose[inde][a][0]].rotation_euler
								else:
									orie = scen.objects[pose[inde][a][0]].worldOrientation
									orie = orie.to_euler()
								orie = (math.degrees(orie[0]), math.degrees(orie[1]), math.degrees(orie[2]))
								pose[inde - 1][b][1] = orie
					else:
			"""
			phas += 1
			anim = 0
	return phas, inde, anim

def Bone(name = "", valu = (0.0, 0.0, 0.0), typ_ = True, abso = True, mirr = -1):
	retu = {}
	retu.update({"name" : name})
	retu.update({"valu" : valu})
	retu.update({"typ_" : typ_})
	retu.update({"abso" : abso})
	retu.update({"mirr" : mirr})
	return retu

def AppeFromBone(boneDict, inde, bone, valu, typ_, abso, mirr):
	bone[inde].append(boneDict["name"])
	valu[inde].append(boneDict["valu"])
	typ_[inde].append(boneDict["typ_"])
	abso[inde].append(boneDict["abso"])
	mirr[inde].append(boneDict["mirr"])
	return bone, valu, typ_, abso, mirr

def BoneList(pose, typ_, abso, inde):
	boneList = []
	for a in range(len(pose[inde])):
		boneList.append(Bone(name = pose[inde][a][0], valu = pose[inde][a][1], typ_ = typ_[inde][a], abso = abso[inde][a], mirr = False))
	return boneList

def main():

	continu_ = True
	while continu_:

		continu_ = False

		blen = True
		try:
			import bpy
		except:
			blen = False
			import bge
			import mathutils
			cont = bge.logic.getCurrentController()
			scen = bge.logic.getCurrentScene()
			owne = cont.owner
		import math

		# TODO:
		# whats the best way to organize
		# changing numbers of frames of an animation changes the outcome for relative rotations
		# cant change from absolute to relative. need to store end of last rotation
		# are interpolations between poses correct? maybe cross beginning and end to get an axis and use quaternion
		# specify a relative local position change
		# bge.logic.KX_GAME_QUIT

		name = "matt"
		animList = []
		fps_ = 60

		################

		# ready arrow
		key_Coun = 2
		valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr = AnimInit(key_Coun)
		time[0] = (1.0 * fps_)

		# star
		inde = 0
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		inde += 1
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, -136.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((0.0, -121.8, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)

		pose, reve = AnimFina(key_Coun, valu, pose, bone, reve, -1, mirr)
		animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

		################

		# swing sword
		key_Coun = 4
		valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr = AnimInit(key_Coun)

		time[0] = 0.2
		time[1] = 0.3
		time[2] = 0.4

		inde = 0
		# ready pose
		# TODO: whats the best way for this data to be stored for all environments
		bone, valu, typ_, abso, mirr = AppeFromBone(Bone(name = name + "." + "shou.r", valu = (0.0, -84.1, -57.0)), inde, bone, valu, typ_, abso, mirr)
		bone, valu, typ_, abso, mirr = AppeFromBone(Bone(name = name + "." + "elbo.r", valu = (99.4, -8.1, 0.0)), inde, bone, valu, typ_, abso, mirr)
		bone, valu, typ_, abso, mirr = AppeFromBone(Bone(name = name + "." + "body"), inde, bone, valu, typ_, abso, mirr)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)

		pose, reve = AnimFina(key_Coun, valu, pose, bone, reve, -1, mirr)
		for a in range(len(reve[inde])):
			reve[3][a] = True
		animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

		################

		# ready sword

		# TODO: put away
		#valu[inde].append((0.11219, -0.155, 1.45067))

		key_Coun = 3
		valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr = AnimInit(key_Coun)

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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)

		pose, reve = AnimFina(key_Coun, valu, pose, bone, reve, -1, mirr)
		animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

		################

		# shared pose

		shol = Bone(name = name + "." + "shou.l")
		elbl = Bone(name = name + "." + "elbo.l", valu = (0.0, -90.0, -23.0))
		wril = Bone(name = name + "." + "wris.l")

		################

		# TODO:
		# switch arrow 0 and 4. make a layer 2 object
		# cuts off fingers

		# TODO
		# keys need to have a beginning and an end, otherwise cant switch from relative to absolute. or need to store current rotation at the end of a pose

		# ready bow
		key_Coun = 11
		valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr = AnimInit(key_Coun)

		# TODO: frame count changes outcome
		"""
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
		"""
		#"""
		time[0] = round(1.0 * fps_)
		time[1] = round(1.0 * fps_)
		time[2] = round(1.0 * fps_)
		time[3] = round(1.0 * fps_)
		time[4] = round(1.0 * fps_)
		time[5] = round(1.0 * fps_)
		time[6] = round(1.0 * fps_)
		time[7] = round(1.0 * fps_)
		time[8] = round(1.0 * fps_)
		time[9] = round(1.0 * fps_)
		time[10] = round(1.0 * fps_)
		#"""

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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		# 5 - pass to other hand
		inde += 1
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, -48.0, 20.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((-10.5, -20.0, 13.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((68.4, -22.3, -3.4))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "bow_")
		valu[inde].append((20.0, 20.0, -20.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		# 6 - hand to arrow
		inde += 1
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, -136.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((0.0, -121.8, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "bow_")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		# 7 - draw arrow
		inde += 1
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, -164.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((0.0, -26.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((0.0, -63.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "bow_")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "quiv")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		if blen:
			bone[inde].append(name + "." + "arro.011")
		else:
			bone[inde].append(owne["inde"])
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		# 8 - clear quiver
		inde += 1
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, -90.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((0.0, -26.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((0.0, -63.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.l")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "bow_")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "quiv")
		valu[inde].append((0.0, 60.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(inde + 1)
		if blen:
			bone[inde].append(name + "." + "arro.011")
		else:
			bone[inde].append(owne["inde"])
		valu[inde].append((5.0, 8.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		# 9 - arrow to bow
		inde += 1
		# TODO: need a system for this
		#print("copy to inde" , inde)
		writInde = inde
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, -8.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((0.0, -90.0, 24.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((0.0, 23.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "bow_")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		# TODO: should return this to start
		# TODO: should be timed for gravity
		bone[inde].append(name + "." + "quiv")
		valu[inde].append((-1, -1, -1))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(inde - 1)
		if blen:
			bone[inde].append(name + "." + "arro.011")
		else:
			bone[inde].append(owne["inde"])
		valu[inde].append((70.0, 20.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		bone, valu, typ_, abso, mirr = AppeFromBone(shol, inde, bone, valu, typ_, abso, mirr)
		bone, valu, typ_, abso, mirr = AppeFromBone(elbl, inde, bone, valu, typ_, abso, mirr)
		bone, valu, typ_, abso, mirr = AppeFromBone(wril, inde, bone, valu, typ_, abso, mirr)
		# 10 - extend bow
		inde += 1
		bone[inde].append(name + "." + "shou.r")
		valu[inde].append((0.0, -50.0, -15.7))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "shou.l")
		valu[inde].append((0.0, -45.0, -13.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.r")
		valu[inde].append((100.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.l")
		valu[inde].append((0.0, -45.0, -30.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		bone[inde].append(name + "." + "wris.r")
		valu[inde].append((-84.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.l")
		valu[inde].append((0.0, 40.0, 20.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "bow_")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "quiv")
		valu[inde].append((0.0, 0.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)
		if blen:
			bone[inde].append(name + "." + "arro.011")
		else:
			bone[inde].append(owne["inde"])
		valu[inde].append((0.0, -15.0, 0.0))
		typ_[inde].append(True)
		abso[inde].append(False)
		mirr[inde].append(-1)

		pose, reve = AnimFina(key_Coun, valu, pose, bone, reve, 0, mirr)
		animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

		#brea = False
		#for a in range(len(pose[mirrInde[0]])):
		#	for b in range(len(pose[mirrInde[1]])):
		#		if pose[mirrInde[0]][a][0] == mirrName and pose[mirrInde[1]][b][0] == mirrName:
		#			pose[mirrInde[1]][b][1] = Math.VectScal(pose[mirrInde[0]][a][1], -1.0)
		#			brea = True
		#			break
		#	if brea:
		#		break
		#for pos_ in pose:
		#	print(pos_)
		#return 0

		################

		# clear sword for bow

		key_Coun = 6
		valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr = AnimInit(key_Coun)
		"""
		time[0] = round(0.2 * fps_)
		time[1] = round(0.2 * fps_)
		time[2] = round(0.2 * fps_)
		time[3] = round(0.3 * fps_)
		time[4] = round(0.3 * fps_)
		time[5] = round(0.1 * fps_)
		"""
		#"""
		time[0] = round(1.0 * fps_)
		time[1] = round(1.0 * fps_)
		time[2] = round(1.0 * fps_)
		time[3] = round(1.0 * fps_)
		time[4] = round(1.0 * fps_)
		time[5] = round(1.0 * fps_)
		#"""
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		# raise sword
		inde += 1
		bone[inde].append(name + "." + "shou.l")
		valu[inde].append((0.0, -140.0, -16.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "elbo.l")
		valu[inde].append((-30.0, 0.0, 60.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
		bone[inde].append(name + "." + "wris.l")
		valu[inde].append((0.0, 76.0, -10.0))
		typ_[inde].append(True)
		abso[inde].append(True)
		mirr[inde].append(-1)
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
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		mirr[inde].append(-1)
		# hold out hand for bow
		inde += 1
		# TODO: system
		#print("copy from inde", inde)
		readInde = inde
		#return 0
		bone, valu, typ_, abso, mirr = AppeFromBone(shol, inde, bone, valu, typ_, abso, mirr)
		bone, valu, typ_, abso, mirr = AppeFromBone(elbl, inde, bone, valu, typ_, abso, mirr)
		bone, valu, typ_, abso, mirr = AppeFromBone(wril, inde, bone, valu, typ_, abso, mirr)

		pose, reve = AnimFina(key_Coun, valu, pose, bone, reve, 1, mirr)
		animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

		boneList = BoneList(pose, typ_, abso, readInde)

		# TODO: make a function
		# copy to inde 9
		# copy from inde 5
		#print(animList[3][0][9])
		#print(animList[4][0][5])
		#for a in range(len(animList[3][0][9])):
		#	for b in range(len(animList[4][0][5])):
		#		if animList[3][0][9][a][0] == animList[4][0][5][b][0]:
		#			animList[3][0][9][a][1] = animList[4][0][5][b][1]
		for a in range(len(animList[3][0][writInde])):
			for b in range(len(boneList)):
				if animList[3][0][writInde][a][0] == boneList[b]["name"]:
					animList[3][0][9][a][1] = boneList[b]["valu"]
		#return 0

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
			
		# TODO: dont really need phas except for 0 / -1. use inde?
		for a in range(star, end_ + 1):
			# TODO
			"""
			# swing sword
			if a == 2 and ani_List[0] == 0.01666666753590107:
				scen.objects[name + ".swor"].setParent(name + ".wris.r")
				eule = mathutils.Euler((0.0, -math.pi / 2.0, 0.0), 'XYZ')
				scen.objects[name + ".swor"].worldOrientation = eule.to_matrix()
				posi = scen.objects[name + ".wris.r"].worldPosition
				scen.objects[name + ".swor"].worldPosition = posi
			"""
			# TODO: create as many varibles as needed to hold maximum simultaneous animations
			ind_ = a - star
			if blen:
				phas = bpy.data.objects[name].game.properties["ani" + str(ind_) + "Phas"].value
				inde = bpy.data.objects[name].game.properties["pos" + str(ind_)].value
				anim = bpy.data.objects[name].game.properties["ani" + str(ind_) + "Time"].value
			else:
				phas = owne["ani" + str(ind_) + "Phas"]
				inde = owne["pos" + str(ind_)]
				anim = owne["ani" + str(ind_) + "Time"]
			if anim != -1:
				if blen:
					continu_ = True
				phas, inde, anim = AnimPhas(animList[a][0], animList[a][1], animList[a][2], animList[a][3], phas, inde, anim, animList[a][4], animList[a][5], animList[a][6], animList[a][7], blen)
				if blen:
					bpy.data.objects[name].game.properties["ani" + str(ind_) + "Phas"].value = phas
					bpy.data.objects[name].game.properties["pos" + str(ind_)].value = inde
					bpy.data.objects[name].game.properties["ani" + str(ind_) + "Time"].value = anim
				else:
					owne["ani" + str(ind_) + "Phas"] = phas
					owne["pos" + str(ind_)] = inde
					owne["ani" + str(ind_) + "Time"] = anim

def AnimFina(key_Coun, valu, pose, bone, reve, offsInde, mirr):
	if offsInde != -1:
		offsList = []
		try:
			import bge
			cont = bge.logic.getCurrentController()
			owne = cont.owner
			for a in range(len(valu)):
				offs = []
				for b in range(len(valu[a])):
					x = owne["offs." + str(offsInde) + "." + str(a) + "." + str(b) + ".x"]
					y = owne["offs." + str(offsInde) + "." + str(a) + "." + str(b) + ".y"]
					z = owne["offs." + str(offsInde) + "." + str(a) + "." + str(b) + ".z"]
					offs.append((x, y, z))
				offsList.append(offs)
			#print("try finished")
		except:
			for a in range(len(valu)):
				offs = []
				for b in range(len(valu[a])):
					offs.append((0.0, 0.0, 0.0))
				offsList.append(offs)
			#print("except finished")
		for a in range(key_Coun):
			for b in range(len(valu[a])):
				reve[a].append(False)
				#print(offsList)
				pose = PoseAdd_(pose, a, bone, valu, offsList)
	#brea = False
	#for a in range(len(pose[mirrInde[0]])):
	#	for b in range(len(pose[mirrInde[1]])):
	#		if pose[mirrInde[0]][a][0] == mirrName and pose[mirrInde[1]][b][0] == mirrName:
	#			pose[mirrInde[1]][b][1] = Math.VectScal(pose[mirrInde[0]][a][1], -1.0)
	#			brea = True
	#			break
	#	if brea:
	#		break
	"""
	brea = False
	for a in range(len(mirr)):
		for b in range(len(mirr[a])):
			#if a != 0 and mirr[a][b]:
			if mirr[a][b] != -1:
				for c in range(a):
					for d in range(len(mirr[c])):
						#if mirr[a - 1][d] != -1 and pose[a][b][0] == pose[a - 1][d][0]:
						if mirr[c][d] != -1 and pose[a][b][0] == pose[c][d][0] and :
							pose[a][b][1] = Math.VectScal(pose[c][d][1], -1.0)
							brea = True
							break
			if brea:
				break
		if brea:
			break
	"""
	brea = False
	for a in range(len(mirr)):
		for b in range(len(mirr[a])):
			mirrLowe = mirr[a][b]
			if mirrLowe != -1 and mirrLowe < a:
				for d in range(len(mirr[mirrLowe])):
					mirrUppe = mirr[mirrLowe][d]
					if mirrUppe == a and pose[a][b][0] == pose[mirrLowe][d][0]:
						#pose[a][b][1] = Math.VectScal(pose[mirrLowe][d][1], -1.0)
						pose[a][b][1] = (pose[mirrLowe][d][1][0] * -1.0, pose[mirrLowe][d][1][1] * -1.0, pose[mirrLowe][d][1][2] * -1.0)
						brea = True
						break
			if brea:
				break
		if brea:
			break

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
	mirr = []
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
		mirr.append([])
	return valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr

"""
# TODO: turn to block
# ready shield
key_Coun = 3
valu, time, pose, pare, reve, typ_, bone = AnimInit(key_Coun)
time[0] = 1.0
time[1] = 1.0
pare[0] = [owne.name + "." + "shie", owne.name + "." + "wris.l"]
end_ = key_Coun - 2
inde = 0
# start
bone[inde].append(name + "." + "shou.l")
bone[inde].append(name + "." + "elbo.l")
bone[inde].append(name + "." + "wris.l")
bone[inde].append(name + "." + "shie")
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.03517, 0.34419, 1.31144))
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(False)
inde += 1
# hand to handle
bone[inde].append(name + "." + "shou.l")
bone[inde].append(name + "." + "elbo.l")
bone[inde].append(name + "." + "wris.l")
bone[inde].append(name + "." + "shie")
bone[inde].append(name + "." + "shie")
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.0, 0.0, 0.0))
#valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.03517, 0.34419, 1.08))
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(False)
inde += 1
# raise
bone[inde].append(name + "." + "shou.l")
bone[inde].append(name + "." + "elbo.l")
bone[inde].append(name + "." + "wris.l")
bone[inde].append(name + "." + "shie")
bone[inde].append(name + "." + "shie")
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.0, -90.0, 0.0))
valu[inde].append((0.0, 0.0, 0.0))
valu[inde].append((0.0, -90.0, 0.0))
#valu[inde].append((0.07, 0.15, -0.05))
valu[inde].append((0.0, 0.0, 0.0))
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(True)
typ_[inde].append(False)
pose, reve = AnimFina(key_Coun, valu, pose, bone, reve)
animList.append([pose, time, pare, reve, end_, typ_])
"""

main()

