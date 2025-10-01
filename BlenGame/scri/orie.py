"""
def VectMagn(vect):
	retu = 0.0
	for dime in vect:
		retu += dime * dime
	return retu ** 0.5

def VectDot_(vec1, vec2):
	retu = 0.0
	a = 0
	while a < len(vec1):
		retu += vec1[a] * vec2[a]
		a += 1
	return retu

def VectAngl(vec1, vec2):
	import math
	retu = 0.0
	tole = 0.0001
	deno = VectMagn(vec1) * VectMagn(vec2)
	if math.fabs(deno) >= tole:
		argu = VectDot_(vec1, vec2) / deno
		if math.fabs(argu) <= 1.0 + tole:
			if argu > 1.0:
				argu = 1.0
			if argu < -1.0:
				argu = 1.0
			retu = math.acos(argu)
		#else:
		#	print("math domain error", argu)
	#else:
	#	print("approaching divide by 0", deno)
	return retu

# is angle 1 greater than (relatively counter-clockwise to) angle 2
def AnglGrea(ang1, ang2):
	import math
	retu = False
	ang1 -= ang2
	while ang1 > 1.0 * math.pi:
		ang1 -= 2.0 * math.pi
	while ang1 <= -1.0 * math.pi:
		ang1 += 2.0 * math.pi
	if ang1 > 0.0:
		retu = True
	return retu
"""

def main():
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	dire = -1
	if owne.sensors["W"].positive:
		if scen.objects[owne.name + "." + "forward"]["pathChec"]:
			dire = 2
	if owne.sensors["A"].positive:
		if scen.objects[owne.name + "." + "left"]["pathChec"]:
			dire = 0
	if owne.sensors["S"].positive:
		if scen.objects[owne.name + "." + "right"]["pathChec"]:
			dire = 3
	if owne.sensors["D"].positive:
		if scen.objects[owne.name + "." + "back"]["pathChec"]:
			dire = 1
	if dire != -1:
		orie = mathutils.Matrix(scen.objects[owne.name + "." + "look"].worldOrientation)
		orie = orie.to_euler()
		comp = orie[2]
		orie = mathutils.Matrix(scen.objects[owne.name + "." + "body"].worldOrientation)
		orie = orie.to_euler()
		diff = 0.0
		if dire == 0:
			diff = math.pi / 2.0
		if dire == 1:
			diff = -math.pi / 2.0
		if dire == 3:
			diff = math.pi
		orie = mathutils.Euler((orie[0], orie[1], comp + diff), 'XYZ')
		scen.objects[owne.name + "." + "body"].worldOrientation = orie.to_matrix()
		# TODO: get speed
		movx = 0.1 * math.cos(comp + diff)
		movy = 0.1 * math.sin(comp + diff)
		owne.worldPosition[0] += movx
		owne.worldPosition[1] += movy

		acti = owne["acti"]
		actiStag = owne[acti]
		if actiStag == 0:
			owne[acti] = 1
	else:
		#	scen.objects[owne.name + "." + "body"].localPosition = (scen.objects[owne.name + "." + "body"].localPosition[0], scen.objects[owne.name + "." + "body"].localPosition[1], owne["bodyHeig"])
		acti = owne["acti"]
		owne[acti] = 0

main()
