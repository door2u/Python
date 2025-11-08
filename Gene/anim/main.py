
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

def PoseAdd_(poseList, inde, obje, pose, offs):
	poseList[inde].append([obje, (pose[inde][len(poseList[inde])][0] + offs[inde][len(poseList[inde])][0], pose[inde][len(poseList[inde])][1] + offs[inde][len(poseList[inde])][1], pose[inde][len(poseList[inde])][2] + offs[inde][len(poseList[inde])][2])])
	return poseList

def Pose(poseList, inde):
	for a in range(len(poseList[inde])):
		#print("obje", poseList[inde][a][0])
		#print("rota", poseList[inde][a][1])
		Blen.Sele(poseList[inde][a][0])
		Blen.RotaSet_(poseList[inde][a][1])

def main():

	play = True
	#play = False
	if play:
		out_ = "/home/christopher/Documents/prog/gene/anim/out_/"
		exe_ = "/home/christopher/Downloads/blender-2.78c-linux-glibc219-x86_64/blenderplayer"
		fileList = os.listdir(out_)
		fileList = sorted(fileList)
		for fil_ in fileList:
			name = fil_.split(".")
			if len(name) > 0 and name[len(name) - 1] == "blend":
				os.system(exe_ + " " + out_ + fil_)

	pose = True
	pose = False
	if pose:
		import math
		name = "matt"
		key_Coun = 6
		bow_Anim = []
		timeList = []
		for a in range(key_Coun):
			bow_Anim.append([])
			timeList.append(0.0)
		bow_Anim[0].append((-9.956509590148926, 8.098031997680664, 0.660513162612915))
		bow_Anim[0].append((-0.5120113492012024, -8.408488273620605, -7.078009605407715))
		bow_Anim[0].append((2.730665922164917, 6.031726837158203, 4.393641948699951))
		bow_Anim[1].append((-4.914102554321289, 17.312920999526977, 3.885723829269409))
		bow_Anim[1].append((2.9964630603790283, -92.04479241371155, 28.549610710144044))
		bow_Anim[1].append((31.21913843154907, -1.4837994575500488, 6.285317897796631))
		bow_Anim[2].append((-23.321675109863282, -33.61186256408691, -9.998162364959716))
		bow_Anim[2].append((2.1855549812316895, -134.00480222702026, -6.310117530822754))
		bow_Anim[2].append((15.142509031295777, 77.83781256675721, -45.94693546295166))
		bow_Anim[2].append((-96.98304539310416, 26.86925150445699, -60.068446742064964))
		bow_Anim[3].append((12.767421627044676, -19.107391473278405, -13.359359169006346))
		bow_Anim[3].append((12.20978593826294, -134.93702101707458, 0.5044281005859377))
		bow_Anim[3].append((19.116707611083985, 73.08039083480836, -64.33842449188232))
		bow_Anim[3].append((-102.76148610698661, 39.45585228494405, -61.454979525573265))

		bow_Anim[4].append((13.91518940925598, -28.173756217956544, -14.154681587219237))
		bow_Anim[4].append((-23.610430854558945, -133.44030900001525, 16.801973819732666))
		bow_Anim[4].append((121.39839534759521, 77.79054260253906, 59.20841331481934))
		bow_Anim[4].append((-102.76148610698661, 39.45585228494405, -61.454979525573265))

		##########

		bow_Anim[5].append((13.9, -60.5, -14.2))
		bow_Anim[5].append((10.0, -29.2, 16.8))
		bow_Anim[5].append((40.0, 0.0, 3.0))
		#bow_Anim[5].append((30.0, -10.0, 23.0))
		bow_Anim[5].append((-2.0, 18.0, -14.5))
		poseList = []
		for a in range(key_Coun):
			poseList.append([])
		offsList = []
		for a in range(len(bow_Anim)):
			offs = []
			for b in range(len(bow_Anim[a])):
				offs.append((0.0, 0.0, 0.0))
			offsList.append(offs)
		inde = 0
		poseList = PoseAdd_(poseList, inde, name + "." + "shou.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "elbo.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "wris.r", bow_Anim, offsList)
		inde += 1
		poseList = PoseAdd_(poseList, inde, name + "." + "shou.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "elbo.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "wris.r", bow_Anim, offsList)
		inde += 1
		poseList = PoseAdd_(poseList, inde, name + "." + "shou.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "elbo.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "wris.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "bow_", bow_Anim, offsList)
		inde += 1
		poseList = PoseAdd_(poseList, inde, name + "." + "shou.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "elbo.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "wris.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "bow_", bow_Anim, offsList)
		inde += 1
		poseList = PoseAdd_(poseList, inde, name + "." + "shou.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "elbo.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "wris.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "bow_", bow_Anim, offsList)
		inde += 1
		poseList = PoseAdd_(poseList, inde, name + "." + "shou.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "elbo.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "wris.r", bow_Anim, offsList)
		poseList = PoseAdd_(poseList, inde, name + "." + "bow_", bow_Anim, offsList)

		######

		Pose(poseList, 1)
		Blen.Sele("matt.bow_")
		Blen.Pare("matt.wris.r")
		Pose(poseList, 5)
		#Blen.Loca((0.3041, -0.1783, 1.6888))
		#Blen.RotaSet_((math.degrees(-0.2264), math.degrees(-0.2806), math.degrees(0.2359)))

	add_ = True
	add_ = False
	if add_:
		key_Coun = 4
		bow_Anim = []
		for a in range(key_Coun):
			bow_Anim.append([])
		inde = 0
		bow_Anim[inde].append((0.0, -84.1, -57.0))
		bow_Anim[inde].append((99.4,  -8.1,  0.0))
		bow_Anim[inde].append((0.0,  0.0,  0.0))
		inde += 1
		bow_Anim[inde].append((-52.6, -139.0, -59.0))
		bow_Anim[inde].append((34.0,  13.7, -2.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0,  0.0,  -10.0))
		inde += 1
		bow_Anim[inde].append((-52.6, -90.0, 80.0))
		bow_Anim[inde].append((55.0, 15.4, 2.0))
		bow_Anim[inde].append((0.0, 0.0, -90.0))
		bow_Anim[inde].append((0.0, -70.0, 0.0))
		bow_Anim[inde].append((0.0, 60.0, 0.0))
		bow_Anim[inde].append((0.0, 60.0, 0.0))
		bow_Anim[inde].append((0.0, 10.0, 30.0))
		inde += 1
		bow_Anim[inde].append((0.0, -84.1, -57.0))
		bow_Anim[inde].append((99.4,  -8.1,  0.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0, 0.0, 0.0))
		bow_Anim[inde].append((0.0,  0.0,  0.0))
		for a in range(len(bow_Anim)):
			for b in range(len(bow_Anim[a])):
				BlenGame.Prop(propName = "offs." + str(a) + "." + str(b) + ".x", propType = 'FLOAT')
				BlenGame.Prop(propName = "offs." + str(a) + "." + str(b) + ".y", propType = 'FLOAT')
				BlenGame.Prop(propName = "offs." + str(a) + "." + str(b) + ".z", propType = 'FLOAT')

main()
