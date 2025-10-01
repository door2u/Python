
def Pad_(numb):
	retu = ""
	if numb >= 1000:
		thou = int(numb) / 1000
	if numb < 100:
		retu += "0"
	if numb < 10:
		retu += "0"
	retu += str(numb)
	if numb >= 1000:
		retu = str(thou) + retu
	return retu

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

def VectDot_(vec1, vec2):
	retu = 0.0
	a = 0
	while a < len(vec1):
		retu += vec1[a] * vec2[a]
		a += 1
	return retu

def VectMagn(vect):
	return VectDot_(vect, vect) ** 0.5

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

# project vec1 onto vec2
def VectProj(vec1, vec2):
	import math
	tole = 0.0001
	# TODO
	retu = "divide by 0 error"
	deno = VectDot_(vec2, vec2)
	if math.fabs(deno) >= tole:
		nume = VectDot_(vec1, vec2)
		nume /= deno
		nume = VectScal(vec2, nume)
		retu = nume
	return retu

def VectAngl(vec1, vec2, tole = 0.0001, prin = False):
	import math
	retu = 0.0
	deno = VectMagn(vec1) * VectMagn(vec2)
	if math.fabs(deno) >= tole:
		argu = VectDot_(vec1, vec2) / deno
		if math.fabs(argu) <= 1.0 + tole:
			if argu > 1.0:
				argu = 1.0
			if argu < -1.0:
				argu = -1.0
			# !!! returning degrees
			retu = math.degrees(math.acos(argu))
		else:
			if prin == True:
				print("math domain error", argu)
	else:
		if prin == True:
			print("approaching divide by 0", deno)
	return retu

def VectInte2d__(ori1, vec1, ori2, vec2, tole = 0.0001):
	return DistTo__Inte(ori1, VectNorm(vec1), ori2, VectNorm((-vec2[1], vec2[0])), tole = tole)

# get the distance to the point where a vector intersects a plane
# assumes vectDire and norm are normalized
def DistTo__Inte(vectOrig, vectDire, poin, norm, tole = 0.0001):
	import math
	# normal is the direction of the plane
	deno = VectDot_(vectDire, norm)
	# TODO
	dist = "divide by zero error"
	if math.fabs(deno) > tole:
		# point is any point on the plane being checked for distance to ray origin. it could be the face center for the polygon, for example.
		vect = Vect(vectOrig, poin)
		dist = VectDot_(vect, norm) / deno
	return dist

def Faci(dire, posi, targ):
	retu = True
	vect = Vect(posi, targ)
	dot_ = VectDot_(dire, vect)
	if dot_ < 0.0:
		retu = False
	return retu

# TODO
#pathName = "temp.room.main"

def VertLoca(vert, pathName):
	import bge
	#cont = bge.logic.getCurrentController()
	#owne = cont.owner
	scen = bge.logic.getCurrentScene()
	x = scen.objects[pathName + ".vert"]["vert." + str(vert) + ".x"]
	y = scen.objects[pathName + ".vert"]["vert." + str(vert) + ".y"]
	z = scen.objects[pathName + ".vert"]["vert." + str(vert) + ".z"]
	return (x, y, z)

def VertEdge(edge, pathName):
	import bge
	#cont = bge.logic.getCurrentController()
	#owne = cont.owner
	scen = bge.logic.getCurrentScene()
	ver1 = scen.objects[pathName + ".edge"]["edge." + str(edge) + ".0"]
	ver2 = scen.objects[pathName + ".edge"]["edge." + str(edge) + ".1"]
	return ver1, ver2

def Same(edg1, nor1, loca, pathPoly, pol1, pathName):
	retu = False
	ver1, ver2 = VertEdge(edg1, pathName)
	ver1 = VertLoca(ver1, pathName)
	ver2 = VertLoca(ver2, pathName)
	samePoly = False
	if pol1 == pathPoly:
		samePoly = True
	sameSide = Faci(nor1, ver1, loca)
	sam1 = False
	if samePoly == sameSide:
		sam1 = True
	return sam1

