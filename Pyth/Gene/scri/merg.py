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

	# TODO
	# almost the same as flat.py

	ignoList = ["face", "para"]
	# merge dir1 into dir2
	# ! assumes dir2 is flat
	dir1 = Modu.geneCont + "face" + os.sep + "dir1" + os.sep
	dir2 = Modu.geneCont + "face" + os.sep + "dir2" + os.sep
	# TODO: code an empty check
	# WARNING: might be required for windows. MAKE SURE THERE ARE NO CONFLICTS
	temp = os.path.expanduser("~") + os.sep + "Documents" + os.sep + "trash" + os.sep

	fileList = os.listdir(dir1)
	fileList = sorted(fileList)
	prev = ""
	new_ = Gene.FileCoun(dir2)
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
				print("moving", dir1 + fileList[a], "to", dir2 + fil_)
				if os.name == 'nt':
					# TODO: not tested
					# move
					syst = "MOVE " + dir1 + fileList[a] + " " + temp + fileList[a]
					os.system(syst)
					# rename
					syst = "RENAME " + temp + fileList[a] + " " + temp + fil_
					os.system(syst)
					# move
					syst = "MOVE " + temp + fil_ + " " + dir2 + fil_
					os.system(syst)
				else:
					syst = "mv " + dir1 + fileList[a] + " " + dir2 + fil_
					os.system(syst)

main()

