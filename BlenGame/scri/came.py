
def Pad_(numb):
	retu = ""
	if numb < 100:
		retu += "0"
	if numb < 10:
		retu += "0"
	retu += str(numb)
	return retu

def VectMagn(vect):
	retu = 0.0
	for dime in vect:
		retu += dime * dime
	return retu ** 0.5

def Vect(vec1, vec2):
	retu = []
	a = 0
	while a < len(vec1):
		retu.append(vec2[a] - vec1[a])
		a += 1
	return tuple(retu)

def VectScal(vect, scal):
	retu = []
	a = 0
	while a < len(vect):
		retu.append(vect[a] * scal)
		a += 1
	return tuple(retu)

def VectAdd_(vec1, vec2):
	retu = []
	a = 0
	while a < len(vec1):
		retu.append(vec1[a] + vec2[a])
		a += 1
	return tuple(retu)

# TODO
def main():
	import bge
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	# TODO: in (ground cast?) set camecurr to 0
	#firs = owne["firs"]
	char = owne["char"]
	if char != -1:
		charName = scen.objects[scen.name + "." + "scen_obje"]["charName." + Pad_(char)]
		tracPosi = scen.name + "." + charName + "." + "trac" + "." + "posi"
		tracNear = scen.name + "." + charName + "." + "trac" + "." + "near"
		# distant
		tracDist = scen.name + "." + charName + "." + "trac" + "." + "dist"
		tracFirs = scen.name + "." + charName + "." + "trac" + "." + "firs"
		near = owne["near"]
		steps = 1.0 / owne["scroSens"]
		#move = owne["cameMove"]
		# TODO: var names
		zoom = owne["zoom"]
		dest = scen.objects[tracPosi].worldPosition
		spee = owne["cameSpee"]
		cameZoom = owne["cameZoom"]
		if zoom == True:
			curr = owne["cameCurr"]
			maxi = owne["cameMaxi"]
			if owne.sensors["WHEELUP"].positive:
				cameZoom = True
				curr -= 1
				if curr < 0:
					curr = 0
			if owne.sensors["WHEELDOWN"].positive:
				cameZoom = True
				curr += 1
				if curr > maxi:
					curr = maxi
			if cameZoom == True:
				owne["cameCurr"] = curr
				if curr != maxi and curr != 0 and curr != 1:
					vect = Vect(scen.objects[tracNear].worldPosition, scen.objects[tracDist].worldPosition)
					vec2 = VectScal(vect, (curr - 1) / (maxi - 1))
					vec2 = VectAdd_(vec2, scen.objects[tracNear].worldPosition)
					owne["cameDestX___"] = vec2[0]
					owne["cameDestY___"] = vec2[1]
					owne["cameDestZ___"] = vec2[2]
				else:
					if curr == maxi:
						owne["cameDestX___"] = scen.objects[tracDist].worldPosition[0]
						owne["cameDestY___"] = scen.objects[tracDist].worldPosition[1]
						owne["cameDestZ___"] = scen.objects[tracDist].worldPosition[2]
					if curr == 1:
						owne["cameDestX___"] = scen.objects[tracNear].worldPosition[0]
						owne["cameDestY___"] = scen.objects[tracNear].worldPosition[1]
						owne["cameDestZ___"] = scen.objects[tracNear].worldPosition[2]
					if curr == 0:
						owne["cameDestX___"] = scen.objects[tracFirs].worldPosition[0]
						owne["cameDestY___"] = scen.objects[tracFirs].worldPosition[1]
						owne["cameDestZ___"] = scen.objects[tracFirs].worldPosition[2]
				# TODO: make sure this gets set on load (set cameZoom to true)
				dest = (owne["cameDestX___"], owne["cameDestY___"], owne["cameDestZ___"])
				diff = Vect(scen.objects[tracPosi].worldPosition, dest)
				incr = 1.0 / steps * spee
				magn = VectMagn(diff)
				if incr < magn:
					diff = VectScal(diff, 1.0 / magn)
					diff = VectScal(diff, incr)
					scen.objects[tracPosi].worldPosition = (scen.objects[tracPosi].worldPosition[0] + diff[0], scen.objects[tracPosi].worldPosition[1] + diff[1], scen.objects[tracPosi].worldPosition[2] + diff[2])
				else:
					scen.objects[tracPosi].worldPosition = dest
					cameZoom = False
				owne.worldPosition = scen.objects[tracPosi].worldPosition
				owne["cameZoom"] = cameZoom
		tab = owne["tab_"]
		if tab == True:
			if owne.sensors["tab_"].positive:
				if char != -1:
					scen.objects[scen.name + "." + charName]["cont"] = False
					char += 1
					charCoun = scen.objects[scen.name + "." + "scen_obje"]["charCoun"]
					if char == charCoun:
						char = 0
					charName = scen.objects[scen.name + "." + "scen_obje"]["charName." + Pad_(char)]
					scen.objects[scen.name + "." + charName]["cont"] = True
					owne.removeParent()
					owne.worldPosition = scen.objects[scen.name + "." + charName + "." + "trac.posi"]
					# TODO: rotation?
					# parent
					owne.setParent(scen.objects[scen.name + "." + charName + "." + "look"])

main()
