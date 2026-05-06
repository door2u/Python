
def Swap(val1, val2):
	temp = val1
	val1 = val2
	val2 = temp
	return val1, val2

def Inte(star, end_, prog):
	return star + prog * (end_ - star)

def RotaInte(stax, endx, stay, endy, staz, endz, prog, blen, reve = False):
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
						scen.objects[obj1].localOrientation = RotaInte(pose[inde][a][1][0], pose[inde + 1][b][1][0], pose[inde][a][1][1], pose[inde + 1][b][1][1], pose[inde][a][1][2], pose[inde + 1][b][1][2], anim / time, blen, reve = rev_)
					else:
						scen.objects[obj1].applyRotation((math.radians(pose[inde + 1][b][1][0]) / time, math.radians(pose[inde + 1][b][1][1]) / time, math.radians(pose[inde + 1][b][1][2]) / time), True)
				else:
					if abs2:
						loca = LocaInte(pose[inde][a][1][0], pose[inde + 1][b][1][0], pose[inde][a][1][1], pose[inde + 1][b][1][1], pose[inde][a][1][2], pose[inde + 1][b][1][2], anim / time, reve = rev_)
						scen.objects[obj1].localPosition = loca
					else:
						scen.objects[obj1].localPosition = (scen.objects[obj1].localPosition[0] + pose[inde + 1][b][1][0] / time, scen.objects[obj1].localPosition[1] + pose[inde + 1][b][1][1] / time, scen.objects[obj1].localPosition[2] + pose[inde + 1][b][1][2] / time)
				break

def PoseAdd_(pose, inde, obje, valu, offs):
	pose[inde].append([obje[inde][len(pose[inde])], (valu[inde][len(pose[inde])][0] + offs[inde][len(pose[inde])][0], valu[inde][len(pose[inde])][1] + offs[inde][len(pose[inde])][1], valu[inde][len(pose[inde])][2] + offs[inde][len(pose[inde])][2])])
	return pose

def AnimPhas(pose, time, pare, reve, phas, inde, anim, end_, typ_, abso, dupl, blen):
	import bge
	import mathutils
	scen = bge.logic.getCurrentScene()
	import math
	time = time[inde]
	if anim >= 0 and anim < time - 2:
		Pose(pose, reve, inde, anim, time - 1, typ_, abso, blen)
		anim += 1
	else:
		for a in range(len(pose[inde])):
			if inde != 0 and typ_[inde][a] and abso[inde][a] == False:
				for b in range(len(pose[inde - 1])):
					if pose[inde][a][0] == pose[inde - 1][b][0]:
						pose[inde][a][1] = (pose[inde - 1][b][1][0] + pose[inde][a][1][0], pose[inde - 1][b][1][1] + pose[inde][a][1][1], pose[inde - 1][b][1][2] + pose[inde][a][1][2])
						abso[inde][a] = True
		Pose(pose, reve, inde, time - 1, time - 1, typ_, abso, blen)
		for a in range(len(pose[inde])):
			if typ_[inde][a]:
				orie = scen.objects[pose[inde][a][0]].worldOrientation
				orie = orie.to_euler()
				orie = (math.degrees(orie[0]), math.degrees(orie[1]), math.degrees(orie[2]))
				pose[inde][a][1] = orie
		if dupl[inde] != []:
			posi = scen.objects[dupl[inde][0]].worldPosition
			orie = scen.objects[dupl[inde][0]].worldOrientation
			obje = scen.addObject(dupl[inde][1], dupl[inde][1])
			scen.objects[scen.name + "." + "matt"]["inde"] = len(scen.objects) - 1
			scen.objects[dupl[inde][1]].worldPosition = posi
			scen.objects[dupl[inde][1]].worldOrientation = orie
		if pare[inde] != []:
			posi = scen.objects[pare[inde][0]].worldPosition
			orie = scen.objects[pare[inde][0]].worldOrientation
			scen.objects[pare[inde][0]].setParent(pare[inde][1])
			scen.objects[pare[inde][0]].worldPosition = posi
			scen.objects[pare[inde][0]].worldOrientation = orie
		inde += 1
		if phas == end_:
			anim = -1
		else:
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
	bone = ListAppe(bone, inde, boneDict["name"])
	valu = ListAppe(valu, inde, boneDict["valu"])
	typ_ = ListAppe(typ_, inde, boneDict["typ_"])
	abso = ListAppe(abso, inde, boneDict["abso"])
	mirr = ListAppe(mirr, inde, boneDict["mirr"])
	return bone, valu, typ_, abso, mirr

