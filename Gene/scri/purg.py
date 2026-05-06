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

	#dire = Modu.geneCont + "mesh" + os.sep + "out_" + os.sep
	dire = "/home/christopher/Documents/prog/gene/mesh/kept/00/"
	tras = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "trash" + os.sep

	fileList = os.listdir(dire)
	for a in range(len(fileList)):
		keep = True
		chec = False
		name = ""
		fil_ = fileList[a]
		fil_ = fil_.split(".")
		if len(fil_) > 1:
			if fil_[1] == "blend":
				name = fil_[0]
				chec = True
			elif fil_[1] == "blend1":
				keep = False
		else:
			fil_ = fil_[0].split("_")
			if len(fil_) > 1:
				if fil_[len(fil_) - 1] == "para":
					for b in range(len(fil_) - 1):
						name += fil_[b]
						if b < len(fil_) - 2:
							name += "_"
					chec = True
		if keep == False or (chec and name != ""):
			if keep == False or (name + "0001.png" in fileList) == False:
				print("moving", fileList[a], "to", tras)
				if os.name == 'nt':
					# TODO: not tested
					syst = "MOVE " + dire + fileList[a] + " " + tras
					os.system(syst)
				else:
					syst = "mv " + dire + fileList[a] + " " + tras
					os.system(syst)
			else:
				print("keeping", fileList[a])

main()

