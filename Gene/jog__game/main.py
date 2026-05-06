
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

	play = True
	#play = False
	if play:
		out_ = "/home/christopher/Documents/prog/gene/jog__game/out_/"
		exe_ = "/home/christopher/Downloads/blender-2.78c-linux-glibc219-x86_64/blenderplayer"
		fileList = os.listdir(out_)
		fileList = sorted(fileList)
		for fil_ in fileList:
			name = fil_.split(".")
			if len(name) > 0 and name[len(name) - 1] == "blend":
				os.system(exe_ + " " + out_ + fil_)

main()
