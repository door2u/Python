
#def Path(posi, orie, pathPoly, moveVect, moveMagn, spee, offs, use_GrouCast, use_PosiAdju, use_Orie, use_OrieCons, scen, math, mathutils, Math, pathObje, path_geom):
def Path(posi, orie, pathPoly, moveVect, moveMagn, spee, offs, use_GrouCast, use_PosiAdju, use_Orie, use_OrieCons, scen, math, mathutils, Math, pathObje):

	coll = Math.VectAdd_(posi, Math.VectScal(moveVect, offs))
	vect = Math.VectScal(moveVect, spee * moveMagn)
	loca = Math.VectAdd_(coll, vect)
	unwaList = Unwa(scen)
	edgeExcl = []
	checInte = True
	while checInte:
		checInte = False
		#use_Prop = scen.objects[scen.name + "." + pathObje]["use_Prop"]
		#if use_Prop:
		#	edg1, edg2, edg3, ver1, ver2, ver3, nor1, nor2, nor3, pol1, pol2, pol3 = PolyGeom(scen, pathPoly, pathObje)
		#	refeList = [EdgeRefeList(scen, edg1, pathObje), EdgeRefeList(scen, edg2, pathObje), EdgeRefeList(scen, edg3, pathObje)]
		#	vert = VertList(scen, PolyList(scen, pathPoly, pathObje), pathObje)
		#	norm = NormList(scen, pathPoly, pathObje)
		#else:

		# TODO: where should this import be
		from scri import path_geom
		#import path_geom
		#vertList, edgeList, polyList, normList, polyEdgeList, edgeNormList, edgeRefeList, edgeBordList = path_geom.PathGeom()
		#edg1, edg2, edg3, ver1, ver2, ver3, nor1, nor2, nor3, pol1, pol2, pol3 = PolyGeomScri(pathPoly, polyEdgeList, vertList, edgeList, edgeNormList, edgeRefeList)
		edg1, edg2, edg3 = path_geom.PolyEdgeList(pathPoly)
		ed_1 = path_geom.EdgeList(edg1)
		ed_2 = path_geom.EdgeList(edg2)
		ed_3 = path_geom.EdgeList(edg3)
		#ver1, ver2, ver3 = path_geom.PolyList(pathPoly)
		ver1 = path_geom.VertList(ed_1[0])
		ver2 = path_geom.VertList(ed_2[0])
		ver3 = path_geom.VertList(ed_3[0])
		nor1 = path_geom.EdgeNormList(edg1)
		nor2 = path_geom.EdgeNormList(edg2)
		nor3 = path_geom.EdgeNormList(edg3)
		pol1 = path_geom.EdgeRefeList(edg1)
		pol2 = path_geom.EdgeRefeList(edg2)
		pol3 = path_geom.EdgeRefeList(edg3)

		#refeList = [edgeRefeList[edg1], edgeRefeList[edg2], edgeRefeList[edg3]]
		#vert = vertList[polyList[pathPoly][0]]
		#norm = normList[pathPoly]
		refeList = [pol1, pol2, pol3]
		#vert = path_geom.VertList(ver1)
		vert = ver1
		norm = path_geom.NormList(pathPoly)
		#print(ver1, nor1, loca)
		sam1 = Same(ver1, nor1, loca, pathPoly, pol1, Math)
		sam2 = Same(ver2, nor2, loca, pathPoly, pol2, Math)
		sam3 = Same(ver3, nor3, loca, pathPoly, pol3, Math)
		sameList = [sam1, sam2, sam3]
		edg_List = [edg1, edg2, edg3]
		ver_List = [ver1, ver2, ver3]
		nor_List = [nor1, nor2, nor3]
		for a in range(len(sameList)):
			if sameList[a] == False and (edg_List[a] in edgeExcl) == False:
				updaPathPoly = -1
				callPosiAdju = False
				#if use_Prop:
				#	pol1, pol2 = EdgeBordList(scen, edg_List[a], pathObje)
				#else:
				#pol1 = edgeBordList[edg_List[a]][0]
				#pol2 = edgeBordList[edg_List[a]][1]
				pol1 = path_geom.EdgeBordList(edg_List[a])
				pol2 = pol1[1]
				pol1 = pol1[0]
				if pol1 != pathPoly:
					if (pol1 in unwaList) == False: updaPathPoly = pol1
					else: callPosiAdju = True
				else:
					if pol2 == -1: callPosiAdju = True
					else:
						if (pol2 in unwaList) == False: updaPathPoly = pol2
						else: callPosiAdju = True
				if updaPathPoly != -1:
					pathPoly = updaPathPoly
					checInte = True
					edgeExcl.append(edg_List[a])
					break
				if use_PosiAdju and callPosiAdju:
					loca = PosiAdju(ver_List[a], nor_List[a], loca, pathPoly != refeList[a], Math)
					checInte = True
					edgeExcl.append(edg_List[a])
					break
			if a == len(sameList) - 1: edgeExcl = []
	loca = Math.VectAdd_(loca, Math.VectScal(moveVect, -1.0 * offs))
	if use_GrouCast: loca = GrouCast(vert, norm, loca, pathPoly, Math)
	if use_Orie: orie = Orie(vert, norm, orie, loca, Math, use_OrieCons, math, mathutils)
	return loca, orie, pathPoly

