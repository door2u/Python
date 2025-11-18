
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
def GeneContLink(geneCont = None):
	return geneCont
def HeadLink(Head = None):
	return Head

def ScriList():
	return sorted(['tree', 'tree_simp'])

class TreeSimp():
	import os
	name = "tree_simp"
	dire = "flor" + os.sep + "tree_simp" + os.sep
	scri = "flor" + os.sep + "tree_simp" + os.sep + "tree_simp"

class Pose():
	import os
	name = "pose"
	dire = "pose" + os.sep
	scri = "pose" + os.sep + "pose"

class Anim():
	import os
	name = "anim"
	dire = "anim" + os.sep
	scri = "anim" + os.sep + "anim"

class Jog_():
	import os
	name = "jog_"
	dire = "jog_" + os.sep
	scri = "jog_" + os.sep + "jog_"

# TODO: link class. try using self
"""
class Bran():
	import os
	geneCont = GeneContLink()
	name = "bran"
	#dire = "flor" + os.sep + "bran" + os.sep
	dire = geneCont + "flor" + os.sep + "bran" + os.sep
	scri = "flor" + os.sep + "bran" + os.sep + "bran"
"""

def Bran():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "bran"
	retu.dire = "flor" + os.sep + "bran" + os.sep
	retu.libr = geneCont + "flor" + os.sep + "bran" + os.sep
	retu.scri = "flor" + os.sep + "bran" + os.sep + "bran"
	return retu

def Coni():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "coni"
	retu.dire = "flor" + os.sep + "coni" + os.sep
	retu.libr = geneCont + "flor" + os.sep + "coni" + os.sep
	retu.scri = "flor" + os.sep + "coni" + os.sep + "coni"
	return retu

def Fern():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "fern"
	retu.dire = "flor" + os.sep + "fern" + os.sep
	retu.libr = geneCont + "flor" + os.sep + "fern" + os.sep
	retu.scri = "flor" + os.sep + "fern" + os.sep + "fern"
	return retu

def Flow():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "flow"
	retu.dire = "flor" + os.sep + "flow" + os.sep
	retu.libr = geneCont + "flor" + os.sep + "flow" + os.sep
	retu.scri = "flor" + os.sep + "flow" + os.sep + "flow"
	return retu

# TODO: include mode here
def Hard():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "hard"
	retu.dire = "hard" + os.sep
	retu.libr = geneCont + "hard" + os.sep
	retu.scri = "hard" + os.sep + "hard"
	retu.pref = "hard"
	return retu

def Para(paraOut_, dire, name, iden):
	Pyth = PythLink()
	paraLine = []
	paraLine.append("<class 'int'>")
	paraLine.append("iden")
	paraLine.append(str(iden))
	Pyth.LineTo__File(paraLine, paraOut_)
	# read random min/max range for different parameters
	para = Pyth.FileTo__Line(dire + name + "_para")
	if para != ['']:
		para = Pyth.LineTo__Dict(para)
		para = ParaInit(para)
	return para

# mode of operation for the generator library
# 0 - standard mode / scratch mode. a script is run repeatedly, each time producing a new outputted set of files in the out_ directory. (a set of files [might] include a blend file, a rendered image, and a text file storing data and attributes)
# 1 - library mode. a new file is not created from scratch. instead, a file is chosen (usually at random) from a library and modified.
# 2 - propagate mode. a file is chosen from the out_ directory. like library mode, but diverges rapidly since newly created files may be chosen to be modified again.
# 3 - single file mode. a script is run repeatedly on the same file
class Scri():
	mode = 0
	name = ""
	dire = ""
	scri = ""
	geneCont = ""
	pref = ""
	out_ = ""
	vari = {}
	syst = ""
	save = True
	def Init(self):
		import os
		blenComm = BlenCommLink()
		self.scri = self.dire + self.name
		self.syst = blenComm + " -b " + self.dire + self.name + ".blend" + " --python tempScri.py"
		# create new files from scratch
		if self.mode == 0:
			self.out_ = self.geneCont + "out_" + os.sep
			self.vari.update({"dire" : self.geneCont})
			self.vari.update({"name" : self.name})
		# read a file to be modified from a library
		elif self.mode == 1:
			self.out_ = self.geneCont
			#if self.pref != "": self.out_ += self.pref + "_"
			self.out_ = Conc(self.out_, self.pref)
			self.out_ += "out_" + os.sep
			self.vari.update({"dire" : self.geneCont})
			self.vari.update({"name" : self.name})
		# read files to be modified from the out_ directory
		elif self.mode == 2:
			self.out_ = self.geneCont + "out_" + os.sep
			self.vari.update({"dire" : self.geneCont})
			self.vari.update({"name" : self.name})
		# apply a script to a single file
		elif self.mode == 3:
			self.syst = blenComm + " -b " + self.geneCont + "libr" + os.sep + self.name + ".blend" + " --python tempScri.py"
			save = False
		# TODO?
		return self

