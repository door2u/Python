
def Vect(vec1, vec2):
	retu = []
	a = 0
	while a < len(vec1):
		retu.append(vec2[a] - vec1[a])
		a += 1
	return tuple(retu)

def Dist(vec1, vec2):
	return VectMagn(Vect(vec1, vec2))

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
	prin = True
	prin = False
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
		else:
			if prin == True:
				print("math domain error", argu)
	else:
		if prin == True:
			print("approaching divide by 0", deno)
	return retu

def VectScal(vect, scal):
	retu = []
	a = 0
	while a < len(vect):
		retu.append(vect[a] * scal)
		a += 1
	return tuple(retu)

def Elli(t = 0.0, spee = 1.0, radi = 0.2, phas = 0.0, rati = 0.2):
	import math
	y = radi * math.sin(t * 2.0 * math.pi * spee + phas)
	x = radi * math.cos(t * 2.0 * math.pi * spee + phas)
	y *= rati
	return x, y

# axle has to directly under the hip or shoulder in (x or y) for this to work
# place bones directly underneath (x and y) the root bone. (elbow goes directly under shoulder, wrist directly under elbow, hand tip directly under wrist)
# ik solution:
# form two right triangles with the line from hip to target (foot) as the base
# a**2 + b**2 = c**2
# a1**2 + b1**2 = c1**2
# a2**2 + b2**2 = c2**2
# b1**2 = c1**2 - a1**2
# b2**2 = c2**2 - a2**2
#	b1 = b2
# c1**2 - a1**2 = c2**2 - a2**2
#	a1 + a2 = A
#	a1 = A - a2
# c1**2 - (A - a2)**2 = c2**2 - a2**2
# c1**2 - (A**2 - 2Aa2 + a2**2) = c2**2 - a2**2
# c1**2 - A**2 + 2Aa2 - a2**2 = c2**2 - a2**2
# c1**2 - A**2 + 2Aa2 = c2**2
# 2Aa2 = c2**2 - c1**2 + A**2
# a2 = (c2**2 - c1**2 + A**2) / 2A
# c1 is uppe, c2 is lowe
def Ik2d(arms = False, A = 1.0, angl = 0.0, uppeLeng = 1.0, loweLeng = 1.0):
	import math
	tole = 0.0001
	# solution
	# TODO: maybe solve for a1
	a2 = (loweLeng ** 2.0 - uppeLeng ** 2.0 + A ** 2.0) / (2.0 * A)
	rati = (A - a2) / uppeLeng
	uppeAngl = 0.0
	loweAngl = 0.0
	if math.fabs(rati) <= 1.0 + tole:
		if rati > 1.0:
			#print("tolerance correction")
			rati = 1.0
		if rati < -1.0:
			#print("tolerance correction")
			rati = -1.0
		bend = math.acos(rati)
		uppeAngl = angl + bend
		if arms == True:
			uppeAngl = angl - bend
	else:
		#print("parent bone domain error")
		# straight to target
		uppeAngl = angl
	rati = a2 / loweLeng
	if math.fabs(rati) <= 1.0 + tole:
		if rati > 1.0:
			#print("tolerance correction")
			rati = 1.0
		if rati < -1.0:
			#print("tolerance correction")
			rati = -1.0
		if arms == False:
			loweAngl = angl - uppeAngl - math.acos(rati)
		else:
			loweAngl = angl - uppeAngl + math.acos(rati)
	else:
		#print("child bone domain error")
		if arms == False:
			loweAngl = angl - uppeAngl
	stra = False
	#stra = True
	# points hips at target and set knees to 0.0 (for debugging "angle" var)
	if stra == True:
		uppeAngl = angl
		loweAngl = 0.0
	return uppeAngl, loweAngl

