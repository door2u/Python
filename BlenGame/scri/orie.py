
def Orie(dire, lookX___Angl, dest = False):
	dire += lookX___Angl
	return dire

def OrieDest():
	dire = math.atan2(dify, difx)
	orie = mathutils.Matrix(owne.worldOrientation)
	orie = orie.to_euler()
	comp = orie[2]
	tole = 0.01
	if math.fabs(comp - dire) > tole:
		rotaSpee = owne["rotaSpee"]
		x___ = math.cos(comp)
		y___ = math.sin(comp)
		diff = VectAngl((x___, y___), (vect[0], vect[1]))
		diff *= rotaSpee
		if AnglGrea(math.atan2(y___, x___), math.atan2(vect[1], vect[0])) == False:
			orie = mathutils.Euler((orie[0], orie[1], orie[2] + diff), 'XYZ')
		else:
			orie = mathutils.Euler((orie[0], orie[1], orie[2] - diff), 'XYZ')
		owne.worldOrientation = orie.to_matrix()

