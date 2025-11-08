def Pad_(numb):
	retu = ""
	if numb < 100:
		retu += "0"
	if numb < 10:
		retu += "0"
	retu += str(numb)
	return retu

def Pad4(numb):
	retu = ""
	if numb < 1000:
		retu += "0"
	if numb < 100:
		retu += "0"
	if numb < 10:
		retu += "0"
	retu += str(numb)
	return retu

def LineTo__File(line, filePath, mode = "w"):
	fileObje = open(filePath, mode = mode)
	writ = ""
	a = 0
	while a < len(line):
		writ += line[a] + "\n"
		a += 1
	fileObje.write(writ)
	fileObje.close()

def main():

	import bge
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner

	writ = True
	#writ = False
	coun = owne["coun"]
	curr = owne["curr"]
	grouCoun = owne["grouCoun"]
	if owne.sensors['ente'].positive:
		if curr >= 0:
			para = []
			for a in range(grouCoun):
				if owne['set_.' + Pad_(a)]:
					para.append('True')
				else:
					para.append('False')
			if writ:
				# TODO: mode is write
				LineTo__File(para, "/home/christopher/Documents/prog/gene/face/face_out_/face_" + Pad4(curr) + "_para", mode = "w")
		for a in range(grouCoun):
			owne['set_.' + Pad_(a)] = False
			scen.objects[scen.name + "." + 'grou.' + Pad_(a) + '.f'].visible = True
			scen.objects[scen.name + "." + 'grou.' + Pad_(a) + '.t'].visible = False
		curr += 1
		if curr < coun:
			if curr > 0:
				scen.objects[scen.name + "." + "plan." + Pad4(curr - 1)].visible = False
			scen.objects[scen.name + "." + "plan." + Pad4(curr)].visible = True
	owne["curr"] = curr

main()
