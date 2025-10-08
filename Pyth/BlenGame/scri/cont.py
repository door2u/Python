
def Pad_(numb):
	retu = ""
	if numb < 100:
		retu += "0"
	if numb < 10:
		retu += "0"
	retu += str(numb)
	return retu

def VectDot_(vec1, vec2):
	retu = 0.0
	a = 0
	while a < len(vec1):
		retu += vec1[a] * vec2[a]
		a += 1
	return retu

def VectMagn(vect):
	retu = 0.0
	for dime in vect:
		retu += dime * dime
	return retu ** 0.5

def VectScal(vect, scal):
	retu = []
	a = 0
	while a < len(vect):
		retu.append(vect[a] * scal)
		a += 1
	return tuple(retu)

def VectNorm(vect):
	import math
	tole = 0.0001
	magn = VectMagn(vect)
	retu = []
	a = 0
	while a < len(vect):
		if math.fabs(magn) >= tole:
			retu.append(vect[a] / magn)
		else:
			retu.append(0.0)
		a += 1
	return tuple(retu)

def main():
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	if owne.sensors["cont"].positive:
		acti = owne["acti"]
		spee = owne[acti + "Spee"]
		"""
		if spee > 0.0:
			magn = scen.objects[scen.name + "." + "scen_obje"]["inpuMagn"]
			spee *= magn
			# TODO: this is relative to +y?
			angl = math.radians(scen.objects[scen.name + "." + "scen_obje"]["inpuDire"])
			x = spee * math.cos(angl)
			y = spee * math.sin(angl)
			# path checking
			# TODO: look up coun
			#coun = 16
			coun = 4
			# get the closest True empty to x, y
			anglClos = 360.0
			inde = -1
			a = 0
			while a < coun:
				own_ = owne.name
				obje = "path" + "." + Pad_(a)
				ex = scen.objects[own_ + "." + obje].localPosition[0]
				ey = scen.objects[own_ + "." + obje].localPosition[1]
				# TODO: maybe start at +x
				emptAngl = math.atan2(ey, ex)
				# TODO: weird
				if emptAngl > math.pi / 2.0:
					emptAngl -= 2.0 * math.pi
				emptAngl = math.degrees(emptAngl)
				diff = math.fabs(emptAngl - math.degrees(angl))
				if diff < anglClos:
					anglClos = diff
					inde = a
				a += 1
			# counter-clockwise path empties
			counList = []
			# clockwise path empties
			clocList = []
			if inde != -1:
				obje = "path" + "." + Pad_(inde)
				obje = scen.objects[own_ + "." + obje]["pathChec"]
				if obje == False:
					a = 0
					# TODO: over 2 or 4
					while a < int(coun / 4):
						li = inde + (a + 1)
						ri = inde - (a + 1)
						if li >= coun:
							li -= coun
						if ri < 0:
							ri += coun
						obje = "path" + "." + Pad_(li)
						pathChec = scen.objects[own_ + "." + obje]["pathChec"]
						if pathChec:
							ex = scen.objects[own_ + "." + obje].localPosition[0]
							ey = scen.objects[own_ + "." + obje].localPosition[1]
							break
						obje = "path" + "." + Pad_(ri)
						pathChec = scen.objects[own_ + "." + obje]["pathChec"]
						if pathChec:
							ex = scen.objects[own_ + "." + obje].localPosition[0]
							ey = scen.objects[own_ + "." + obje].localPosition[1]
							break
						a += 1
					if a == int(coun / 4):
						ex = 0.0
						ey = 0.0
				else:
					ex = x
					ey = y
			# dot speed with empty x y
			damp = VectDot_(VectNorm((x, y)), VectNorm((ex, ey)))
			spee *= damp
			x = spee * math.cos(angl)
			y = spee * math.sin(angl)
		"""
		magn = scen.objects[scen.name + "." + "scen_obje"]["inpuMagn"]
		angl = math.radians(scen.objects[scen.name + "." + "scen_obje"]["inpuDire"])
		move = False
		# reset limbs to 0.0 by setting this to 3 (will override animations if they exist)
		actiValu = owne[acti]
		if magn == 0.0 or spee == 0.0:
			actiValu = 3
		else:
			lookX___Angl = scen.objects[owne.name + "." + "look"]["lookX___Angl"]
			angl += lookX___Angl
			# TODO
			angl += math.pi / 2.0
			# orient character
			orie = mathutils.Matrix(scen.objects[owne.name + "." + "body"].localOrientation)
			orie = orie.to_euler()
			# TODO: subtracting 90 from angl
			eule = mathutils.Euler((orie[0], orie[1], angl - math.pi / 2.0), 'XYZ')
			scen.objects[owne.name + "." + "body"].localOrientation = eule.to_matrix()
			owne["dire"] = angl
			acti = owne["acti"]
			if actiValu == 0:
				actiValu = 1
			move = True
		owne[acti] = actiValu
		owne["move"] = move
		owne["spee"] = spee

main()
