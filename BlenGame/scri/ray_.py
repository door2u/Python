
def main(vari, GameNode, game, Math, bge, math, mathutils, scen):
	vect_fr = None
	orie = scen.objects[scen.name + "." + "came"].worldOrientation
	posi = scen.objects[scen.name + "." + "came"].worldPosition
	vect_to = Math.VectScal((orie[0][2], orie[1][2], orie[2][2]), -1.0)
	vect_to = Math.VectAdd_(posi, vect_to)
	dist = 50.0
	prop = "targ"
	obje, poin, norm = scen.objects[scen.name + "." + "came"].rayCast(vect_to, vect_fr, dist, prop, 1, 1)
	if poin != None:
		hit_ = obje.name
		scen.objects[hit_]["hit_"] = True
		scenObje = scen.name + "." + "scen_obje"
		fro_ = False
		to__ = False
		thru = False
		if "in__" in scen.objects[hit_].getPropertyNames():
			to__ = True
		if "out_" in scen.objects[hit_].getPropertyNames():
			fro_ = True
		if "thr1" in scen.objects[hit_].getPropertyNames():
			thru = True
		if "thr2" in scen.objects[hit_].getPropertyNames():
			thru = True
		if "thr3" in scen.objects[hit_].getPropertyNames():
			thru = True
		if fro_ or to__ or thru:
			con_ = scen.objects[scenObje]["conn"]
			if con_ == "":
				scen.objects[scenObje]["conn"] = hit_
				if to__:
					scen.objects[scenObje]["from"] = False
				if fro_:
					scen.objects[scenObje]["from"] = True
			else:
				connCoun = scen.objects[scenObje]["connCoun"]
				fr__ = scen.objects[scenObje]["from"]
				if to__ or (thru and fr__):
					vari = GameNode.ConnAdd_(con_, hit_, connCoun, game, Math, vari, bge, math, mathutils, scen)
				if fro_ or (thru and fr__ == False):
					vari = GameNode.ConnAdd_(hit_, con_, connCoun, game, Math, vari, bge, math, mathutils, scen)
				scen.objects[scenObje]["conn"] = ""
	return vari

