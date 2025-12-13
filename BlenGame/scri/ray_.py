
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
	return VectDot_(vect, vect) ** 0.5

def Vect(vec1, vec2):
	retu = []
	a = 0
	while a < len(vec1):
		retu.append(vec2[a] - vec1[a])
		a += 1
	return tuple(retu)

def VectAdd_(vec1, vec2):
	retu = []
	a = 0
	while a < len(vec1):
		retu.append(vec1[a] + vec2[a])
		a += 1
	return tuple(retu)

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

def VectCros3d__(vec1, vec2):
	a = vec1[1] * vec2[2] - vec1[2] * vec2[1]
	b = vec1[0] * vec2[2] - vec1[2] * vec2[0]
	c = vec1[0] * vec2[1] - vec1[1] * vec2[0]
	return (a, -b, c)

def Faci(dire, posi, targ):
	retu = True
	vect = Vect(posi, targ)
	dot_ = VectDot_(dire, vect)
	if dot_ < 0.0:
		retu = False
	return retu

def DistTo__Inte(vectOrig, vectDire, poin, norm):
	import math
	tole = 0.0001
	deno = VectDot_(vectDire, norm)
	dist = "divide by zero error"
	if math.fabs(deno) > tole:
		vect = Vect(vectOrig, poin)
		dist = VectDot_(vect, norm) / deno
	return dist

def Boun(poin = (0.0, 0.0, 0.0), ver1 = (0.0, 0.0, 0.0), ver2 = (0.0, 0.0, 0.0), ver3 = (0.0, 0.0, 0.0), sort = False, tole = 0.001):
	import math
	Engi = EngiLink()
	vec1 = Engi.Vect(poin, ver1)
	vec2 = Engi.Vect(poin, ver2)
	vec3 = Engi.Vect(poin, ver3)
	retu = False
	anglList = []
	if sort == True:
		vectList = [vec1, vec2, vec3]
		if len(vectList) > 1:
			axis = Engi.VectCros3d__(vectList[0], vectList[1])
			axis = Engi.VectNorm(axis)
			refe = Engi.Quat(vectList[0], 90.0, axis)
			anglList = [[0.0, vectList[0]]]
			a = 1
			while a < len(vectList):
				angl = Engi.VectAngl(vectList[a], vectList[0])
				angr = Engi.VectAngl(vectList[a], refe)
				if angr > 90.0:
					angl = (-1.0 * angl) + 360.0
				anglList.append([angl, vectList[a]])
				a += 1
			anglList = sorted(anglList)
	else:
		anglList = [[0.0, vec1], [0.0, vec2], [0.0, vec3]]
	tota = 0.0
	a = 1
	while a < len(anglList):
		add_ = Engi.VectAngl(anglList[a - 1][1], anglList[a][1])
		if type(add_) == float:
			tota += add_
		a += 1
	a -= 1
	if len(anglList) > a:
		add_ = Engi.VectAngl(anglList[a][1], anglList[0][1])
		if type(add_) == float:
			tota += add_
	if math.fabs(tota - 360.0) < tole:
		retu = True
	return retu

def Ray_(orig = (0.0, 0.0, 0.0), dest = (1.0, 0.0, 0.0), polyList = [], vertList = [], normList = [], centList = [], tole = 0.001, magnTole = 5.0, back = False, sort = False):
	Engi = EngiLink()
	pi = 3.14159265359
	dire = Engi.Vect(orig, dest)
	magn = Engi.VectMagn(dire)
	unit = Engi.VectNorm(dire)
	boun = False
	a = 0
	while a < len(polyList):
		poly = polyList[a]
		norm = normList[a]
		cent = centList[a]
		ver_List = []
		for b in range(len(poly)):
			ver_List.append(vertList[poly[b]])
		faci = Engi.Faci(unit, orig, cent)
		if faci == True:
			if back == True:
				faci = Engi.Faci(norm, cent, orig)
			else:
				faci = True
			if faci == True:
				dist = Engi.DistTo__Inte(orig, unit, cent, norm)
				if dist != "divide by zero error":
					if dist <= magn + magnTole:
						poin = Engi.VectScal(unit, dist)
						poin = Engi.VectAdd_(orig, poin)
						boun = Boun(ver1 = ver_List[0], ver2 = ver_List[1], ver3 = ver_List[2], poin = poin, sort = sort, tole = tole)
						if boun == True:
							break
		a += 1
	return boun

