import importlib.util
import os

path = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Modu" + os.sep + "Modu.py"
spec = importlib.util.spec_from_file_location("Modu", path)
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

def main():

	make = True
	#make = False
	rend = True
	#rend = False
	incr = True
	incr = False

	if make == True:

		fileCoun = 1000

		#scriList = [Gene.Tree()]
		#scriList = [Gene.TreeSimp()]
		#scriList = [Gene.Pose()]
		scriList = [Gene.Anim()]

		Gene.Make(scriList = scriList, fileCoun = fileCoun, incr = incr, rend = rend)

main()

