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

	ignoList = ["face", "para"]
	dire = Modu.geneCont + "face" + os.sep + "out_" + os.sep

	fileList = os.listdir(dire)
	fileList = sorted(fileList)
	prev = ""
	new_ = 0
	for a in range(len(fileList)):
		numb = ""
		fil_ = fileList[a]
		fil_ = fil_.split(".")
		if len(fil_) > 1 and fil_[1] == "png":
			fil_ = fil_[0]
			fil_ = fil_[0 : len(fil_) - 4]
		else:
			fil_ = fil_[0]
		fil_ = fil_.split("_")
		for b in range(len(fil_)):
			if (fil_[b] in ignoList) == False and fil_[b].isnumeric():
				numb = fil_[b]
				break
		if numb != "":
			if prev == "":
				prev = numb
			if numb != prev:
				prev = numb
				new_ += 1
			if int(numb) != new_:
				name = ""
				fil_ = fileList[a]
				for b in range(len(fil_) - len(numb)):
					if fil_[b : b + len(numb)] == numb:
						fil_ = fil_[0 : b] + Pyth.Pad_(new_, 4) + fil_[b + len(numb) + 0 : len(fil_)]
						break
				print("renaming", dire + fileList[a], "to", dire + fil_)
				if os.name == 'nt':
					# TODO: not tested
					syst = "RENAME " + dire + fileList[a] + " " + dire + fil_
					os.system(syst)
				else:
					syst = "mv " + dire + fileList[a] + " " + dire + fil_
					os.system(syst)

main()