def PolyEdge(pathPoly, pathName):
	import bge
	#cont = bge.logic.getCurrentController()
	#owne = cont.owner
	scen = bge.logic.getCurrentScene()
	edg1 = scen.objects[pathName + ".polyEdge"]["polyEdge." + str(pathPoly) + ".0"]
	edg2 = scen.objects[pathName + ".polyEdge"]["polyEdge." + str(pathPoly) + ".1"]
	edg3 = scen.objects[pathName + ".polyEdge"]["polyEdge." + str(pathPoly) + ".2"]
	return edg1, edg2, edg3

def EdgeNorm(edg1, pathName):
	import bge
	#cont = bge.logic.getCurrentController()
	#owne = cont.owner
	scen = bge.logic.getCurrentScene()
	x = scen.objects[pathName + ".edgeNorm"]["edgeNorm." + str(edg1) + ".x"]
	y = scen.objects[pathName + ".edgeNorm"]["edgeNorm." + str(edg1) + ".y"]
	z = scen.objects[pathName + ".edgeNorm"]["edgeNorm." + str(edg1) + ".z"]
	return (x, y, z)

def Norm(norm, pathName):
	import bge
	#cont = bge.logic.getCurrentController()
	#owne = cont.owner
	scen = bge.logic.getCurrentScene()
	x = scen.objects[pathName + ".norm"]["norm." + str(norm) + ".x"]
	y = scen.objects[pathName + ".norm"]["norm." + str(norm) + ".y"]
	z = scen.objects[pathName + ".norm"]["norm." + str(norm) + ".z"]
	return (x, y, z)

def PosiAdju(ori1, loca, edge, pathName):
	import math
	vec1 = Vect(ori1, loca)
	edge = Edge(edge, pathName)
	ori2 = edge[0]
	vec2 = Vect(edge[0], edge[1])
	# get the distance from the start of a vector, in the direction of the vector, to its intersection with an infinite line
	dist = VectInte2d__((ori1[0], ori1[1]), (vec1[0], vec1[1]), (ori2[0], ori2[1]), (vec2[0], vec2[1]))
	if type(dist) == float:
		# TODO
		#pushBack = 0.01
		pushBack = 0.1
		# get intersection
		vectNorm = VectNorm(vec1)
		inte = VectScal(vectNorm, dist)
		inte = VectAdd_(inte, ori1)
		# distance to intersection, minus distance to keep object on path
		# TODO: pushBack is based on object direction, instead of maintaining a constant offset from the boundary edge
		# TODO: why does the object slip through a corner if its being pushed back from the edge
		scal = dist - pushBack
		if scal > 0.0:
			vect = VectScal(vectNorm, scal)
			vect = VectAdd_(vect, ori1)
		else:
			vect = VectScal(vectNorm, -1.0 * pushBack)
			vect = VectAdd_(vect, inte)
		# get the remainder of vec1 past the intersection
		rema = VectMagn(vec1)
		# TODO
		rema = math.fabs(math.fabs(dist - pushBack) - rema)
		rema = VectScal(vectNorm, rema)
		# project remainder of vec1 onto normalized vec2
		rema = VectProj(rema, VectNorm(vec2))
		# world position
		vect = VectAdd_(vect, rema)
	else:
		vect = ori1
	return vect

def Edge(edge, pathName):
	import bge
	#cont = bge.logic.getCurrentController()
	#owne = cont.owner
	scen = bge.logic.getCurrentScene()
	e1v1 = scen.objects[pathName + ".edge"]["edge." + str(edge) + ".0"]
	e1v2 = scen.objects[pathName + ".edge"]["edge." + str(edge) + ".1"]
	e11x = scen.objects[pathName + ".vert"]["vert." + str(e1v1) + ".x"]
	e11y = scen.objects[pathName + ".vert"]["vert." + str(e1v1) + ".y"]
	e11z = scen.objects[pathName + ".vert"]["vert." + str(e1v1) + ".z"]
	e12x = scen.objects[pathName + ".vert"]["vert." + str(e1v2) + ".x"]
	e12y = scen.objects[pathName + ".vert"]["vert." + str(e1v2) + ".y"]
	e12z = scen.objects[pathName + ".vert"]["vert." + str(e1v2) + ".z"]
	return [(e11x, e11y, e11z), (e12x, e12y, e12z)]