def TranRead(name):
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	rota = mathutils.Matrix(scen.objects[name].worldOrientation)
	rota = rota.to_euler()
	rota = (math.degrees(rota[0]), math.degrees(rota[1]), math.degrees(rota[2]))
	return scen.objects[name].worldScale, rota, scen.objects[name].worldPosition

def ObstTran(vert, cent, norm, poly, scal, rota, loca):
	# convert vertices to world space
	d = 0
	while d < len(vert):
		vert[d] = Tran3d__(vert[d], scal, rota, loca)
		d += 1
	d = 0
	while d < len(cent):
		# convert centers to world space
		cent[d] = Tran3d__(cent[d], scal, rota, loca)
		# convert normals to world space
		norm[d] = Quat(norm[d], math.degrees(rota[0]), (1.0, 0.0, 0.0))
		norm[d] = Quat(norm[d], math.degrees(rota[1]), (0.0, 1.0, 0.0))
		norm[d] = Quat(norm[d], math.degrees(rota[2]), (0.0, 0.0, 1.0))
		d += 1
	return vert, cent, norm, poly

def Tran3d__(vect, scal, rota, loca):
	vect = ScalAppl(vect, scal)
	vect = Quat(vect, math.degrees(rota[0]), (1.0, 0.0, 0.0))
	vect = Quat(vect, math.degrees(rota[1]), (0.0, 1.0, 0.0))
	vect = Quat(vect, math.degrees(rota[2]), (0.0, 0.0, 1.0))
	vect = VectAdd_(vect, loca)
	return vect

def ScalAppl(vect, scal):
	retu = []
	a = 0
	while a < len(vect):
		retu.append(vect[a] * scal[a])
		a += 1
	return tuple(retu)

def Quat(poin, angl, axis):
	import math
	p = poin[0]
	q = poin[1]
	r = poin[2]
	t = math.radians(angl)
	t /= 2.0
	a = math.cos(t)
	b = math.sin(t)
	x = axis[0]
	y = axis[1]
	z = axis[2]
	i = r*(2*b*b*x*z+2*a*b*y)+b*b*p*x*x+2*b*b*q*x*y-b*b*p*y*y-b*b*p*z*z-2*a*b*q*z+a*a*p
	j = r*(2*b*b*y*z-2*a*b*x)-b*b*q*x*x+2*b*b*p*x*y+b*b*q*y*y-b*b*q*z*z+2*a*b*p*z+a*a*q
	k = r*(-b*b*x*x-b*b*y*y+b*b*z*z+a*a)+x*(2*b*b*p*z+2*a*b*q)+y*(2*b*b*q*z-2*a*b*p)
	return (i, j, k)

# TODO

