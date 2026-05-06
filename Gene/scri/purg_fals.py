import importlib.util
import os

spec = importlib.util.spec_from_file_location("Modu", os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Pyth" + os.sep + "Modu" + os.sep + "Modu.py")
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

def main():
	dire = "/home/christopher/Documents/prog/gene/face/out_/"
	fileList = os.listdir(dire)
	fileList = sorted(fileList)
	for fil_ in fileList:
		fileName = fil_.split("_")
		if len(fileName) > 0 and fileName[len(fileName) - 1] == "para":
			pref = fileName[0]
			numb = fileName[1]
			line = Pyth.FileTo__Line(dire + fil_)
			purg = True
			for lin_ in line:
				if lin_ != "False":
					purg = False
			if purg:
				comm = "rm " + dire + fil_
				os.system(comm)
				blen = pref + "_" + numb + ".blend"
				if blen in fileList:
					comm = "rm " + dire + blen
					os.system(comm)
				imag = pref + "_" + numb + "0001.png"
				if imag in fileList:
					comm = "rm " + dire + imag
					os.system(comm)

main()