def Tree():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "tree"
	retu.dire = "flor" + os.sep + "tree" + os.sep
	retu.geneCont = geneCont + "flor" + os.sep + "tree" + os.sep
	retu.Init()
	return retu

def TreeDist():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.mode = 3
	retu.name = "tree_dist"
	retu.dire = "flor" + os.sep + "tree_dist" + os.sep
	retu.scri = "flor" + os.sep + "tree_dist" + os.sep + "tree_dist"
	retu.geneCont = geneCont + "flor" + os.sep + "tree_dist" + os.sep
	retu.save = False
	retu.Init()
	return retu

def Jog_():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.mode = 0
	retu.name = "jog_"
	retu.dire = "jog_" + os.sep
	retu.scri = "jog_" + os.sep + "jog_"
	retu.geneCont = geneCont + "jog_" + os.sep
	#retu.save = False
	retu.Init()
	return retu

def Anim():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.mode = 0
	retu.name = "anim"
	retu.dire = "anim" + os.sep
	retu.scri = "anim" + os.sep + "anim"
	retu.geneCont = geneCont + "anim" + os.sep
	retu.Init()
	return retu

def Face(pref = "face"):
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "face"
	retu.dire = "face" + os.sep
	retu.geneCont = geneCont + "face" + os.sep
	retu.scri = "face" + os.sep + "face"
	retu.Init()
	return retu

def Mesh():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	#retu.mode = 0
	retu.mode = 1
	retu.name = "mesh"
	retu.dire = "mesh" + os.sep
	retu.geneCont = geneCont + "mesh" + os.sep
	retu.scri = "mesh" + os.sep + "mesh"
	retu.Init()
	return retu

def Jog_Game():
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.name = "jog__game"
	retu.dire = "jog__game" + os.sep
	retu.geneCont = geneCont + "jog__game" + os.sep
	retu.scri = "jog__game" + os.sep + "jog__game"
	retu.Init()
	return retu

def Mes1(pref = "mesh"):
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.mode = 1
	retu.name = "mesh"
	retu.dire = "mesh" + os.sep
	retu.geneCont = geneCont + "mesh" + os.sep
	retu.scri = "mesh" + os.sep + "mesh"
	retu.pref = pref
	retu.Init()
	return retu

def Mes2(pref = "mesh"):
	import os
	geneCont = GeneContLink()
	retu = Scri()
	retu.mode = 2
	retu.name = "mesh"
	retu.dire = "mesh" + os.sep
	retu.geneCont = geneCont + "mesh" + os.sep
	retu.scri = "mesh" + os.sep + "mesh"
	retu.pref = pref
	retu.Init()
	return retu

# assumes content directories arent numeric. name and pref can be numeric if added to ignoList
def FileCoun(out_, ignoList = [], pad_ = 4):
	import os
	fileList = os.listdir(out_)
	fileList = sorted(fileList)
	striSub_ = "-1"
	if len(fileList) > 0:
		stri = fileList[len(fileList) - 1]
		founList = []
		for a in range(len(ignoList)):
			founList.append(False)
		a = 0
		while a < len(stri):
			striSub_ = stri[a : a + pad_]
			if striSub_.isnumeric():
				igno = False
				for b in range(len(ignoList)):
					if founList[b] == False and ignoList[b] == striSub_:
						igno = True
						founList[b] = True
						break
				if igno == False:
					break
			a += 1
	return int(striSub_) + 1