def main():
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	if cont.sensors["ray_"].positive:
		pref = "obst"
		# the "pathNumb" variable is set by path.py
		# set "owne" to the owner name is the rays source and the owners position are the same
		# TODO: owne
		roomOwne = scen.objects[owne["owne"]]["pathNumb"]
		obstCoun = owne["obstCoun"]
		orig = owne.worldPosition
		# set target elsewhere
		# if you want to a ray to cast in the direction a camera looks, parent an empty to a camera and extend it to the desired range in the -z direction, then set the empty name in the "targ" property
		dest = scen.objects[owne["targ"]].worldPosition
		hit_ = False
		a = 0
		while a < obstCoun:
			instStri = Pad_(a)
			room = owne[pref + "." + instStri + "." + "room"]
			if room == -1 or room == roomOwne:
				stat = owne[pref + "." + instStri + "." + "stat"]
				boun = owne[pref + "." + instStri + "." + "boun"]
				bounOnly = owne[pref + "." + instStri + "." + "bounOnly"]
				# check if the ray intersects the bounding box
				if boun == True:
					# read bounding box geometry
					vert = []
					cent = []
					norm = []
					poly = []
					end_ = owne[pref + "." + instStri + "." + "verbCoun"]
					for b in range(end_):
						x = owne[pref + "." + instStri + "." + "verb" + "." + Blen.Pad_(b) + "." + "x"]
						y = owne[pref + "." + instStri + "." + "verb" + "." + Blen.Pad_(b) + "." + "y"]
						z = owne[pref + "." + instStri + "." + "verb" + "." + Blen.Pad_(b) + "." + "z"]
						vert.append((x, y, z))
					end_ = owne[pref + "." + instStri + "." + "polbCoun"]
					for b in range(end_):
						x = owne[pref + "." + instStri + "." + "cenb" + "." + Blen.Pad_(b) + "." + "x"]
						y = owne[pref + "." + instStri + "." + "cenb" + "." + Blen.Pad_(b) + "." + "y"]
						z = owne[pref + "." + instStri + "." + "cenb" + "." + Blen.Pad_(b) + "." + "z"]
						cent.append((x, y, z))
					for b in range(end_):
						x = owne[pref + "." + instStri + "." + "norb" + "." + Blen.Pad_(b) + "." + "x"]
						y = owne[pref + "." + instStri + "." + "norb" + "." + Blen.Pad_(b) + "." + "y"]
						z = owne[pref + "." + instStri + "." + "norb" + "." + Blen.Pad_(b) + "." + "z"]
						norm.append((x, y, z))
					for b in range(end_):
						pol_ = []
						instPoly = Pad_(b)
						en__ = owne[pref + "." + instStri + "." + "polbVertCoun" + "." + instPoly]
						for c in range(en__):
							pol_.append(owne[pref + "." + instStri + "." + "polbVert" + "." + instPoly + "." + Pad_(c)])
						poly.append(tuple(pol_))
					# convert to world space
					if stat == False:
						name = owne[pref + "." + instStri + "." + "stat"]
						scal, rota, loca = TranRead(name)
						vert, cent, norm, poly = ObstTran(vert, cent, norm, poly, scal, rota, loca)
					hit_ = Ray_(orig = orig, dest = dest, polyList = poly, vertList = vert, normList = norm, centList = cent, magnTole = 0.0)
					if bounOnly == False:
						# check for intersection with geometry
						if hit_ == True:
							# read geometry
							vert = []
							cent = []
							norm = []
							poly = []
							end_ = owne[pref + "." + instStri + "." + "vertCoun"]
							for b in range(end_):
								x = owne[pref + "." + instStri + "." + "vert" + "." + Blen.Pad_(b) + "." + "x"]
								y = owne[pref + "." + instStri + "." + "vert" + "." + Blen.Pad_(b) + "." + "y"]
								z = owne[pref + "." + instStri + "." + "vert" + "." + Blen.Pad_(b) + "." + "z"]
								vert.append((x, y, z))
							end_ = owne[pref + "." + instStri + "." + "polyCoun"]
							for b in range(end_):
								x = owne[pref + "." + instStri + "." + "cent" + "." + Blen.Pad_(b) + "." + "x"]
								y = owne[pref + "." + instStri + "." + "cent" + "." + Blen.Pad_(b) + "." + "y"]
								z = owne[pref + "." + instStri + "." + "cent" + "." + Blen.Pad_(b) + "." + "z"]
								cent.append((x, y, z))
							for b in range(end_):
								x = owne[pref + "." + instStri + "." + "norm" + "." + Blen.Pad_(b) + "." + "x"]
								y = owne[pref + "." + instStri + "." + "norm" + "." + Blen.Pad_(b) + "." + "y"]
								z = owne[pref + "." + instStri + "." + "norm" + "." + Blen.Pad_(b) + "." + "z"]
								norm.append((x, y, z))
							for b in range(end_):
								pol_ = []
								instPoly = Pad_(b)
								en__ = owne[pref + "." + instStri + "." + "polyVertCoun" + "." + instPoly]
								for c in range(en__):
									pol_.append(owne[pref + "." + instStri + "." + "polyVert" + "." + instPoly + "." + Pad_(c)])
								poly.append(tuple(pol_))
							# convert to world space
							if stat == False:
								vert, cent, norm, poly = ObstTran(vert, cent, norm, poly, scal, rota, loca)
							hit_ = Ray_(orig = orig, dest = dest, polyList = poly, vertList = vert, normList = norm, centList = cent, magnTole = 0.0)
							if hit_ == True:
								break
					else:
						if hit_ == True:
							break
			a += 1
		# hit_ is did the ray hit_ the obstacle, so hit_ is False if the ray reached its target
		# if the target is an empty that represents a ray range, and an obstacle is the target, then the target reaching its destination is a "miss". in that case, the "not" in front of "hit_" can be removed
		owne["ray_"] = not hit_

main()
