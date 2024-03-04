
def VectDot_(vec1, vec2):
	retu = 0.0
	a = 0
	while a < len(vec1):
		retu += vec1[a] * vec2[a]
		a += 1
	return retu

def Vect(vec1, vec2):
	retu = []
	a = 0
	while a < len(vec1):
		retu.append(vec2[a] - vec1[a])
		a += 1
	return tuple(retu)

def Faci(dvec, posi, targ):
	retu = True
	# get a line from source to targert
	vect = Vect(posi, targ)
	dot_ = VectDot_(dvec, vect)
	if dot_ < 0.0:
		retu = False
	return retu

def main():
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	rang = 5.0
	obje, poin, norm = owne.rayCast(scen.objects[owne.name + ".d"], owne, rang, "path", 0, 1)
	if poin != None:
		grou = owne["grou"]
		if grou == True:
			name = owne["owne"]
			char = scen.objects[scen.name + "." + "came"]["view"]
			if name == char:
				# TODO
				stai = obje["stai"]
				if stai == True:
					eule = mathutils.Matrix(scen.objects[scen.name + "." + name + ".look"].worldOrientation)
					eule = eule.to_euler()
					# z angle
					z = eule[2]
					# x / y vector
					x = math.cos(z)
					y = math.sin(z)
					posi = scen.objects[scen.name + "." + name].worldPosition
					numb = obje["numb"]
					targ = scen.objects[scen.name + "." + "stai.bott." + numb].worldPosition
					faci = Faci((x, y, 0.0), (posi[0], posi[1], 0.0), (targ[0], targ[1], 0.0))
					if faci == True:
						scen.objects[scen.name + "." + "came"]["firsTemp"] = True
					else:
						scen.objects[scen.name + "." + "came"]["firsTemp"] = False
				else:
					scen.objects[scen.name + "." + "came"]["firsTemp"] = False
			owne["grouHeig"] = poin[2]
		else:
			scen.objects[scen.name + "." + "came"]["firsTemp"] = False

main()