def CyclPath(t = 0.0, acti = "jog", spee = 1.0, radi = 0.2, phas = 0.0, step = 16, righ = False, arms = False):
	import bge
	import math
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	y = radi * math.sin(t * 2.0 * math.pi * spee + phas)
	x = radi * math.cos(t * 2.0 * math.pi * spee + phas)
	angl = math.atan2(y, x)
	while angl < 0.0:
		angl += 2.0 * math.pi

	#print("cycl angl", angl)


	# File "cycl.py", line 179, in CyclPath
	# KeyError: 'value = gameOb[key]: KX_GameObject, key "jogLegsX16" does not exist'
	



	# TODO: think theres a simpler way to do this
	stepThis = int(step * angl / (2.0 * math.pi))
	# get the total distance of all points: distance
	# find the progress of the angle relative to the current step
	# TODO: is this right? angle between points are all different
	stepSing = 2.0 * math.pi / step
	# find the angle remainder
	rema = angl
	while rema >= stepSing:
		rema -= stepSing
	part = "Legs"
	if arms == 1:
		part = "Arms"
	x1 = acti + part + "X"
	if stepThis < 10:
		x1 += "0"
	x1 += str(stepThis)
	y1 = acti + part + "Y"
	if stepThis < 10:
		y1 += "0"
	y1 += str(stepThis)
	if stepThis < step - 1:
		stepNext = stepThis + 1
	else:
		stepNext = 0
	x2 = acti + part + "X"
	if stepNext < 10:
		x2 += "0"
	x2 += str(stepNext)
	y2 = acti + part + "Y"
	if stepNext < 10:
		y2 += "0"
	y2 += str(stepNext)
	# for non-adjusted angle, the ratio of progress (a) to a full step (b)
	prog = rema / stepSing
	stax = owne[x1]
	stay = owne[y1]
	endx = owne[x2]
	endy = owne[y2]
	# angle between this step and the next step
	diff = -VectAngl((stax, stay), (endx, endy))
	prog *= diff
	# angle from origin to x, y start of this step
	a = math.atan2(stay, stax)
	while a < 0.0:
		a += 2.0 * math.pi
	b = math.atan2(endy, endx)
	while b < 0.0:
		b += 2.0 * math.pi
	# add adjusted progress to angle a, the start of this step
	a += prog
	x = math.cos(a)
	y = math.sin(a)
	# new radius: intersection between angle a and line from start x y to end x y
	m1 = (y / x)
	b1 = 0.0
	deno = endx - stax
	if deno != 0.0:
		m2 = (endy - stay) / deno
	b2 = (endy) - m2 * (endx)
	deno = m1 - m2
	if deno != 0.0:
		X = (b2 - b1) / (m1 - m2)
		Y = m1 * X
	else:
		X = 0.0
		Y = 0.0
	return X, Y

def Cycl(trac = "axle.legs.l", t = 0.0, acti = "jog", radi = 0.2, spee = 0.1, uppe = "", lowe = "", end = "", righ = False, arms = False, armsPath = True, armsRati = 0.05, uppeLeng = 1.0, loweLeng = 1.0, faci = (1.0, 0.0)):
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	part = "axle."
	if arms == 0:
		part += "legs."
	else:
		part += "arms."
	# TODO
	phas = 0.0
	if righ == False:
		part += "l"
		if arms == False:
			phas = -math.pi / 1.0
	else:
		part += "r"
		if arms == True:
			phas = -math.pi / 1.0
	nameStri = owne.name + "." + part
	if arms == False or (arms == True and armsPath == True):
		peda = CyclPath(t = t, acti = acti, spee = spee, radi = radi, phas = phas, righ = righ, arms = arms)
	else:
		peda = Elli(t = -t, spee = spee, radi = radi, phas = phas, rati = armsRati)
	peda = VectScal(peda, radi)
	tracPosi = scen.objects[trac].localPosition
	tota = uppeLeng + loweLeng
	# the distance from hip where the foot should be
	uppePosi = scen.objects[uppe].localPosition
	# TODO: convert x/y to x using faci
	uppePosi = (uppePosi[0], 0.0, uppePosi[2])
	targPosi = (peda[0] + tracPosi[0], 0.0, peda[1] + tracPosi[2])
	difx = targPosi[0] - uppePosi[0]
	dify = targPosi[2] - uppePosi[2]
	angl = math.atan2(dify, difx) + math.pi / 2.0
	A = Dist(uppePosi, targPosi)
	if A > tota:
		A = tota
	uppeAngl, loweAngl = Ik2d(arms = arms, A = A, angl = angl, uppeLeng = uppeLeng, loweLeng = loweLeng)
	eule = mathutils.Euler((faci[1] * uppeAngl, -faci[0] * uppeAngl, 0.0), 'XYZ')
	scen.objects[uppe].localOrientation = eule.to_matrix()
	eule = mathutils.Euler((faci[1] * loweAngl, -faci[0] * loweAngl, 0.0), 'XYZ')
	scen.objects[lowe].localOrientation = eule.to_matrix()

