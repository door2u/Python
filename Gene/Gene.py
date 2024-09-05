def PythLink(Pyth = None):
	return Pyth
def MathLink(Math = None):
	return Math
def BlenLink(Blen = None):
	return Blen
def BlenCommLink(blenComm = None):
	return blenComm
def BlenDireLink(blenDire = None):
	return blenDire
def GeneDireLink(geneDire = None):
	return geneDire

def ScriList():
	return sorted(['tree', 'tree_simp'])

class TreeSimp():
	import os
	pref = "tree_simp"
	dire = "flor" + os.sep + "tree_simp" + os.sep
	scri = "flor" + os.sep + "tree_simp" + os.sep + "tree_simp"

class Tree():
	import os
	pref = "tree"
	dire = "flor" + os.sep + "tree" + os.sep
	scri = "flor" + os.sep + "tree" + os.sep + "tree"

class Pose():
	import os
	pref = "pose"
	dire = "pose" + os.sep
	scri = "pose" + os.sep + "pose"

class Anim():
	import os
	pref = "anim"
	dire = "anim" + os.sep
	scri = "anim" + os.sep + "anim"

def Make(scriList = [], fileCoun = 1, incr = True, rend = True):

	# TODO:
	# make flag files: out / pick / kept. purg and merg
	# reset a and count if pick flag is set
	# put all parent files where theyre supposed to be
	# record current nudg file

	import os
	import random

	Pyth = PythLink()
	Blen = BlenLink()
	blenComm = BlenCommLink()
	blenDire = BlenDireLink()
	geneDire = GeneDireLink()

	# cap at 9999
	if fileCoun > 9999:
		fileCoun = 9999

	# read iden file
	iden = {}
	line = Pyth.FileTo__Line("iden")
	for a in range(len(line)):
		lin_ = line[a]
		lin_ = lin_.split("=")
		lin_[0] = lin_[0].strip()
		iden.update({lin_[0]:int(lin_[1])})

	# the number of blend files in library
	tota = {}
	# the number of files in "out_" folder
	coun = {}
	tota.update(iden)
	coun.update(iden)
	for entr in tota:
		tota[entr] = 0
		coun[entr] = 0

	a = 0
	while a < fileCoun or fileCoun == -2:

		for e in range(len(scriList)):

			pref = scriList[e].pref
			scri = scriList[e].scri
			dire = scriList[e].dire

			# out directory where created files are stored
			out_ = dire + "out_" + os.sep

			# padded number of this file (a)
			numb = Pyth.Pad_(coun[pref], 4)

			# clear the param file
			paraOut_ = out_ + pref + "_" + numb + "_para"
			paraLine = ["iden"]
			paraLine.append(str(iden[pref]))
			paraLine.append("<class 'int'>")
			Pyth.LineTo__File(paraLine, paraOut_)

			# read random min/max range for different parameters
			para = Pyth.FileTo__Line(dire + pref + "_para")
			# TODO: how should this really be done
			if para != ['']:
				para = Pyth.LineTo__Dict(para)
				para = ParaInit(para)

			# new file path
			vari = {"path":out_ + pref + "_" + numb + ".blend"}
			vari = Pyth.DictTo__Vari(vari)

			# other vars
			varsExtr = "numb = \"" + numb + "\"\n"
			varsExtr += "pref = \"" + pref + "\"\n"
			varsExtr += "dire = \"" + dire + "\"\n"
			varsExtr = Pyth.EscaPath(varsExtr)

			# start a new command-line string to pass to the console
			syst = blenComm + " -b " + dire + pref + ".blend"
			# convert script file to a string
			fileObje = open(scri + ".py", mode = "r")
			stri = fileObje.read()
			fileObje.close()
			vari = {"path":out_ + pref + "_" + numb + ".blend"}
			vari = Pyth.DictTo__Vari(vari)
			vari = Pyth.EscaPath(vari)
			vari += "\n"
			stri += vari
			fileObje = open("scri" + os.sep + "save.py", mode = "r")
			stri += fileObje.read()
			fileObje.close()
			vari = "para = "
			vari += str(para)
			vari += "\n"
			stri = vari + stri
			scriStri = varsExtr + stri
			fileObje = open("tempScri.py", mode = "w")
			fileObje.write(scriStri)
			fileObje.close()
			syst += " --python tempScri.py"

			# execute the command-line string
			os.system(syst)

			# render
			if rend == True:
				imag = geneDire + dire + "out_" + os.sep + pref + "_" + numb
				syst = Blen.Batc(dire + "out_" + os.sep + pref + "_" + numb + ".blend")
				#syst += Blen.Rend(imag)
				syst += Blen.RendVide(imag, 24)
				os.system(syst)

			iden[pref] += 1
			coun[pref] += 1

		a += 1

	# rewrite iden file which tracks the count of the total files of each type created (for all history)
	if incr == True:
		ite_ = iden.keys()
		line = []
		for key_ in ite_:
			line.append(key_ + " = " + str(iden[key_]))
		Pyth.LineTo__File(line, "iden")

def ParaInit(para):
	Pyth = PythLink()
	Math = MathLink()
	retu = {}
	for key_ in para:
		pref = key_
		pref = pref.split("_")
		entr = ""
		for a in range(len(pref) - 1):
			entr += pref[a]
			if a < len(pref) - 2:
				entr += "_"
		if key_ == entr + "_mini":
			valu = Math.RandRang(para[entr + "_mini"], para[entr + "_maxi"])
			if type(para[entr + "_mini"]) == float:
				valu = float(valu)
			if type(para[entr + "_mini"]) == int:
				valu = int(valu)
			retu.update({entr:valu})
	return retu

def ParaWrit(para = {}, dire = "", exte = True):
	Pyth = PythLink()
	writ = []
	for entr in para:
		writ.append(entr)
		writ.append(str(para[entr]))
		if type(para[entr]) == float:
			writ.append("<class 'float'>")
		if type(para[entr]) == int:
			writ.append("<class 'int'>")
		if type(para[entr]) == str:
			writ.append("<class 'str'>")
	if exte == False:
		for line in writ:
			print(line)
	else:
		Pyth.LineTo__File(writ, dire, mode = "a")