# TODO: fix overrides. use method in inpu.py
def Inpu(W, A, S, D, spee):
	import bge
	cont = bge.logic.getCurrentController()
	owne = cont.owner
	updx = False
	updy = False
	move = (0.0, 0.0, 0.0)
	othe = (0.0, 0.0, 0.0)
	if S:
		orie = owne.orientation
		move = VectAdd_(move, VectScal(orie[0], -1.0))
		othe = VectAdd_(move, VectScal(orie[1], -1.0))
		updx = True
	if W:
		orie = owne.orientation
		move = VectAdd_(move, VectScal(orie[0], 1.0))
		othe = VectAdd_(move, VectScal(orie[1], 1.0))
		updx = True
	if A:
		orie = owne.orientation
		move = VectAdd_(move, VectScal(orie[1], 1.0))
		othe = VectAdd_(move, VectScal(orie[0], 1.0))
		#move = VectAdd_(move, VectScal(orie[1], -1.0))
		#othe = VectAdd_(move, VectScal(orie[0], -1.0))
		updy = True
	if D:
		orie = owne.orientation
		move = VectAdd_(move, VectScal(orie[1], -1.0))
		othe = VectAdd_(move, VectScal(orie[0], -1.0))
		#move = VectAdd_(move, VectScal(orie[1], 1.0))
		#othe = VectAdd_(move, VectScal(orie[0], 1.0))
		updy = True
	move = VectScal(VectNorm(move), spee)
	othe = VectNorm(othe)
	return updx, updy, move, othe

def VectCros3d__(vec1, vec2):
	a = vec1[1] * vec2[2] - vec1[2] * vec2[1]
	b = vec1[0] * vec2[2] - vec1[2] * vec2[0]
	c = vec1[0] * vec2[1] - vec1[1] * vec2[0]
	return (a, -b, c)

