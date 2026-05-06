
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

def main(own_, u, d, move):
	import bge
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	char = own_["char"]
	if char != -1:
		charName = scen.objects[scen.name + "." + "scen_obje"]["charName." + Pad_(char)]
		tracPosi = scen.name + "." + charName + "." + "trac" + "." + "posi"
		tracNear = scen.name + "." + charName + "." + "trac" + "." + "near"
		tracDist = scen.name + "." + charName + "." + "trac" + "." + "dist"
		tracFirs = scen.name + "." + charName + "." + "trac" + "." + "firs"
		near = own_["near"]
		steps = 1.0 / 0.2
		zoom = own_["zoom"]
		dest = scen.objects[tracPosi].worldPosition
		spee = own_["cameSpee"]
		cameZoom = own_["cameZoom"]
		curr = own_["cameCurr"]
		if move == False:
			cameZoom = True
			if curr > 2:
				steps = 1.0
				curr -= 1
		if zoom == True:
			maxi = own_["cameMaxi"]
			if u:
				cameZoom = True
				curr -= 1
				if curr < 2:
					curr = 0
					steps = 1.0
					spee = 10.0
			if d:
				cameZoom = True
				curr += 1
				if curr > maxi:
					curr = maxi
				if curr == 1:
					curr = 2
					steps = 1.0
					spee = 10.0
			if cameZoom == True:
				if curr != maxi and curr != 0 and curr != 1:
					vect = Vect(scen.objects[tracNear].worldPosition, scen.objects[tracDist].worldPosition)
					vec2 = VectScal(vect, (curr - 1) / (maxi - 1))
					vec2 = VectAdd_(vec2, scen.objects[tracNear].worldPosition)
					own_["cameDestX___"] = vec2[0]
					own_["cameDestY___"] = vec2[1]
					own_["cameDestZ___"] = vec2[2]
				else:
					if curr == maxi:
						own_["cameDestX___"] = scen.objects[tracDist].worldPosition[0]
						own_["cameDestY___"] = scen.objects[tracDist].worldPosition[1]
						own_["cameDestZ___"] = scen.objects[tracDist].worldPosition[2]
					if curr == 1:
						own_["cameDestX___"] = scen.objects[tracNear].worldPosition[0]
						own_["cameDestY___"] = scen.objects[tracNear].worldPosition[1]
						own_["cameDestZ___"] = scen.objects[tracNear].worldPosition[2]
					if curr == 0:
						own_["cameDestX___"] = scen.objects[tracFirs].worldPosition[0]
						own_["cameDestY___"] = scen.objects[tracFirs].worldPosition[1]
						own_["cameDestZ___"] = scen.objects[tracFirs].worldPosition[2]
				dest = (own_["cameDestX___"], own_["cameDestY___"], own_["cameDestZ___"])
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
				own_["cameZoom"] = cameZoom
		own_["cameCurr"] = curr

