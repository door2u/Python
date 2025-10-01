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

	dire = "/home/christopher/Documents/prog/game/path_shor/bow_/"
	blenName = "anim_0712"

	expr = ""
	expr += Modu.blenComm + " -b " + dire + blenName + ".blend"	
	expr += " --python tempScri.py"

	scri = Modu.Head()
	scri += "def main():\n"

	#scri += "\timport bpy\n"
	#scri += "\tfor a in range(len(bpy.context.object.game.properties)):\n"
	#scri += "\t\tname = bpy.context.object.game.properties[a].name\n"
	#scri += "\t\tname = name.split(\".\")\n"
	#scri += "\t\tif len(name) > 0 and name[0] == \"offs\":\n"
	#scri += "\t\t\tprint(bpy.context.object.game.properties[a].name, bpy.context.object.game.properties[a].value)\n"

	scri += "\timport bpy\n"
	scri += "\timport math\n"
	scri += "\tbow_Anim = []\n"
	scri += "\tbow_Anim.append([])\n"
	scri += "\tbow_Anim.append([])\n"
	scri += "\tbow_Anim.append([])\n"
	scri += "\tbow_Anim.append([])\n"
	scri += "\tbow_Anim.append([])\n"
	scri += "\tbow_Anim[0].append((0.0, 0.0, 0.0))\n"
	scri += "\tbow_Anim[0].append((0.0, 0.0, 0.0))\n"
	scri += "\tbow_Anim[0].append((0.0, 0.0, 0.0))\n"
	scri += "\tbow_Anim[1].append((0.0, 15.7, 0.0))\n"
	scri += "\tbow_Anim[1].append((0.0, -94.0, 18.6))\n"
	scri += "\tbow_Anim[1].append((36.8, 0.0, 0.0))\n"
	scri += "\tbow_Anim[2].append((-17.8, -24.9, -2.6))\n"
	scri += "\tbow_Anim[2].append((6.0, -137.0, 2.7))\n"
	scri += "\tbow_Anim[2].append((13.3, 79.4, -54.8))\n"
	scri += "\tbow_Anim[2].append((math.degrees(-1.8450), math.degrees(0.5910), math.degrees(-1.2878 + 0.1)))\n"
	scri += "\tbow_Anim[3].append((17.9, -19.1, -16.4))\n"
	scri += "\tbow_Anim[3].append((6.0, -137.0, 2.7))\n"
	scri += "\tbow_Anim[3].append((13.3, 79.4, -54.8))\n"
	scri += "\tbow_Anim[3].append((math.degrees(-1.8450), math.degrees(0.5910), math.degrees(-1.2878 + 0.1)))\n"
	scri += "\tbow_Anim[4].append((17.9, -19.1, -16.4))\n"
	scri += "\tbow_Anim[4].append((-23.3, -136.2, 14.0))\n"
	scri += "\tbow_Anim[4].append((123.3, 73.0, 62.2))\n"
	scri += "\toffsList = []\n"
	scri += "\tfor a in range(len(bpy.context.object.game.properties)):\n"
	scri += "\t\tname = bpy.context.object.game.properties[a].name\n"
	scri += "\t\tname = name.split(\".\")\n"
	scri += "\t\tif len(name) > 0 and name[0] == \"offs\":\n"
	scri += "\t\t\toffsList.append(bpy.context.object.game.properties[a].value)\n"
	scri += "\ta = 0\n"
	scri += "\tfor b in range(len(bow_Anim)):\n"
	scri += "\t\tfor c in range(len(bow_Anim[b])):\n"
	#scri += "\t\t\tfor d in range(3):\n"
	scri += "\t\t\tprint(\"bow_Anim[\" + str(b) + \"].append((\" + str(bow_Anim[b][c][0] + offsList[a]) + \", \" + str(bow_Anim[b][c][1] + offsList[a + 1]) + \", \" + str(bow_Anim[b][c][2] + offsList[a + 2]) + \"))\")\n"
	#print("bow_Anim[" + str(b) + "].append((" + str(bow_Anim[b][c][0] + offsList[a]) + "), (" + str(bow_Anim[b][c][1] + offsList[a + 1]) + "), (" + str(bow_Anim[b][c][2] + offsList[a + 2]) + "))"
	scri += "\t\t\ta += 3\n"
	scri += "main()\n"

	fileObje = open("tempScri.py", mode = "w")
	fileObje.write(scri)
	fileObje.close()

	# execute
	os.system(expr)

main()
