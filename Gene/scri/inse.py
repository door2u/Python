
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

# TODO: for now, assume file is png
def NameSpli(fil_):
	fil_ = fil_.split(".")
	fileName = fil_[0]
	if len(fil_) > 1: fileExte = fil_[1]
	else: fileExte = ""
	fil_ = fileName.split("_")
	a = 0
	pref = ""
	while a < len(fil_) and (fil_[a].isnumeric() == False):
		pref += fil_[a]
		a += 1
	numb = fil_[a][0 : 4]
	return fileName, fileExte, pref, numb

def fileMatc(pref, numb):
	paraFile = pref + "_" + numb + "_" + "para"
	blenFile = pref + "_" + numb + ".blend"
	ble1File = pref + "_" + numb + ".blend1"
	return paraFile, blenFile, ble1File

def fileRena(fileList, numbOld_, numbNew_, pref, fileExte, paraFile, blenFile, ble1File, debu = False):
	renaComm = "mv"
	# TODO: test on windows
	if os.name == "nt": renaComm = "RENAME"
	syst = renaComm + " " + pref + "_" + Pyth.Pad_(numbOld_, 4) + "0001." + fileExte + " " + pref + "_" + Pyth.Pad_(numbNew_, 4) + "0001." + fileExte
	if debu: print(syst)
	else: os.system(syst)
	syst = renaComm + " " + paraFile + " " + pref + "_" + Pyth.Pad_(numbNew_, 4) + "_para"
	if debu: print(syst)
	else: os.system(syst)
	syst = renaComm + " " + blenFile + " " + pref + "_" + Pyth.Pad_(numbNew_, 4) + ".blend"
	if debu: print(syst)
	else: os.system(syst)

def main():

	# TODO
	# purge blend1

	debu = True
	debu = False

	import sys
	if len(sys.argv) > 1: 
		fil_ = sys.argv[1]
		fil_ = fil_.split(os.sep)
		fil_ = fil_[len(fil_) - 1]
	else: fil_ = ""

	direCurr = os.path.realpath(os.curdir)
	fileList = os.listdir(direCurr)
	fileList = sorted(fileList)

	# get file numb
	fileName, fileExte, pref, numb = NameSpli(fil_)
	#print(numb)
	# get matching files
	paraFile, blenFile, ble1File = fileMatc(pref, numb)
	# set filenames to last numb
	fil_Name, fil_Exte, pre_, numbFina = NameSpli(fileList[len(fileList) - 2])
	fileRena(fileList, int(numb), int(numbFina) + 1, pref, fileExte, paraFile, blenFile, ble1File, debu = debu)
	# push next lowest file to file numb, all the way down to 0
	num_ = "0000"
	a = 0
	while a < len(fileList) and num_ != numb:
		fil_Name, fil_Exte, pre_, num_ = NameSpli(fileList[a])
		a += 1
	a -= 1
	a -= 1
	if a <= 0:
		pass
	else:
		while a >= 0:
			fil_Name, fil_Exte, pre_, num_ = NameSpli(fileList[a])
			paraFile, blenFile, ble1File = fileMatc(pre_, num_)
			fileRena(fileList, int(num_), int(num_) + 1, pre_, "png", paraFile, blenFile, ble1File, debu = debu)
			a -= 1
			nu__ = num_
			while a >= 0 and nu__ == num_:
				fil_Name, fil_Exte, pre_, nu__ = NameSpli(fileList[a])
				a -= 1
		paraFile, blenFile, ble1File = fileMatc(pref, Pyth.Pad_(int(numbFina) + 1, 4))
		fileRena(fileList, int(numbFina) + 1, 0, pref, "png", paraFile, blenFile, ble1File, debu = debu)

main()