# TODO
def main():
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	# TODO: read this
	faci = (1.0, 0.0)
	acti = owne["acti"]
	cycl = owne[acti]
	if cycl == 1:
		owne["cyclTime"] = 0.0
		owne[acti] = 2
		cycl = 2
	if cycl == 2:
		t = owne["cyclTime"]
		cyclRadi = owne[acti + "LegsRadi"]
		cyclSpee = owne[acti + "CyclSpee"]
		uppeLeng = owne["legsUppe"]
		loweLeng = owne["legsLowe"]

		spee = owne[acti + "Spee"]
		cyclRadi *= spee
		cyclSpee *= spee

		Cycl(trac = owne.name + ".axle.legs.l", t = t, acti = acti, radi = cyclRadi, spee = cyclSpee, uppe = owne.name + ".hip_.l", lowe = owne.name + ".knee.l", end = owne.name + ".foot.l", righ = False, arms = False, armsRati = 0.0, uppeLeng = uppeLeng, loweLeng = loweLeng, faci = faci)
		Cycl(trac = owne.name + ".axle.legs.r", t = t, acti = acti, radi = cyclRadi, spee = cyclSpee, uppe = owne.name + ".hip_.r", lowe = owne.name + ".knee.r", end = owne.name + ".foot.r", righ = True,  arms = False, armsRati = 0.0, uppeLeng = uppeLeng, loweLeng = loweLeng)
		cyclArms = owne[acti + "CyclArms"]
		if cyclArms == True:
			uppeLeng = owne["armsUppe"]
			loweLeng = owne["armsLowe"]
			cyclRadi = owne[acti + "ArmsRadi"]
			cyclRadi *= spee
			armsRati = owne[acti + "ArmsRati"]
			Cycl(trac = owne.name + ".axle.arms.l", t = t, acti = acti, radi = cyclRadi, spee = cyclSpee, uppe = owne.name + ".shou.l", lowe = owne.name + ".elbo.l", end = owne.name + ".hand.l", righ = False, arms = True, armsRati = armsRati, uppeLeng = uppeLeng, loweLeng = loweLeng)
			Cycl(trac = owne.name + ".axle.arms.r", t = t, acti = acti, radi = cyclRadi, spee = cyclSpee, uppe = owne.name + ".shou.r", lowe = owne.name + ".elbo.r", end = owne.name + ".hand.r", righ = True,  arms = True, armsRati = armsRati, uppeLeng = uppeLeng, loweLeng = loweLeng)
		osci = owne[acti + "Osci"]
		if osci != 0.0:
			#z = osci * math.sin(spee * t * 4.0 * math.pi) - osci / 2.0
			z = osci * math.sin(cyclSpee * t * 4.0 * math.pi) - osci / 2.0
			owne["z___"] = z
		tilt = owne[acti + "Tilt"]
		if tilt != 0.0:
			orie = mathutils.Matrix(scen.objects[owne.name + "." + "body"].localOrientation)
			orie = orie.to_euler()
			eule = mathutils.Euler((-tilt * faci[1], tilt * faci[0], orie[2]), 'XYZ')
			scen.objects[owne.name + "." + "body"].localOrientation = eule.to_matrix()
	if cycl == 3:
		eule = mathutils.Euler((0.0, 0.0,0.0), 'XYZ')
		scen.objects[owne.name + "." + "hip_.l"].localOrientation = eule.to_matrix()
		scen.objects[owne.name + "." + "hip_.r"].localOrientation = eule.to_matrix()
		scen.objects[owne.name + "." + "knee.l"].localOrientation = eule.to_matrix()
		scen.objects[owne.name + "." + "knee.r"].localOrientation = eule.to_matrix()
		scen.objects[owne.name + "." + "shou.l"].localOrientation = eule.to_matrix()
		scen.objects[owne.name + "." + "shou.r"].localOrientation = eule.to_matrix()
		scen.objects[owne.name + "." + "elbo.l"].localOrientation = eule.to_matrix()
		scen.objects[owne.name + "." + "elbo.r"].localOrientation = eule.to_matrix()
		osci = owne[acti + "Osci"]
		if osci != 0.0:
			owne["z___"] = 0.0
		tilt = owne[acti + "Tilt"]
		if tilt != 0.0:
			orie = mathutils.Matrix(scen.objects[owne.name + "." + "body"].localOrientation)
			orie = orie.to_euler()
			eule = mathutils.Euler((0.0, 0.0, orie[2]), 'XYZ')
			scen.objects[owne.name + "." + "body"].localOrientation = eule.to_matrix()
		owne[acti] = 0

main()