def Make(scriList = [], fileCoun = 1, incr = True, rendImag = True, rendVide = False, framCoun = 1, exe_ = True):

	# TODO:

	# tree / spir / fern / flow
	# clean up scripts. tree etc
	# use os.sep

	# linux / windows / mac / new versions of blender

	# video:
	# modu explanation and all directories that gene and blen rely on

	# test:
	# conc()
	# purg merg flat

	# TODO eventually:

	# make a working python folder and a work in progress python folder

	# make flag files: out / pick / kept. purg and merg
	# reset a and count if pick flag is set
	# put all parent files where theyre supposed to be
	# record current nudg file

	# define folder names like out_ and libr

	# try to remove script header try / except and automatically add a function

	# make a purge py cache script

	import os
	import random
	read = True
	#read = False
	writ = True
	#writ = False
	Pyth = PythLink()
	Blen = BlenLink()
	# blenComm - the command that executes blender in the system [terminal / console]
	blenComm = BlenCommLink()
	# blenDire - the directory of the blender executable
	blenDire = BlenDireLink()
	# geneDire - this is not the code directory, this is where content created by the generator scripts is stored
	geneDire = GeneDireLink()
	# cap at 9999
	if fileCoun > 9999:
		fileCoun = 9999
	# read iden file
	if incr:
		iden = IdenRead()
	else:
		iden = {}
	# pick - pick the next library file to modify. when all have been picked, start over.
	pick = []
	for a in range(len(scriList)):
		pick.append(0)
	brea = 0
	true = True
	while true:
		for a in range(len(scriList)):
			# read variables
			name = scriList[a].name
			scri = scriList[a].scri
			dire = scriList[a].dire
			pref = scriList[a].pref
			save = scriList[a].save
			out_ = scriList[a].out_
			mode = scriList[a].mode
			syst = scriList[a].syst
			vari = scriList[a].vari
			geneCont = scriList[a].geneCont
			# check if iden has an entry for the script being run
			if (name in iden) == False:
				iden.update({name : 0})
				if incr:
					IdenWrit(iden)
			if mode != 3:
				# get the number of the next file
				fil_Coun = FileCoun(out_, ignoList = [name, pref])
				numb = Pyth.Pad_(fil_Coun, 4)
			# update variables
			if mode == 0:
				paraOut_ = out_ + name + "_" + numb + "_para"
				vari.update({"blenPath" : out_ + name + "_" + numb + ".blend"})
				vari.update({"numb" : numb})
			if mode == 1:
				# pick the next file in the libr folder
				fileList = geneCont
				fileList = Conc(fileList, pref)
				fileList += "libr" + os.sep
				fil_Coun = FileCoun(fileList, ignoList = [name, pref])
				fileName = out_
				fileName = Conc(fileName, pref, els_ = name)
				fileName += numb
				paraOut_ = fileName + "_para"
				vari.update({"blenPath" : fileName + ".blend"})
				vari.update({"numb" : numb})
				syst = blenComm + " -b " + geneCont
				syst = Conc(syst, pref)
				syst += "libr" + os.sep
				syst = Conc(syst, pref, els_ = name)
				syst += Pyth.Pad_(pick[a], 4) + ".blend" + " --python tempScri.py"
				pick[a] += 1
				if pick[a] == fil_Coun: pick[a] = 0
			if mode == 2:
				if fil_Coun > 0:
					# pick a random file in the out_ directory
					random.seed()
					rand = random.randint(0, fil_Coun - 1)
					syst = blenComm + " -b " + geneCont
					paraOut_ = out_ + name + "_" + numb + "_para"
					vari.update({"blenPath" : out_ + name + "_" + numb + ".blend"})
					vari.update({"numb" : numb})
					fil_ = Conc(syst, pref)
					syst += "out_" + os.sep
					syst = Conc(syst, pref, els_ = name)
					syst += Pyth.Pad_(rand, 4) + ".blend" + " --python tempScri.py"
				else:
					print("error: Make() function called on a script with mode 2 which requires at least one blend file in the out_ content directory. exiting.")
					return 0
			if mode == 3:
				paraOut_ = ""
			if paraOut_ != "":
				para = Para(paraOut_, dire, name, iden[name])
				vari.update({"para" : str(para)})
			if read:
				# read script
				fileObje = open(scri + ".py", mode = "r")
				stri = fileObje.read()
				fileObje.close()
			# should the blend file always be saved
			if save:
				fileObje = open("scri" + os.sep + "save.py", mode = "r")
				stri += fileObje.read()
				fileObje.close()

			# prepend required variables
			if vari != {}:
				vari = Pyth.DictTo__Vari(vari)
				stri = vari + stri
			if writ:
				# write tempScri to file
				fileObje = open("tempScri.py", mode = "w")
				fileObje.write(stri)
				fileObje.close()
			if exe_:
				# execute the command-line string
				os.system(syst)
			# render
			if rendImag or rendVide:
				if mode == 0:
					fil_ = geneCont + "out_" + os.sep + name + "_" + numb
				if mode == 1:
					fil_ = geneCont
					fil_ = Conc(fil_, pref)
					fil_ += "out_" + os.sep
					fil_ = Conc(fil_, pref, els_ = name)
					fil_ += numb
				if mode == 2:
					fil_ = geneCont + "out_" + os.sep + name + "_" + numb
				if mode == 3:
					fil_ = dire + os.sep + name
				syst = Blen.Batc(fil_ + ".blend")
				if rendImag:
					syst += Blen.Rend(fil_)
				if rendVide:
					syst += Blen.RendVide(fil_, framCoun)
				os.system(syst)
			iden[name] += 1
			# TODO: catch a program break?
			# rewrite iden file which tracks the count of the total files of each type created (for all history)
			if incr == True:
				IdenWrit(iden)
		brea += 1
		if brea >= fileCoun:
			true = False
		if fileCoun == -1:
			true = True