def main():

	import bge
	import math
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner

	# TODO:
	# if pushBack is too high, rema is 0 and object sticks instead of sliding
	# define pushBack in body
	# check 3d
	# found magn, and other vars, already
	# assumes character is on a level plane with a path polygon. initialize with cast downward and place the character on the surface
	# pass character / allow multiple characters
	# organize with functions
	# var names

	# need to get vertex normals to split planes equally on a 3d path. or maybe it doesnt matter since normals are on the same axis
	# test jumping of traiangles

	#spee = 0.02
	#spee = 0.1
	spee = 0.2
	updx, updy, vec1, othe = Inpu(owne.sensors["W"].positive, owne.sensors["A"].positive, owne.sensors["S"].positive, owne.sensors["D"].positive, spee)
	move = VectNorm(vec1)

	#spee = "spee"
	#spee = owne[spee]
	#angl = owne["dire"]
	#x = spee * math.cos(angl)
	#y = spee * math.sin(angl)
	#owne.worldPosition = (owne.worldPosition[0] + x, owne.worldPosition[1] + y, owne.worldPosition[2])
	#vec1 = (x, y, 0.0)

	updx = True

	checInte = False
	if updx or updy:

		#print(vec1)

		#charName = scen.name + "." + "matt"
		#charName = scen.name + "." + "to__"
		charName = owne.name
		#pathName = scen.name + "." + "room.main"
		pathName = scen.name + "." + owne["pathName"]
		scenObje = scen.name + "." + "scen_obje"

		# TODO: pass
		pushBack = spee / 2.0

		#tole = 0.00000001
		#tole = 0.0000001
		tole = 0.00001

		ori1 = scen.objects[charName].worldPosition
		#print(ori1)
		loca = ori1
		checInte = True
		loca = VectAdd_(ori1, vec1)
		pathPoly = scen.objects[pathName]["pathPoly"]
		#edgeExcl = -1
		edgeExcl = []

		# TODO
		unwa = []
		"""
		#polyExcl = []
		#set_Star = 0
		set_Star = scen.objects[scenObje]["set_Star"]
		set_End_ = 13
		unwa = []
		for b in range(set_Star, set_End_):
			unwaSet_ = b
			star = scen.objects[scenObje]["unwaStar." + str(unwaSet_)]
			end_ = scen.objects[scenObje]["unwaEnd_." + str(unwaSet_)]
			# TODO: maybe make a function to return this to avoid iteration
			for a in range(star, end_):
				unwa.append(scen.objects[scenObje]["unwa." + str(a)])
				#unwa.append(scen.objects[scenObje]["unwa." + Pad_(a)])
		#print(unwa)
		"""

		while checInte:
			checInte = False

			# get the edges for the polygon
			edg1, edg2, edg3 = PolyEdge(pathPoly, pathName)
			# get the normals for the polygon
			nor1 = EdgeNorm(edg1, pathName)
			nor2 = EdgeNorm(edg2, pathName)
			nor3 = EdgeNorm(edg3, pathName)
			# get the polygon the normal points to
			pol1 = scen.objects[pathName + ".edgeNorm"]["edgeNorm." + str(edg1)]
			pol2 = scen.objects[pathName + ".edgeNorm"]["edgeNorm." + str(edg2)]
			pol3 = scen.objects[pathName + ".edgeNorm"]["edgeNorm." + str(edg3)]
			# is the object still within the triangle
			sam1 = Same(edg1, nor1, loca, pathPoly, pol1, pathName)
			sam2 = Same(edg2, nor2, loca, pathPoly, pol2, pathName)
			sam3 = Same(edg3, nor3, loca, pathPoly, pol3, pathName)
			# TODO
			oob_ = False
			# TODO: why does a bounds edge need to be excluded?
			oob_Excl = -1
			sameList = [[sam1, edg1], [sam2, edg2], [sam3, edg3]]
			#print(pathPoly)
			# 2533
			for a in range(len(sameList)):
				#if sameList[a][0] == False and sameList[a][1] != edgeExcl:
				if sameList[a][0] == False and (sameList[a][1] in edgeExcl) == False:
					pol1 = scen.objects[pathName + ".bord"]["bord." + str(sameList[a][1]) + ".0"]
					pol2 = scen.objects[pathName + ".bord"]["bord." + str(sameList[a][1]) + ".1"]
					if pol1 != pathPoly:
						if (pol1 in unwa) == False:
							pathPoly = pol1
							checInte = True
							edgeExcl.append(sameList[a][1])
							break
						else:
							print("adj1")
							loca = PosiAdju(ori1, loca, sameList[a][1], pathName)
							checInte = True
							edgeExcl.append(sameList[a][1])
							break
					# TODO: tracing needs to avoid border edges
					else:
						if pol2 == -1:
							#oob_ = True
							#oob_Excl = sameList[a][1]
							print("adj2")
							loca = PosiAdju(ori1, loca, sameList[a][1], pathName)
							checInte = True
							edgeExcl.append(sameList[a][1])
							break
						else:
							if (pol2 in unwa) == False:
								pathPoly = pol2
								checInte = True
								edgeExcl.append(sameList[a][1])
								break
							else:
								print("adj3")
								loca = PosiAdju(ori1, loca, sameList[a][1], pathName)
								checInte = True
								edgeExcl.append(sameList[a][1])
								break
				if a == len(sameList) - 1:
					edgeExcl = []
					if oob_:
						print("adj4")
						loca = PosiAdju(ori1, loca, sameList[a][1], pathName)
						checInte = True
						edgeExcl.append(oob_Excl)
						#break

		

		#print("x", scen.objects[scen.name + "." + "to__"].worldPosition[0])
		#print("y", scen.objects[scen.name + "." + "to__"].worldPosition[1])

		scen.objects[pathName]["pathPoly"] = pathPoly

		# TODO: pass an option
		# TODO: adjust final position to adhere to speed. try drawing a vector from previous to new and scaling
		grouCast = True
		#grouCast = False
		if grouCast:
			poin = scen.objects[pathName + ".polyVert"]["polyVert." + str(pathPoly) + ".0"]
			poin = VertLoca(poin, pathName)
			norm = Norm(pathPoly, pathName)
			dist = DistTo__Inte(loca, VectScal(norm, -1.0), poin, norm)
			if type(dist) == float:
				dist = VectScal(norm, -1.0 * dist)
				#dist = VectScal(norm, 1.0 * dist)
				loca = VectAdd_(loca, dist)

		scen.objects[charName].worldPosition = loca

		orie = True
		#orie = False
		if orie:

			"""
			orie = owne.orientation
			#print(owne.localOrientation)
			#print(owne.worldOrientation)
			#if owne.localOrientation != owne.worldOrientation:
			#	print("diff")
			#print(orie)
			# get forward vector
			#vect = (0.0, 0.0, 0.0)
			#if updx:
			#	vect = orie[0]
			#if updy:
			#	vect = orie[1]
			### rotate around other vector to "z plane"
			# get z plane
			#	cross other and normal. maybe reverse. vectangl
			norm = Norm(pathPoly, pathName)

			#norm = VectTo__Eule3d__(norm)
			#orie = orie.to_euler()
			#orie = norm

			move = orie[0]
			othe = orie[1]

			zpla = VectCros3d__(norm, move)
			zpla = VectNorm(zpla)

			scen.objects["path.z"].worldPosition = VectAdd_(loca, zpla)

			angl = VectAngl(zpla, othe)
			othe = Quat(othe, -angl, move)
			z = orie[2]
			z = Quat(z, -angl, move)

			angl = VectAngl(z, norm)
			z = Quat(z, angl, othe)
			move = Quat(move, angl, othe)

			#scen.objects["path.x"].worldPosition = VectAdd_(loca, move)
			#scen.objects["path.y"].worldPosition = VectAdd_(loca, y)
			#scen.objects["path.z"].worldPosition = VectAdd_(loca, z)

			#if updx:
			#	x = move
			#	y = othe
			#else:
			#	x = othe
			#	y = move

			x = move
			y = othe

			#scen.objects["path.x"].worldPosition = VectAdd_(loca, x)
			#scen.objects["path.y"].worldPosition = VectAdd_(loca, y)
			#scen.objects["path.z"].worldPosition = VectAdd_(loca, z)
			#scen.objects["path.x"].worldPosition = VectAdd_(loca, orie[0])
			#scen.objects["path.y"].worldPosition = VectAdd_(loca, orie[1])
			#scen.objects["path.z"].worldPosition = VectAdd_(loca, orie[2])

			owne.orientation = ((x[0], y[0], z[0]), (x[1], y[1], z[1]), (x[2], y[2], z[2]))
			#owne.orientation = ((orie[0][0], orie[1][0], orie[2][0]), (orie[0][1], orie[1][1], orie[2][1]), (orie[0][2], orie[1][2], orie[2][2]))
			"""

			"""
			zpla = VectCros3d__(othe, norm)
			scen.objects["path.z"].worldPosition = VectAdd_(loca, zpla)
			z = orie[2]
			angl = VectAngl(zpla, z)
			###
			z = Quat(z, angl, othe)
			move = Quat(move, angl, othe)
			### rotate around forward vector to pathpoly
			angl = VectAngl(z, norm)
			z = Quat(z, angl, move)
			othe = Quat(othe, angl, move)
			# TODO: depends on which way the object is moving
			x = move
			y = othe

			#scen.objects["path.x"].worldPosition = VectAdd_(loca, x)
			#scen.objects["path.y"].worldPosition = VectAdd_(loca, y)

			owne.orientation = ((x[0], y[0], z[0]), (x[1], y[1], z[1]), (x[2], y[2], z[2]))
			"""

			#z = Norm(pathPoly, pathName)
			#angl = VectAngl(z, 
			#if updx:
			#	# rotate around y

			#if updy:
			#	# rotate around x


			# figure 8
			"""
			orie = owne.orientation
			x = orie[0]
			z = Norm(pathPoly, pathName)
			y = VectCros3d__(z, x)
			y = VectNorm(y)
			scen.objects["path.y"].worldPosition = VectAdd_(loca, y)
			x = VectCros3d__(y, z)
			x = VectNorm(x)
			scen.objects["path.x"].worldPosition = VectAdd_(loca, x)
			scen.objects["path.z"].worldPosition = VectAdd_(loca, z)
			owne.orientation = ((x[0], y[0], z[0]), (x[1], y[1], z[1]), (x[2], y[2], z[2]))
			"""






			import mathutils

			norm = Norm(pathPoly, pathName)
			"""
			norm = (0.0, 0.0, 1.0)
			x = scen.objects["path.Plane"]["x"]
			y = scen.objects["path.Plane"]["y"]
			z = scen.objects["path.Plane"]["z"]
			rotn = (x, y, z)
			rotn = mathutils.Euler(rotn, 'XYZ')
			scen.objects["path.Plane"].orientation = rotn.to_matrix()
			norm = VectRota3d__(norm, rotn)
			"""

			#print(norm)
			
			vert = scen.objects[pathName + ".polyVert"]["polyVert." + str(pathPoly) + ".0"]
			vert = VertLoca(vert, pathName)
			#vert = loca
			# TODO: get world position
			#vert = VectRota3d__(vert, rotn)

			#print(pathPoly)

			orie = owne.orientation
			#orie = owne.worldOrientation
			#forw = orie[0]
			#othe = orie[1]
			#z___ = orie[2]
			#forw = (orie[0][0], orie[0][1], orie[0][2])
			#othe = (-orie[1][0], -orie[1][1], -orie[1][2])
			#forw = (orie[1][0], orie[1][1], orie[1][2])
			#othe = (orie[0][0], orie[0][1], orie[0][2])
			#z___ = (orie[2][0], orie[2][1], orie[2][2])
			#forw = (1.0, 0.0, 0.0)
			#othe = (0.0, 1.0, 0.0)
			#z___ = (0.0, 0.0, 1.0)
			#print(forw)
			orie = orie.to_euler()
			rota = (math.degrees(orie[0]), math.degrees(orie[1]), math.degrees(orie[2]))
			forw = EuleTo__Vect3d__(rota, vect = (1.0, 0.0, 0.0))
			othe = EuleTo__Vect3d__(rota, vect = (0.0, 1.0, 0.0))
			z___ = EuleTo__Vect3d__(rota, vect = (0.0, 0.0, 1.0))

			print(norm)
			print(z___)
			#print(VectDot_(VectNorm(norm), VectNorm(z___)))
			#print(VectDot_(norm, (orie[0][2], orie[1][2], orie[2][2])))
			#print(loca)

			to__ = norm
			dire = othe
			#dire = (0.0, 1.0, 0.0)
			axis = z___
			#axis = (0.0, 0.0, 1.0)
			dot_ = othe
			#dot_ = (0.0, 1.0, 0.0)
			#to_1 = norm
			#dire = othe
			#axi1 = z___
			#dot1 = othe
			#forw = (1.0, 0.0, 0.0)
			angy = PlanAngl(loca, to__, dire, axis, dot_, vert, debu = True)
			#print(angy)
			floy = type(angy) == float
			if floy:
				#eule = mathutils.Euler((0.0, math.radians(angy), 0.0), 'XYZ')
				#eule.rotate(orie)
				#orie = eule
				#orie = orie.to_matrix()
				#owne.orientation = orie
				#forw = Quat(forw, angy, othe)
				#z___ = Quat(z___, angy, othe)
				#forw = VectRota3d__(forw, (0.0, angy, 0.0))
				#z___ = VectRota3d__(z___, (0.0, angy, 0.0))
				#forw = VectNorm(forw)
				#z___ = VectNorm(z___)
				#RotaUpda(forw, othe, z___)
				#orie = owne.orientation
				#orie = orie.to_euler()
				eule = mathutils.Euler((0.0, math.radians(angy), 0.0), 'XYZ')
				orie.rotate(eule)
				owne.orientation = orie.to_matrix()
				rota = (math.degrees(orie[0]), math.degrees(orie[1]), math.degrees(orie[2]))
				forw = EuleTo__Vect3d__(rota, vect = (1.0, 0.0, 0.0))
				othe = EuleTo__Vect3d__(rota, vect = (0.0, 1.0, 0.0))
				z___ = EuleTo__Vect3d__(rota, vect = (0.0, 0.0, 1.0))

			#forw = orie[0]
			#othe = orie[1]
			#z___ = orie[2]
			

			to__ = othe
			#to__ = (0.0, 1.0, 0.0)
			dire = norm
			axis = othe
			#axis = (0.0, 1.0, 0.0)
			dot_ = forw
			#dot_ = 
			angx = PlanAngl(loca, to__, dire, axis, dot_, vert)
			flox = type(angx) == float
			if flox:
				#if flox and floy:
				#eule = mathutils.Euler((math.radians(angx), 0.0, 0.0), 'XYZ')
				#eule.rotate(orie)
				#orie = eule
				#orie = orie.to_matrix()
				#owne.orientation = orie
				#othe = Quat(othe, angx, forw)
				#z___ = Quat(z___, angx, forw)
				#othe = VectRota3d__(othe, (angx, 0.0, 0.0))
				#z___ = VectRota3d__(z___, (angx, 0.0, 0.0))
				#othe = VectNorm(othe)
				#z___ = VectNorm(z___)
				#print(flox, floy)
				#if flox and floy:
				#RotaUpda(forw, othe, z___)
				eule = mathutils.Euler((math.radians(angx), 0.0, 0.0), 'XYZ')
				orie.rotate(eule)
				owne.orientation = orie.to_matrix()

