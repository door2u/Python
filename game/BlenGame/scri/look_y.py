def main():
	import bge
	import math
	import mathutils
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	if owne["lookY___"] == True:
		axisUp__ = scen.objects[scen.name + "." + "scen_obje"]["axisUp__"]
		if axisUp__ != 0.0:
			lookY___Cut_ = owne["lookY___Cut_"]
			if math.fabs(axisUp__) <= lookY___Cut_:
				orie = mathutils.Matrix(owne.localOrientation)
				orie = orie.to_euler()
				newx = orie[0] - axisUp__
				lookY___Limi = owne["lookY___Limi"]
				if lookY___Limi == True:
					lookY___LimiInve = owne["lookY___LimiInve"]
					lookY___LimiUppe = owne["lookY___LimiUppe"]
					lookY___LimiLowe = owne["lookY___LimiLowe"]
					if lookY___LimiInve == True:
						# high limit
						if newx < 0.0:
							lookY___LimiLowe = -math.pi / 2.0
						# low limit
						else:
							lookY___LimiUppe = math.pi / 2.0
					# high limit
					if newx > lookY___LimiUppe:
						newx = lookY___LimiUppe
					# low limit
					if newx < lookY___LimiLowe:
						newx = lookY___LimiLowe
				eule = mathutils.Euler((newx, orie[1], orie[2]), 'XYZ')
				owne.localOrientation = eule.to_matrix()
			#bge.logic.mouse.position = (0.5, 0.5)
			owne["lookY___Acti"] = True
main()
