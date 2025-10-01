
def main():
	import bge
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	rang = 10.0
	obje, poin, norm = owne.rayCast((owne.worldPosition[0], owne.worldPosition[1], owne.worldPosition[2] - rang), owne, rang, "path", 1, 1)
	# set path to -1000 to make it unwalkable temporarily, then set it to something else to make it walkable
	if poin != None and obje["path"] != -1000:
		owne["pathChec"] = True
		name = owne.name
		name = name.split(".")
		name = name[len(name) - 1]
		if name == "000":
			numb = obje.name
			numb = numb.split(".")
			if len(numb) > 1:
				numb = numb[len(numb) - 1]
				if numb.isnumeric():
					numb = int(numb)
					owne["pathNumb"] = numb
	else:
		owne["pathChec"] = False

main()