def RotaUpda(forw, othe, z___):
	# TODO: could pass owne
	import bge
	cont = bge.logic.getCurrentController()
	owne = cont.owner
	x = forw
	y = othe
	z = z___
	#z = VectNorm(z)
	x = VectCros3d__(y, z)
	#x = VectCros3d__(z, y)
	x = VectNorm(x)
	#y = VectCros3d__(x, z)
	#y = VectCros3d__(z, x)
	#y = VectNorm(y)
	owne.orientation = ((x[0], y[0], z[0]), (x[1], y[1], z[1]), (x[2], y[2], z[2]))
	#owne.orientation = (x, y, z)

def PlanAngl(loca, to__, dire, axis, dot_, vert, debu = False):
	angl = -1
	vectOrig = VectAdd_(loca, to__)
	# TODO: distance point to plane
	
	# TODO: does changing loca to vert actually do anything
	#print(VectMagn(dire))
	#dire = VectNorm(dire)
	#if debu:
	#	#print(vectOrig)
	#	print(dire)
	dist = DistTo__Inte(vectOrig, dire, loca, dire)
	#dist = DistTo__Inte(vectOrig, dire, vert, dire)
	#dist = DistPoinTo__Plan(vectOrig, loca, dire)
	#dist = DistPoinTo__Plan(vectOrig, vert, dire)
	#if debu:
	#	print(dist)
	# TODO: dist is same
	if type(dist) == float:
		poin = VectScal(dire, dist)
		poin = VectAdd_(poin, vectOrig)
		vect = Vect(loca, poin)
		angl = VectAngl(vect, axis)
		cros = VectCros3d__(vect, axis)
		if VectDot_(cros, dot_) >= 0.0:
			angl *= -1.0
			#if debu:
			#	print("-")
		#else:
		#	if debu:
		#		print("+")
	return angl

