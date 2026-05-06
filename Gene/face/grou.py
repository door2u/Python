def main():

	import bge
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner

	if owne.sensors['Mouse'].positive:
		over = owne["over"]
		if over:
			name = owne.name
			name = name.split(".")
			numb = name[2]
			kind = name[3]
			#print(kind)
			if owne.visible:
				if kind == "f":
					scen.objects[scen.name + "." + "scen_obje"]["set_." + numb] = True
					scen.objects[scen.name + "." + "grou." + numb + ".t"].visible = True
				else:
					scen.objects[scen.name + "." + "scen_obje"]["set_." + numb] = False
					scen.objects[scen.name + "." + "grou." + numb + ".f"].visible = True
				owne.visible = False

main()