def Same(vert, norm, loca, pathPoly, poly, Math):
	samePoly = False
	if poly == pathPoly: samePoly = True
	sameSide = Math.Faci(norm, vert, loca)
	same = False
	if samePoly == sameSide: same = True
	return same

def PosiAdju(vert, norm, loca, inve, Math):
	if inve: norm = Math.VectScal(norm, -1.0)
	faci = Math.Faci(norm, vert, loca)
	if faci == False:
		dist = Math.DistPoinPlan(loca, vert, norm)
		loca = Math.VectAdd_(loca, Math.VectScal(norm, dist))
	return loca

def Unwa(scen):
	unwaList = []
	if scen.name + ".unwa" in scen.objects:
		set_Coun = scen.objects[scen.name + ".unwa"]["set_Coun"]
		for a in range(set_Coun):
			unwa = scen.objects[scen.name + ".unwa"]["unwa." + str(a)]
			if unwa:
				coun = scen.objects[scen.name + ".unwa"]["unwaCoun." + str(a)]
				for b in range(coun):
					unwaList.append(scen.objects[scen.name + ".unwa"]["unwa." + str(a) + "." + str(b)])
	return unwaList

def GrouCast(poin, norm, loca, pathPoly, Math):
	dist = Math.DistVectPlan(loca, Math.VectScal(norm, -1.0), poin, norm)
	if type(dist) == float:
		dist = Math.VectScal(norm, -1.0 * dist)
		loca = Math.VectAdd_(loca, dist)
	return loca

def Orie(vert, norm, orie, loca, Math, use_OrieCons, math, mathutils):
	forw = (orie[0][0], orie[1][0], orie[2][0])
	othe = (orie[0][1], orie[1][1], orie[2][1])
	z___ = (orie[0][2], orie[1][2], orie[2][2])
	orie = orie.to_euler()
	variList = []
	variList.append([loca, othe, norm, forw, vert, z___, 'X'])
	variList.append([loca, forw, norm, othe, vert, z___, 'Y'])
	angl = Math.PlanAngl(variList[0][0], variList[0][1], variList[0][2], variList[0][3], variList[0][4], variList[0][5])
	if type(angl) == float:
		orie.rotate_axis(variList[0][6], math.radians(angl))
		matr = orie.to_matrix()
		forw = (matr[0][0], matr[1][0], matr[2][0])
		othe = (matr[0][1], matr[1][1], matr[2][1])
		z___ = (matr[0][2], matr[1][2], matr[2][2])
	angl = Math.PlanAngl(variList[1][0], variList[1][1], variList[1][2], variList[1][3], variList[1][4], variList[1][5])
	if type(angl) == float:
		if use_OrieCons:
			axis = (math.cos(orie[2] + math.pi / 2.0), math.sin(orie[2] + math.pi / 2.0), 0.0)
			quat = mathutils.Quaternion(axis, math.radians(angl))
			orie.rotate(quat)
		else:
			orie.rotate_axis(variList[1][6], math.radians(angl))
	return orie.to_matrix()