def EuleTo__Vect3d__(eule, vect = (1.0, 0.0, 0.0)):
	vect = Quat(vect, eule[0], (1.0, 0.0, 0.0))
	vect = Quat(vect, eule[1], (0.0, 1.0, 0.0))
	vect = Quat(vect, eule[2], (0.0, 0.0, 1.0))
	return vect

# distance from a point to the nearest point on an infinite plane. planPoin can be any point as long as it lies on the surface of the plane (like the face center)
def DistPoinTo__Plan(poin, planPoin, norm):
	import math
	tole = 0.0001
	deno = VectDot_(norm, norm)
	dist = 0.0
	chec = False
	if math.fabs(deno) >= tole:
		vect = Vect(planPoin, poin)
		vect = VectProj(vect, norm)
		dist = VectMagn(vect)
		chec = True
	# TODO
	if chec == False:
		dist = "divide by zero error"
	return dist

# rotate a 2 dimensional vector
def VectRota2d__(vect, rota, axis):
	import math
	if axis == None:
		axis = 0
	mat1 = []
	if axis == 0 or axis == 2:
		mat1.append([math.cos(math.radians(rota)), -math.sin(math.radians(rota))])
		mat1.append([math.sin(math.radians(rota)), math.cos(math.radians(rota))])
	if axis == 1:
		mat1.append([math.cos(math.radians(rota)), math.sin(math.radians(rota))])
		mat1.append([-math.sin(math.radians(rota)), math.cos(math.radians(rota))])
	mat2 = []
	mat2.append([vect[0]])
	mat2.append([vect[1]])
	retu = Matr(mat1, mat2)
	return retu