def BoneList(pose, typ_, abso, inde):
	boneList = []
	if len(pose) > inde:
		for a in range(len(pose[inde])):
			boneList.append(Bone(name = pose[inde][a][0], valu = pose[inde][a][1], typ_ = typ_[inde][a], abso = abso[inde][a], mirr = False))
	return boneList

def main(vari, cont, scen, owne, math, Math, mathutils, lookY___Angl, one_, two_, thre, clic, clii):
	blen = False
	clicStar = owne["clicStar"]
	arroInde = owne["arroInde"]
	weap = owne["weap"]
	reveRead = False
	if one_:
		clicStar = False
		scen.objects[scen.name + "." + "came"]["char"] = 0
		scen.objects[scen.name + "." + "came"].setParent("temp.matt" + ".trac.posi")
		scen.objects[scen.name + "." + "came"].worldPosition = scen.objects["temp.matt" + ".trac.posi"].worldPosition
		scen.objects[scen.name + "." + "reti"].visible = 0
		owne["righArm_"] = True
		owne["leftArm_"] = True
		weap = 0
		orie = mathutils.Euler((0.0, 0.0, 0.0))
		scen.objects["temp.matt.shou.r"].orientation = orie.to_matrix()
		scen.objects["temp.matt.elbo.r"].orientation = orie.to_matrix()
		scen.objects["temp.matt.wris.r"].orientation = orie.to_matrix()
		scen.objects["temp.matt.shou.l"].orientation = orie.to_matrix()
		scen.objects["temp.matt.elbo.l"].orientation = orie.to_matrix()
		scen.objects["temp.matt.wris.l"].orientation = orie.to_matrix()
		scen.objects["temp.matt" + ".swor"].setParent("temp.matt" + ".body")
		scen.objects["temp.matt.swor"].localPosition = (0.1122, -0.1550, -0.10474395751953125)
		scen.objects["temp.matt.swor"].localOrientation = [( 0.9277, -0.1707, 0.3321), ( 0.1420,  0.9838, 0.1090),  (-0.3453, -0.0540, 0.9369)]
		scen.objects["temp.matt" + ".bow_"].setParent("temp.matt" + ".body")
		scen.objects["temp.matt.bow_"].localPosition = (0.2158, -0.0494, -0.1820)
		scen.objects["temp.matt.bow_"].localOrientation = [(0.9997,  0.0125, -0.0230), (0.0000,  0.8796,  0.4756), (0.0262, -0.4755,  0.8793)]
		scen.objects["temp.matt.swor"].visible = 1
	if two_:
		clicStar = False
		scen.objects[scen.name + "." + "came"]["char"] = 0
		scen.objects[scen.name + "." + "came"].setParent("temp.matt" + ".trac.posi")
		scen.objects[scen.name + "." + "came"].worldPosition = scen.objects["temp.matt" + ".trac.posi"].worldPosition
		scen.objects[scen.name + "." + "reti"].visible = 0
		owne["righArm_"] = False
		weap = 1
		orie = mathutils.Euler((0.0, 0.0, 0.0))
		scen.objects["temp.matt.shou.r"].orientation = orie.to_matrix()
		orie = mathutils.Euler(Math.VectRadi((0.0, -90.0, 0.0)))
		scen.objects["temp.matt.elbo.r"].orientation = orie.to_matrix()
		orie = mathutils.Euler((0.0, 0.0, 0.0))
		scen.objects["temp.matt.wris.r"].orientation = orie.to_matrix()
		scen.objects["temp.matt.shou.l"].orientation = orie.to_matrix()
		scen.objects["temp.matt.elbo.l"].orientation = orie.to_matrix()
		scen.objects["temp.matt.wris.l"].orientation = orie.to_matrix()
		scen.objects["temp.matt" + ".swor"].setParent("temp.matt" + ".wris.r")
		orie = mathutils.Euler(Math.VectRadi((0.0, 180.0, 0.0)))
		scen.objects["temp.matt.swor"].localPosition = (0.0953, 0.0165, -0.1068)
		scen.objects["temp.matt.swor"].localOrientation = [(0.0000, -0.0000, -1.0000), (0.0000,  1.0000,  0.0000),  (1.0000, -0.0000,  0.0000)]
		scen.objects["temp.matt" + ".bow_"].setParent("temp.matt" + ".body")
		scen.objects["temp.matt.bow_"].localPosition = (0.2158, -0.0494, -0.1820)
		scen.objects["temp.matt.bow_"].localOrientation = [(0.9997,  0.0125, -0.0230), (0.0000,  0.8796,  0.4756), (0.0262, -0.4755,  0.8793)]
		scen.objects["temp.matt.swor"].visible = 1
	if thre:
		clicStar = False
		scen.objects[scen.name + "." + "came"]["char"] = -1
		scen.objects[scen.name + "." + "came"].setParent("temp.matt" + ".trac.shou")
		scen.objects[scen.name + "." + "came"].worldPosition = scen.objects["temp.matt" + ".trac.shou"].worldPosition
		scen.objects[scen.name + "." + "reti"].visible = 1
		owne["righArm_"] = False
		owne["leftArm_"] = False
		weap = 2
		orie = mathutils.Euler(Math.VectRadi((-32.9, -39.8, 39.1)))
		scen.objects["temp.matt.shou.r"].orientation = orie.to_matrix()
		orie = mathutils.Euler(Math.VectRadi((52.1, -111.9, 18.7)))
		scen.objects["temp.matt.elbo.r"].orientation = orie.to_matrix()
		orie = mathutils.Euler(Math.VectRadi((-25.5, 0.0, -75.7)))
		scen.objects["temp.matt.wris.r"].orientation = orie.to_matrix()
		orie = mathutils.Euler(Math.VectRadi((0.0, -49.6, -12.1)))
		scen.objects["temp.matt.shou.l"].orientation = orie.to_matrix()
		orie = mathutils.Euler(Math.VectRadi((0.0, -14.0, -12.3)))
		scen.objects["temp.matt.elbo.l"].orientation = orie.to_matrix()
		orie = mathutils.Euler(Math.VectRadi((0.0, 0.0, 0.0)))
		scen.objects["temp.matt.wris.l"].orientation = orie.to_matrix()
		scen.objects["temp.matt" + ".swor"].setParent("temp.matt" + ".body")
		scen.objects["temp.matt.swor"].localPosition = (0.1122, -0.1550, -0.10474395751953125)
		scen.objects["temp.matt.swor"].localOrientation = [( 0.9277, -0.1707, 0.3321), ( 0.1420,  0.9838, 0.1090),  (-0.3453, -0.0540, 0.9369)]
		scen.objects["temp.matt" + ".bow_"].setParent("temp.matt" + ".wris.l")
		scen.objects["temp.matt.bow_"].localPosition = (0.0224, -0.0139, -0.1163)
		scen.objects["temp.matt.bow_"].localOrientation = [( 0.3773, -0.2923, 0.8788), ( 0.3398,  0.9264, 0.1622), (-0.8615,  0.2374, 0.4489)]
		scen.objects["temp.matt.swor"].visible = 0
	owne["weap"] = weap
	name = "matt"
	animList = []
	fps_ = 60
	animStar = owne["animStar"]
	animEnd_ = owne["animEnd_"]
	if clic:
		if weap == 1:
			animStar = 0
			animEnd_ = 0
			owne["ani0Phas"] = 0
			owne["ani0Time"] = 0
			owne["pos0"] = 0
		if weap == 2:
			animStar = 1
			animEnd_ = 1
			owne["ani0Phas"] = 0
			owne["ani0Time"] = 0
			owne["pos0"] = 0
			clicStar = True
			orie = scen.objects["temp.matt.shou.r"].localOrientation
			orie = orie.to_euler()
			vari["orrx"] = orie[0]
			vari["orry"] = orie[1]
			vari["orrz"] = orie[2]
			orie = scen.objects["temp.matt.shou.l"].localOrientation
			orie = orie.to_euler()
			vari["orlx"] = orie[0]
			vari["orly"] = orie[1]
			vari["orlz"] = orie[2]
	if clii:
		if weap == 2 and clicStar:
			clicStar = False
			orie = mathutils.Euler(Math.VectRadi((-32.9, -39.8, 39.1)))
			scen.objects["temp.matt.shou.r"].orientation = orie.to_matrix()
			orie = mathutils.Euler(Math.VectRadi((52.1, -111.9, 18.7)))
			scen.objects["temp.matt.elbo.r"].orientation = orie.to_matrix()
			orie = mathutils.Euler(Math.VectRadi((-25.5, 0.0, -75.7)))
			scen.objects["temp.matt.wris.r"].orientation = orie.to_matrix()
			orie = mathutils.Euler(Math.VectRadi((0.0, -49.6, -12.1)))
			scen.objects["temp.matt.shou.l"].orientation = orie.to_matrix()
			orie = mathutils.Euler(Math.VectRadi((0.0, -14.0, -12.3)))
			scen.objects["temp.matt.elbo.l"].orientation = orie.to_matrix()
			orie = mathutils.Euler(Math.VectRadi((0.0, 0.0, 0.0)))
			scen.objects["temp.matt.wris.l"].orientation = orie.to_matrix()
			scen.objects["temp.matt.bow_"].localPosition = (0.0224, -0.0139, -0.1163)
			scen.objects["temp.matt.bow_"].localOrientation = [( 0.3773, -0.2923, 0.8788), ( 0.3398,  0.9264, 0.1622), (-0.8615,  0.2374, 0.4489)]
	if clicStar:
		orie = mathutils.Euler((vari["orrx"], vari["orry"], vari["orrz"]))
		shif = 64.0
		orie.rotate_axis('Y', math.radians(-1.0 * lookY___Angl + shif + 0.2 * (90.0 - lookY___Angl)))
		scen.objects["temp.matt.shou.r"].localOrientation = orie.to_matrix()
		orie = mathutils.Euler((vari["orlx"], vari["orly"], vari["orlz"]))
		orie.rotate_axis('Y', math.radians(-1.0 * lookY___Angl + shif))
		scen.objects["temp.matt.shou.l"].localOrientation = orie.to_matrix()
	owne["clicStar"] = clicStar
	owne["animStar"] = animStar
	owne["animEnd_"] = animEnd_
	if weap == 2:
		z = scen.objects[scen.name + "." + "came"].worldOrientation
		z = z.to_euler()
		z = z[2] + math.pi / 2.0
		y = scen.objects[scen.name + "." + "matt.body"].worldOrientation
		y = y.to_euler()
		x = y[0]
		y = y[1]
		y = mathutils.Euler((x, y, z))
		scen.objects[scen.name + "." + "matt.body"].worldOrientation = y.to_matrix()
	key_Coun = 4
	valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr = AnimInit(key_Coun)
	time[0] = round(0.125 * fps_)
	time[1] = round(0.125 * fps_)
	time[2] = round(0.25 * fps_)
	inde = 0
	readShou = Bone(name = scen.name + "." + name + "." + "shou.r", valu = (0.0, 0.0, 0.0))
	readElbo = Bone(name = scen.name + "." + name + "." + "elbo.r", valu = (0.0, -90.0, 0.0))
	readSwor = Bone(name = scen.name + "." + name + "." + "swor", valu = (0.0, -90.0, 0.0))
	bone, valu, typ_, abso, mirr = AppeFromBone(readShou, inde, bone, valu, typ_, abso, mirr)
	bone, valu, typ_, abso, mirr = AppeFromBone(readElbo, inde, bone, valu, typ_, abso, mirr)
	bone, valu, typ_, abso, mirr = AppeFromBone(readSwor, inde, bone, valu, typ_, abso, mirr)
	inde += 1
	bone[inde].append(scen.name + "." + name + "." + "shou.r")
	bone[inde].append(scen.name + "." + name + "." + "elbo.r")
	bone[inde].append(scen.name + "." + name + "." + "swor")
	valu[inde].append((0.0, -40.0, 0.0))
	valu[inde].append((0.0, -90.0, 0.0))
	valu[inde].append((0.0, -90.0, 0.0))
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
	bone[inde].append(scen.name + "." + name + "." + "shou.r")
	bone[inde].append(scen.name + "." + name + "." + "elbo.r")
	bone[inde].append(scen.name + "." + name + "." + "swor")
	valu[inde].append((0.0, 20.0, 0.0))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, -45.0, 0.0))
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
	bone[inde].append(scen.name + "." + name + "." + "shou.r")
	bone[inde].append(scen.name + "." + name + "." + "elbo.r")
	bone[inde].append(scen.name + "." + name + "." + "swor")
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((0.0, -90.0, 0.0))
	valu[inde].append((0.0, -90.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	mirr[inde].append(-1)
	mirr[inde].append(-1)
	mirr[inde].append(-1)
	pose, reve = AnimFina(key_Coun, valu, pose, bone, reve, -1, mirr)
	animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

	key_Coun = 2
	valu, time, pose, pare, reve, typ_, bone, end_, abso, dupl, mirr = AnimInit(key_Coun)
	time[0] = 0
	time[1] = 0
	inde = 0
	bone[inde].append("temp.matt.bow_")
	bone[inde].append(arroInde)
	bone[inde].append(arroInde)
	bone[inde].append("temp.matt.shou.r")
	bone[inde].append("temp.matt.elbo.r")
	bone[inde].append("temp.matt.wris.r")
	bone[inde].append("temp.matt.shou.l")
	bone[inde].append("temp.matt.elbo.l")
	bone[inde].append("temp.matt.wris.l")
	valu[inde].append((math.degrees(0.4865), math.degrees(1.0382), math.degrees(0.7332)))
	valu[inde].append((math.degrees(-1.3334), math.degrees(1.3338), math.degrees(0.1411)))
	valu[inde].append((0.0, 0.0, 0.0))
	valu[inde].append((-32.9, -39.8, 39.1))
	valu[inde].append((52.1, -111.9, 18.7))
	valu[inde].append((-25.5, 0.0, -75.7))
	valu[inde].append((0.0, -49.6, -12.1))
	valu[inde].append((0.0, -14.0, -12.3))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(False)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(False)
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
	mirr[inde].append(-1)
	mirr[inde].append(-1)
	inde += 1
	bone[inde].append("temp.matt.bow_")
	bone[inde].append(arroInde)
	bone[inde].append(arroInde)
	bone[inde].append("temp.matt.shou.r")
	bone[inde].append("temp.matt.elbo.r")
	bone[inde].append("temp.matt.wris.r")
	bone[inde].append("temp.matt.shou.l")
	bone[inde].append("temp.matt.elbo.l")
	bone[inde].append("temp.matt.wris.l")
	valu[inde].append((40.0, 100.0, math.degrees(0.7332)))
	valu[inde].append((-56.0, 85.0, 35.0))
	valu[inde].append((0.05, -0.05, 0.0))
	valu[inde].append((-32.9, -75.0, 39.1))
	valu[inde].append((40.0, -100.0, 18.7))
	valu[inde].append((-25.5, 0.0, -75.7))
	valu[inde].append((0.0, -85.0, -12.1))
	valu[inde].append((0.0, -14.0, -12.3))
	valu[inde].append((0.0, 0.0, 0.0))
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(False)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	typ_[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(True)
	abso[inde].append(False)
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
	mirr[inde].append(-1)
	mirr[inde].append(-1)
	pose, reve = AnimFina(key_Coun, valu, pose, bone, reve, -1, mirr)
	animList.append([pose, time, pare, reve, end_, typ_, abso, dupl])

	if animStar > -1:
		for a in range(animStar, animEnd_ + 1):
			ind_ = a - animStar
			phas = owne["ani" + str(ind_) + "Phas"]
			inde = owne["pos" + str(ind_)]
			anim = owne["ani" + str(ind_) + "Time"]
			if anim != -1:
				phas, inde, anim = AnimPhas(animList[a][0], animList[a][1], animList[a][2], animList[a][3], phas, inde, anim, animList[a][4], animList[a][5], animList[a][6], animList[a][7], blen)
				owne["ani" + str(ind_) + "Phas"] = phas
				owne["pos" + str(ind_)] = inde
				owne["ani" + str(ind_) + "Time"] = anim
	owne["animStar"] = animStar
	owne["animEnd_"] = animEnd_
	owne["arroInde"] = arroInde
	return vari

def ListSet_(lis_, elem, valu):
	if len(lis_) > elem: lis_[elem] = valu
	else: print("ListSet_() out of range.")
	return lis_

def ListAppe(lis_, elem, valu):
	if len(lis_) > elem: lis_[elem].append(valu)
	else: print("ListAppe() out of range.")
	return lis_

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
		except:
			for a in range(len(valu)):
				offs = []
				for b in range(len(valu[a])):
					offs.append((0.0, 0.0, 0.0))
				offsList.append(offs)
	else:
		offsList = []
		for a in range(len(valu)):
			offs = []
			for b in range(len(valu[a])):
				offs.append((0.0, 0.0, 0.0))
			offsList.append(offs)
	for a in range(key_Coun):
		for b in range(len(valu[a])):
			reve[a].append(False)
			pose = PoseAdd_(pose, a, bone, valu, offsList)
	brea = False
	for a in range(len(mirr)):
		for b in range(len(mirr[a])):
			mirrLowe = mirr[a][b]
			if mirrLowe != -1 and mirrLowe < a:
				for d in range(len(mirr[mirrLowe])):
					mirrUppe = mirr[mirrLowe][d]
					if mirrUppe == a and pose[a][b][0] == pose[mirrLowe][d][0]:
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

