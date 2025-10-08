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
			numb = name[1]
			kind = name[2]
			#print(kind)
			if owne.visible:
				if kind == "f":
					scen.objects["scen"]["set_." + numb] = True
					scen.objects["grou." + numb + ".t"].visible = True
				else:
					scen.objects["scen"]["set_." + numb] = False
					scen.objects["grou." + numb + ".f"].visible = True
				owne.visible = False

main()
