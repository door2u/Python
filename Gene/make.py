import importlib.util
import os

path = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Pyth" + os.sep + "Modu" + os.sep + "Modu.py"
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
	exe_ = True
	#exe_ = False
	rendImag = True
	rendImag = False
	rendVide = True
	rendVide = False
	framCoun = 30
	incr = True
	#incr = False

	if make:

		#fileCoun = -1
		fileCoun = 100
		#fileCoun = 1000

		#scriList = [Gene.Tree()]
		#scriList = [Gene.TreeDist()]
		# TODO
		# have to make a jog_.blend file. try specifying a directory or something
		# rename
		#scriList = [Gene.Jog_()]
		#scriList = [Gene.Anim()]
		#scriList = [Gene.Face()]
		#scriList = [Gene.Mes1(blen = "")]
		#scriList = [Gene.Mes2(blen = "")]
		#scriList = [Gene.Mesh()]
		scriList = [Gene.Jog_Game()]
		Gene.Make(scriList = scriList, fileCoun = fileCoun, incr = incr, rendImag = rendImag, rendVide = rendVide, framCoun = framCoun, exe_ = exe_)

	sort = True
	sort = False
	if sort:

		dire = "/home/christopher/Documents/prog/gene/coni/libr/"
		direList = "/home/christopher/Documents/prog/Pyth/Gene/list/leng"

		Gene.Sort(dire, direList, name = "bran")

main()