def IdenRead():
	import os
	Pyth = PythLink()
	retu = {}
	fileList = os.listdir()
	if "iden" in fileList:
		line = Pyth.FileTo__Line("iden")
		for a in range(len(line)):
			lin_ = line[a]
			lin_ = lin_.split("=")
			lin_[0] = lin_[0].strip()
			retu.update({lin_[0]:int(lin_[1])})
	else:
		Pyth.LineTo__File([], "iden")
	return retu

def IdenWrit(iden):
	Pyth = PythLink()
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
		name = key_
		name = name.split("_")
		entr = ""
		for a in range(len(name) - 1):
			entr += name[a]
			if a < len(name) - 2:
				entr += "_"
		if key_ == entr + "_mini":
			valu = Math.RandRang(para[entr + "_mini"], para[entr + "_maxi"])
			if type(para[entr + "_mini"]) == float:
				valu = float(valu)
			if type(para[entr + "_mini"]) == int:
				valu = int(valu)
			retu.update({entr:valu})
	return retu

def Conc(stri, wit_, els_ = ""):
	if wit_ != "":
		stri += wit_ + "_"
	elif els_ != "":
		stri += els_ + "_"
	return stri

#####################################

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

#####################################

def VertCoun(direList):
	Blen = BlenLink()
	Pyth = PythLink()
	Blen.Sele("obje")
	vertCoun = len(Blen.Vertices())
	Pyth.LineTo__File([str(vertCoun)], direList, mode = "a")

# TODO: organize position of functions and make categories
def Leng(direList):
	import bpy
	Blen = BlenLink()
	Pyth = PythLink()
	Blen.Sele("obje")
	leng = bpy.context.object.dimensions[0]
	Pyth.LineTo__File([str(leng)], direList, mode = "a")

def Sort(dire, direList, name = "", mode = 0):
	import os
	Pyth = PythLink()
	Head = HeadLink()
	blenComm = BlenCommLink()
	# mode:
	# 0: length
	# 1: vert count
	writ = True
	#writ = False
	if writ:
		Pyth.LineTo__File([], direList)
	fileList = os.listdir(dire)
	fileList = sorted(fileList)
	tempScri = Head()
	tempScri += "def main():\n"
	if mode == 0:
		tempScri += "\tGene.Leng(\"" + direList + "\")\n"
	if mode == 1:
		tempScri += "\tGene.VertCoun(\"" + direList + "\")\n"
	tempScri += "main()\n"
	if writ:
		fileObje = open("list/temp_scri.py", mode = "w")
		fileObje.write(tempScri)
		fileObje.close()
	for fil_ in fileList:
		blen = False
		para = False
		imag = False
		spli = fil_.split(".")
		if len(spli) > 0:
			if spli[len(spli) - 1] == "blend":
				blen = True
			if spli[len(spli) - 1] == "png":
				imag = True
		if blen == False and imag == False:
			para = True
		if blen:
			syst = blenComm + " -b " + dire + fil_ + " --python list/temp_scri.py"
			if writ:
				os.system(syst)
		numb = fil_.split("_")
		pre_ = numb
		nameStri = ""
		if blen or imag:
			if len(numb) > 0:
				numb = numb[len(numb) - 1]
			for a in range(len(pre_) - 1):
				nameStri += pre_[a] + "_"
		if para:
			if len(numb) > 1:
				numb = numb[len(numb) - 2]
			for a in range(len(pre_) - 2):
				nameStri += pre_[a] + "_"
		if blen or imag:
			numb = numb.split(".")
			if len(numb) > 0:
				numb = numb[0]
		numb = numb[0:4]
		numb = int(numb) + len(fileList)
		numb = Pyth.Pad_(numb, 4)
		nameStri += numb
		nameStri = dire + nameStri
		syst = "mv " + dire + fil_ + " " + nameStri
		if blen:
			syst += ".blend"
		if para:
			syst += "_para"
		if imag:
			syst += "0001.png"
		if writ:
			# TODO: windows
			os.system(syst)
	line = Pyth.FileTo__Line(direList)
	for a in range(len(line)):
		if mode == 0:
			line[a] = [float(line[a]), a + len(fileList)]
		if mode == 1:
			line[a] = [int(line[a]), a + len(fileList)]
	line = sorted(line)
	for a in range(len(line)):
		# TODO: predefine naming formats
		old_Dire = dire + name + "_" + Pyth.Pad_(line[a][1], 4)
		new_Dire = dire + name + "_" + Pyth.Pad_(a, 4)
		if writ:
			os.system("mv " + old_Dire + ".blend" + " " + new_Dire + ".blend")
			os.system("mv " + old_Dire + "_para" + " " + new_Dire + "_para")
			os.system("mv " + old_Dire + "0001.png" + " " + new_Dire + "0001.png")

