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

	# TODO:
	# move data to gene
	# purge files that are all false

	import random

	# TODO: get group count
	grou = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
	# read directory
	# TODO
	#dire = "/home/christopher/Documents/prog/gene/face/face_libr/"
	dire = "/home/christopher/Documents/prog/gene/face/libr/"

	read = True
	#read = False
	if read:
		
		fileList = os.listdir(dire)
		a = len(fileList) - 1
		while a >= 0:
			name = fileList[a].split(".")
			if name[len(name) - 1] != "blend":
				fileList.pop(a)
			a -= 1
		leng = len(fileList)
		# pick faces until all good features are found
		while (-1 in grou):
			random.random()
			rand = random.randint(0, leng - 1)
			# read good features
			para = "face_" + Pyth.Pad_(rand, 4) + "_para"
			para = Pyth.FileTo__Line(dire + para)
			for a in range(len(para)):
				if grou[a] == -1 and para[a] == "True":
					grou[a] = rand
					break

	# write groups to a file
	for a in range(len(grou)):

		# open grou[a] in blender and run sepa
		scri = Modu.Head()
		scri += "def main():\n"
		scri += "\n\timport bpy\n"
		scri += "\n\tgrou = " + str(a) + "\n\n"
		sepa = Pyth.FileTo__Line("face/sepa")
		scri += "\t"
		for line in sepa:
			scri += line + "\n"
		scri += "\n"
		scri += "\tobje = Blen.Down()\n"

		# TODO: make a function to export / read an object list
		scri += "\tobje[0] = Pyth.TuplListExpo(obje[0])\n"
		scri += "\tobje[1] = str(obje[1])\n"
		scri += "\tobje[2] = str(obje[2])\n"
		scri += "\tPyth.LineTo__File(obje[0], \"/home/christopher/Documents/prog/Pyth/Gene/face/expo/" + str(a) + "_vert\")\n"
		scri += "\tPyth.LineTo__File([obje[1]], \"/home/christopher/Documents/prog/Pyth/Gene/face/expo/" + str(a) + "_edge\")\n"
		scri += "\tPyth.LineTo__File([obje[2]], \"/home/christopher/Documents/prog/Pyth/Gene/face/expo/" + str(a) + "_poly\")\n"

		scri += "\nmain()\n"

		fileObje = open("tempScri.py", mode = "w")
		fileObje.write(scri)
		fileObje.close()

		syst = Modu.blenComm + " -b " + dire + "face_" + Pyth.Pad_(grou[a], 4) + ".blend --python tempScri.py"
		os.system(syst)

	a = 0
	while a < len(grou):
		grou[a] = str(grou[a])
		a += 1
	Pyth.LineTo__File(grou, "face/seam/grou")

main()