"""
def PolyGeomScri(pathPoly, polyEdgeList, vertList, edgeList, edgeNormList, edgeRefeList):
	edge = polyEdgeList[pathPoly]
	edg1 = edge[0]
	edg2 = edge[1]
	edg3 = edge[2]
	ver1 = vertList[edgeList[edg1][0]]
	ver2 = vertList[edgeList[edg2][0]]
	ver3 = vertList[edgeList[edg3][0]]
	nor1 = edgeNormList[edg1]
	nor2 = edgeNormList[edg2]
	nor3 = edgeNormList[edg3]
	pol1 = edgeRefeList[edg1]
	pol2 = edgeRefeList[edg2]
	pol3 = edgeRefeList[edg3]
	return edg1, edg2, edg3, ver1, ver2, ver3, nor1, nor2, nor3, pol1, pol2, pol3

def PolyGeom(scen, pathPoly, pathObje):
	edg1, edg2, edg3 = PolyEdgeList(scen, pathPoly, pathObje)
	ver1 = EdgeList(scen, edg1, pathObje)
	ver2 = EdgeList(scen, edg2, pathObje)
	ver3 = EdgeList(scen, edg3, pathObje)
	ver1 = VertList(scen, ver1, pathObje)
	ver2 = VertList(scen, ver2, pathObje)
	ver3 = VertList(scen, ver3, pathObje)
	nor1 = EdgeNormList(scen, edg1, pathObje)
	nor2 = EdgeNormList(scen, edg2, pathObje)
	nor3 = EdgeNormList(scen, edg3, pathObje)
	pol1 = EdgeRefeList(scen, edg1, pathObje)
	pol2 = EdgeRefeList(scen, edg2, pathObje)
	pol3 = EdgeRefeList(scen, edg3, pathObje)
	return edg1, edg2, edg3, ver1, ver2, ver3, nor1, nor2, nor3, pol1, pol2, pol3

def VertList(scen, vert, pathObje):
	x = scen.objects[scen.name + "." + pathObje + ".vertList"]["vert." + str(vert) + ".x"]
	y = scen.objects[scen.name + "." + pathObje + ".vertList"]["vert." + str(vert) + ".y"]
	z = scen.objects[scen.name + "." + pathObje + ".vertList"]["vert." + str(vert) + ".z"]
	return (x, y, z)

def EdgeList(scen, edge, pathObje, inde = 0):
	return scen.objects[scen.name + "." + pathObje + ".edgeList"]["edge." + str(edge) + "." + str(inde)]

def PolyList(scen, poly, pathObje, inde = 0):
	return scen.objects[scen.name + "." + pathObje + ".polyList"]["poly." + str(poly) + "." + str(inde)]

def NormList(scen, norm, pathObje):
	x = scen.objects[scen.name + "." + pathObje + ".normList"]["norm." + str(norm) + ".x"]
	y = scen.objects[scen.name + "." + pathObje + ".normList"]["norm." + str(norm) + ".y"]
	z = scen.objects[scen.name + "." + pathObje + ".normList"]["norm." + str(norm) + ".z"]
	return (x, y, z)

def PolyEdgeList(scen, pathPoly, pathObje):
	edg1 = scen.objects[scen.name + "." + pathObje + ".polyEdgeList"]["polyEdge." + str(pathPoly) + ".0"]
	edg2 = scen.objects[scen.name + "." + pathObje + ".polyEdgeList"]["polyEdge." + str(pathPoly) + ".1"]
	edg3 = scen.objects[scen.name + "." + pathObje + ".polyEdgeList"]["polyEdge." + str(pathPoly) + ".2"]
	return edg1, edg2, edg3

def EdgeNormList(scen, edg1, pathObje):
	x = scen.objects[scen.name + "." + pathObje + ".edgeNormList"]["edgeNorm." + str(edg1) + ".x"]
	y = scen.objects[scen.name + "." + pathObje + ".edgeNormList"]["edgeNorm." + str(edg1) + ".y"]
	z = scen.objects[scen.name + "." + pathObje + ".edgeNormList"]["edgeNorm." + str(edg1) + ".z"]
	return (x, y, z)

def EdgeRefeList(scen, edge, pathObje):
	return scen.objects[scen.name + "." + pathObje + ".edgeRefeList"]["edgeRefe." + str(edge)]

def EdgeBordList(scen, edge, pathObje):
	pol1 = scen.objects[scen.name + "." + pathObje + ".edgeBordList"]["edgeBord." + str(edge) + ".0"]
	pol2 = scen.objects[scen.name + "." + pathObje + ".edgeBordList"]["edgeBord." + str(edge) + ".1"]
	return pol1, pol2
"""