# rotate a 3d vector
def VectRota3d__(vect, eule):
	vecx = VectRota2d__((vect[1], vect[2]), eule[0], 0) # y z
	vecy = VectRota2d__((vect[0], vecx[1][0]), eule[1], 1) # x z
	vecz = VectRota2d__((vecy[0][0], vecx[0][0]), eule[2], 2) # x y
	return (vecz[0][0], vecz[1][0], vecy[1][0])

# copy rows to columns
def MatrDeco(matr):
	retu = []
	leng = -1
	if len(matr) > 0:
		leng = len(matr[0])
	for a in range(leng):
		row_ = []
		for b in range(len(matr)):
			row_.append(matr[b][a])
		retu.append(row_)
	return retu

def Matr(mat1 = [], mat2 = [], deco = True):
	retu = []
	leng = -1
	if len(mat1) > 0:
		leng = len(mat1[0])
	# check if the column count of the first matrix matches the row count of the second matrix
	if len(mat2) == leng:
		if deco == True:
			mat2 = MatrDeco(mat2)
		for a in range(len(mat1)):
			row_ = []
			for b in range(len(mat2)):
				vec1 = mat1[a]
				vec2 = mat2[b]
				row_.append(VectDot_(vec1, vec2))
			retu.append(row_)
	else:
		print("matrix sizes do not match")
	return retu

# convert a vector to an euler rotation
# assumes object was originally oriented towards +x
# TODO: too many cases
def VectTo__Eule3d__(vect):
	import math
	tole = 0.0001
	x = 0.0
	z = math.atan2(vect[1], vect[0])
	if math.fabs(vect[0]) >= tole:
		z2 = math.cos(z)
		if math.fabs(z2) >= tole:
			x2 = vect[0] / z2
		else:
			x2 = vect[0]
		y = math.atan2(-vect[2], x2)
	else:
		# TODO: when did this get messed up
		#if math.fabs(vect[1]) >= 0.0:
		if vect[1] > 0.0:
			y = math.atan2(-vect[2], vect[1])
		else:
			y = math.atan2(-vect[2], -vect[1])
	return VectDegr((x, y, z))

# rotate poin angl degrees around axis
# 3d point
# angle in degrees
# normalized axis
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

main()
