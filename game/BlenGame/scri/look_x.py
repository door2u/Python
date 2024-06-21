def main():
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	if owne["lookX___"] == True:
		axisRigh = scen.objects[scen.name + "." + "scen_obje"]["axisRigh"]
		if axisRigh != 0.0:
			# maximum mouse change. to prevent jumping that occurs when the mouse first enters a window
			lookX___Cut_ = owne["lookX___Cut_"]
			if math.fabs(axisRigh) <= lookX___Cut_:
				orie = mathutils.Matrix(owne.localOrientation)
				orie = orie.to_euler()
				angl = orie[2] - axisRigh
				#print("angl", angl)
				eule = mathutils.Euler((orie[0], orie[1], angl), 'XYZ')
				owne["lookX___Angl"] = angl
				owne.localOrientation = eule.to_matrix()
				owne["lookX___Acti"] = True
main()
