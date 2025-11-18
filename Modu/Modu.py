
import os
import importlib.util
import functools

##################################

# USER VARS

mainDire = os.path.expanduser("~") + os.sep
mainDire += "Documents" + os.sep + "prog" + os.sep
pythDire = mainDire + "Pyth" + os.sep
moduDire = pythDire + "Modu" + os.sep
mathDire = pythDire + "Math" + os.sep
blenDire = pythDire + "Blen" + os.sep
blenGameDire = pythDire + "BlenGame" + os.sep
geneDire = pythDire + "Gene" + os.sep
nodeDire = pythDire + "Node" + os.sep

logiDire = blenGameDire + "scri" + os.sep
geneCont = mainDire + "gene" + os.sep

# options for blender batch mode
linuExec = os.path.expanduser("~") + os.sep + "Downloads" + os.sep
macoExec = os.sep + "Applications" + os.sep
windExec = ""

# True if using a portable linux version
linuPort = False
linuPort = True

linuVers = "blender-2.78c-linux-glibc219-x86_64"
macoVers = "blender-2.78c-OSX_10.6-x86_64"

#################################

# form the command to execute blender in a console
blenComm = ""

# windows
if os.name == 'nt':
	blenComm = '\"C:\\Program Files\\Blender Foundation\\Blender\\blender.exe\"'
	#blenComm = r'\"C:\\Program^ Files\\Blender^ Foundation\\Blender\\blender.exe\"'
# posix (mac / linux)
else:
	# check if the macoExec directory exists. if it does, assume it's a mac system, otherwise, assume linux
	# ! this wont work if the macoExec directory exists on a linux system. in that case, you could create another variable for a comparison, or create a file on mac to identify it, or try another approach.
	exis = os.path.exists(macoExec)
	if exis:
		blenComm = macoExec + macoVers + os.sep + "blender.app" + os.sep + "Contents" + os.sep + "MacOS" + os.sep + "blender"
	else:
		if linuPort == True:
			blenComm = linuExec + linuVers + os.sep + "blender"
		else:
			blenComm = "blender"

#################################

# LOAD LIBRARIES

spec = importlib.util.spec_from_file_location("Pyth", pythDire + "Pyth.py")
Pyth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Pyth)

spec = importlib.util.spec_from_file_location("Math", mathDire + "Math.py")
Math = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Math)

spec = importlib.util.spec_from_file_location("Blen", blenDire + "Blen.py")
Blen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Blen)

spec = importlib.util.spec_from_file_location("BlenGame", blenGameDire + "BlenGame.py")
BlenGame = importlib.util.module_from_spec(spec)
spec.loader.exec_module(BlenGame)

spec = importlib.util.spec_from_file_location("Gene", geneDire + "Gene.py")
Gene = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Gene)

spec = importlib.util.spec_from_file_location("Node", nodeDire + "Node.py")
Node = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Node)

#################################

# FUNCTIONS

# TODO: test
# append header for a python expression
def Head():
	retu = ""
	fileObje = open(moduDire + "head", mode = "r")
	retu += fileObje.read()
	fileObje.close()
	#return "import importlib.util\nimport os\npath = os.path.expanduser(\"~\") + os.sep\npath += \"Documents\" + os.sep + \"prog\" + os.sep + \"Pyth\" + os.sep + \"Modu\" + os.sep + \"Modu.py\"\nspec = importlib.util.spec_from_file_location(\"Modu\", path)\nModu = importlib.util.module_from_spec(spec)\nspec.loader.exec_module(Modu)\nPyth = Modu.Pyth\nMath = Modu.Math\nBlen = Modu.Blen\nBlenGame = Modu.BlenGame\nGene = Modu.Gene\n"
	return retu

#################################

# LINK LIBRARIES AND FORWARD DIRECTORIES

Math.PythLink = functools.partial(Math.PythLink, Pyth = Pyth)

Blen.PythLink = functools.partial(Blen.PythLink, Pyth = Pyth)
Blen.MathLink = functools.partial(Blen.MathLink, Math = Math)
Blen.BlenGameLink = functools.partial(Blen.BlenGameLink, BlenGame = BlenGame)
Blen.HeadLink = functools.partial(Blen.HeadLink, Head = Head)
Blen.BlenCommLink = functools.partial(Blen.BlenCommLink, blenComm = blenComm)
Blen.BlenDireLink = functools.partial(Blen.BlenDireLink, blenDire = blenDire)

BlenGame.PythLink = functools.partial(BlenGame.PythLink, Pyth = Pyth)
BlenGame.BlenLink = functools.partial(BlenGame.BlenLink, Blen = Blen)
BlenGame.MathLink = functools.partial(BlenGame.MathLink, Math = Math)
BlenGame.HeadLink = functools.partial(BlenGame.HeadLink, Head = Head)
BlenGame.BlenCommLink = functools.partial(BlenGame.BlenCommLink, blenComm = blenComm)
BlenGame.BlenDireLink = functools.partial(BlenGame.BlenDireLink, blenDire = blenDire)
BlenGame.LogiDireLink = functools.partial(BlenGame.LogiDireLink, logiDire = logiDire)

Gene.PythLink = functools.partial(Gene.PythLink, Pyth = Pyth)
Gene.MathLink = functools.partial(Gene.MathLink, Math = Math)
Gene.BlenLink = functools.partial(Gene.BlenLink, Blen = Blen)
Gene.BlenCommLink = functools.partial(Gene.BlenCommLink, blenComm = blenComm)
Gene.BlenDireLink = functools.partial(Gene.BlenDireLink, blenDire = blenDire)
Gene.GeneDireLink = functools.partial(Gene.GeneDireLink, geneDire = geneDire)
Gene.GeneContLink = functools.partial(Gene.GeneContLink, geneCont = geneCont)
Gene.HeadLink = functools.partial(Gene.HeadLink, Head = Head)

Node.MathLink = functools.partial(Node.MathLink, Math = Math)
Node.BlenLink = functools.partial(Node.BlenLink, Blen = Blen)
Node.BlenGameLink = functools.partial(Node.BlenGameLink, BlenGame = BlenGame)

