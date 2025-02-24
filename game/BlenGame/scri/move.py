
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

def main():
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	if owne.sensors["move"].positive:
		acti = owne["acti"]
		spee = "spee"
		spee = owne[spee]
		angl = owne["dire"]
		x = spee * math.cos(angl)
		y = spee * math.sin(angl)
		owne.worldPosition = (owne.worldPosition[0] + x, owne.worldPosition[1] + y, owne.worldPosition[2])
		# set character z position
		grouHeig = scen.objects[owne.name + "." + "grou_cast"]["grouHeig"]
		# height displacement caused by run animation
		z___ = owne["z___"]
		bodyHeig = owne["bodyHeig"]
		scen.objects[owne.name + "." + "body"].localPosition = (scen.objects[owne.name + "." + "body"].localPosition[0], scen.objects[owne.name + "." + "body"].localPosition[1], bodyHeig + z___)
		if owne.worldPosition[2] > grouHeig:
			velo = owne["velo"]
			grav = owne["grav"]
			fps_ = owne["fps_"]
			owne.worldPosition[2] += velo
			velo += (grav / fps_)
			owne["velo"] = velo
		if owne.worldPosition[2] <= grouHeig:
			owne.worldPosition = (owne.worldPosition[0], owne.worldPosition[1], grouHeig)
			owne["velo"] = 0.0
		# set orientation to face destination
		orie = owne["orie"]
		if orie == True:
			dire = math.atan2(dify, difx)
			orie = mathutils.Matrix(owne.worldOrientation)
			orie = orie.to_euler()
			comp = orie[2]
			tole = 0.01
			if math.fabs(comp - dire) > tole:
				rotaSpee = owne["rotaSpee"]
				# get current orientation vector
				x___ = math.cos(comp)
				y___ = math.sin(comp)
				# get dest vector
				# get the angle difference
				diff = VectAngl((x___, y___), (vect[0], vect[1]))
				# multiply by rotate speed
				diff *= rotaSpee
				if AnglGrea(math.atan2(y___, x___), math.atan2(vect[1], vect[0])) == False:
					orie = mathutils.Euler((orie[0], orie[1], orie[2] + diff), 'XYZ')
				else:
					orie = mathutils.Euler((orie[0], orie[1], orie[2] - diff), 'XYZ')
				owne.worldOrientation = orie.to_matrix()
	else:
		scen.objects[owne.name + "." + "body"].localPosition = (scen.objects[owne.name + "." + "body"].localPosition[0], scen.objects[owne.name + "." + "body"].localPosition[1], owne["bodyHeig"])

main()
