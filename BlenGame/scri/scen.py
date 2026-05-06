
def main():

	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	# TODO: forward imports
	import Math
	import game
	import move
	import path
	import cycl
	import look_x
	import look_y
	import orie
	import acti
	import Pyth
	import GameNode
	import anim
	import came
	import came_path
	#import path_geom
	variDict = game.VariDict(scen, owne.name)
	vari = bge.logic.globalDict
	vari["objeDele"] = []
	for a in range(variDict["charCoun"]):
		char = variDict["char." + game.Pad_(a)]
		if char:
			charName = scen.name + "." + variDict["charName." + game.Pad_(a)]
			obje = scen.objects[charName]
			variList = obje.getPropertyNames()
			charCont = False
			if "cont" in variList:
				charCont = obje["cont"]
			lookY___Angl = 90.0
			if charCont:
				variDict = game.Inpu(variDict, owne, owne.sensors['W'], owne.sensors['A'], owne.sensors['S'], owne.sensors['D'], owne.sensors['W_T'], owne.sensors['A_T'], owne.sensors['S_T'], owne.sensors['D_T'], owne.sensors["LEFT_SHIFT"], owne.sensors["RIGHTAXIS"], owne.sensors["UPAXIS"], owne.sensors["joysAxisRigh"], owne.sensors["joysAxisUp__"], owne.sensors["look"], bge, math)
				look = True
				#look = False
				if look:
					pathObje = "wall.path"
					obj_ = scen.objects[scen.name + "." + "matt.trac.posi"]
					loca, orientat, pathPoly = came_path.Path(obj_.worldPosition, obj_.orientation, obj_["pathPoly"], (0.0, 0.0, 0.0), 0.0, 0.0, 0.0, False, True, False, False, scen, math, mathutils, Math, pathObje)
					obj_["pathPoly"] = pathPoly
					lookX___Angl, lookX___Acti, lookY___Angl, lookY___Acti = Look(charName, "look", "came", variDict, scen, look_x, look_y, math, mathutils)
					lookName = "look"
					orientat = MatrEule(scen.objects[charName + "." + lookName], mathutils, glob = False)
					lookX___Angl, lookX___Acti = look_x.LookX___(scen.objects[charName + "." + lookName], orientat[2], variDict["axisRigh"], math, mathutils)
					scen.objects[charName + "." + lookName].orientation = EuleMatr((orientat[0], orientat[1], math.radians(lookX___Angl)), mathutils)
					came.main(scen.objects[scen.name + ".came"], owne.sensors["WHEELUP"].positive, owne.sensors["WHEELDOWN"].positive, loca)
				else:
					lookX___Angl = 0.0
					lookY___Angl = 0.0
				moveVect, upda = move.MoveVect(variDict["inpuDire"], variDict["inpuMagn"], obje.orientation, lookX___Angl, math, Math)
				if upda and ("acti" in variList):
					angl = orie.Orie(variDict["inpuDire"], lookX___Angl)
					orientat = MatrEule(scen.objects[obje.name + "." + "body"], mathutils, glob = False)
					if scen.objects[charName]["weap"] != 2:
						scen.objects[obje.name + "." + "body"].orientation = EuleMatr((orientat[0], orientat[1], math.radians(angl)), mathutils)
				if ("acti" in variList):
					actiValu = acti.Acti(obje[obje["acti"]], upda)
					obje[obje["acti"]] = actiValu
			else:
				pass
			if upda:
				if ("acti" in variList):
					acti = obje["acti"]
					spee = obje[acti + "Spee"]
				else:
					spee = 0.4
				pathObje = "room.main"
				offs = obje["offs"]
				#loca, orientat, pathPolyOffs = path.Path(obje.worldPosition, obje.orientation, obje["pathPolyOffs"], moveVect, variDict["inpuMagn"], spee, offs, False, True, False, False, scen, math, mathutils, Math, pathObje, path_geom)
				#loca, orientat, pathPoly = path.Path(loca, orientat, obje["pathPoly"], moveVect, variDict["inpuMagn"], 0.0, 0.0, True, False, False, False, scen, math, mathutils, Math, pathObje, path_geom)
				loca, orientat, pathPolyOffs = path.Path(obje.worldPosition, obje.orientation, obje["pathPolyOffs"], moveVect, variDict["inpuMagn"], spee, offs, False, True, False, False, scen, math, mathutils, Math, pathObje)
				loca, orientat, pathPoly = path.Path(loca, orientat, obje["pathPoly"], moveVect, variDict["inpuMagn"], 0.0, 0.0, True, False, False, False, scen, math, mathutils, Math, pathObje)
				obje.worldPosition = loca
				obje.orientation = orientat
				obje["pathPolyOffs"] = pathPolyOffs
				obje["pathPoly"] = pathPoly
			if ("acti" in variList):
				cycl.main(obje, Math)
				vari = anim.main(vari, cont, scen, scen.objects[charName], math, Math, mathutils, lookY___Angl, owne.sensors["one_"].positive, owne.sensors["two_"].positive, owne.sensors["thre"].positive, owne.sensors["clic"].positive, owne.sensors["clii"].positive)
	if ("variList" in vari) == False:
		vari["variList"] = [[ "connList", []]]
	if ("variList" in vari) == True and len(vari["variList"]) > 0:
		while len(vari["variList"]) > 0:
			vari[vari["variList"][0][0]] = vari["variList"][0][1]
			vari["variList"].pop(0)
	import ray_
	if owne.sensors["clii"].positive:
		vari = ray_.main(vari, GameNode, game, Math, bge, math, mathutils, scen)
	# TODO: if impoComp
	"""
	import temp
	variDict["phas"], vari = temp.main(bge, math, cont, scen, owne, Math, game, Pyth, vari, GameNode, mathutils)
	if len(vari["objeDele"]) > 0:
		inde = scen.objects["temp.matt"]["arroInde"]
		if inde != -1:
			for a in range(len(vari["objeDele"])):
				if vari["objeDele"][a] > inde:
					inde -= 1
			scen.objects["temp.matt"]["arroInde"] = inde
	"""
	variDict["clic"] = False
	variDict["clir"] = False
	for key_ in variDict:
		upda = True
		key_Pref = key_.split(".")
		exclList = ["from", "conn", "to__", "obje", "objeType", "posx", "posy", "posxInde", "posyInde", "indx", "indy", "compObje", "inde", "connCoun", "connCut_", "connCounCurr"]
		if len(key_Pref) > 0:
			if key_Pref[0] in exclList: upda = False
		if upda: owne[key_] = variDict[key_]

def Look(charName, lookName, cameName, variDict, scen, look_x, look_y, math, mathutils):
	orientat = MatrEule(scen.objects[scen.name + "." + cameName], mathutils, glob = False)
	lookY___Angl, lookY___Acti = look_y.LookY___(scen.objects[scen.name + "." + cameName], orientat[0], variDict["axisUp__"], math, mathutils)
	scen.objects[scen.name + "." + cameName].orientation = EuleMatr((math.radians(lookY___Angl), orientat[1], orientat[2]), mathutils)
	return 0.0, False, lookY___Angl, lookY___Acti

def MatrEule(obje, mathutils, glob = True):
	if glob: orientat = mathutils.Matrix(obje.orientation)
	else: orientat = mathutils.Matrix(obje.localOrientation)
	return orientat.to_euler()

def EuleMatr(eule, mathutils):
	eule = mathutils.Euler(eule, 'XYZ')
	return eule.to_matrix()

main()

