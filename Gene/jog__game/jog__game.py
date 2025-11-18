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
Node = Modu.Node

nodz = 0.01

def main():

	#import bpy
	import math

	print()

	lev1 = True
	#lev1 = False
	if lev1:

		scenNew_ = False
		resx = 600
		resy = 600
		scenNew_ = Temp(scenNew_ = scenNew_, resx = resx, resy = resy)
		
def Temp(scenNew_ = False, resx = 1360, resy = 768, glsl = True):

	import bpy
	import math
	import random

	logiDire = BlenGame.LogiDireLink()

	leve = "temp"
	scenNew_ = LeveInit(name = leve, scenNew_ = scenNew_, resx = resx, resy = resy, glsl = glsl)

	bpy.ops.object.lamp_add(type = 'SUN', location = (-10.0, -10.0, 10.0))
	Blen.Rota(rota = (45.0, -45.0, -90.0))

	name = "matt"

	charList = []
	charList.append(name)
	scenObje = BlenGame.ScenObje(charList = charList)

	# TODO: shield texture didnt import. folder 15 (need to reload png)
	dic_ = Blen.Impo(blenFile = "/home/christopher/Documents/prog/game/path_shor/make/scen/char/matt/matt.blend", empt = True)

	Blen.Sele(name)
	coun = 4
	acti = BlenGame.ActiDict()










	random.seed()
	acti["armsRadi"] = 0.2 + 0.6 * random.random()
	random.seed()
	acti["armsRati"] = 3.0 + 4.0 * random.random()
	random.seed()
	acti["legsRadi"] = 2.0 + 1.0 * random.random()
	random.seed()
	acti["osci"] = 0.03 + 0.02 * random.random()
	random.seed()
	acti["tilt"] = math.radians(10.0 + 10.0 * random.random())
	acti["cyclSpee"] = 5.0 + 5.0 * random.random()
	random.seed()
	acti["spee"] = 0.2 + 0.1 * random.random()

	BlenGame.Char(loca = (0.0, 0.0, 0.0), dire = "/home/christopher/Documents/prog/game/path_shor/make/scen/char/matt/", empt = 1.0, cyclArms = True, acti = [acti], coun = coun)
	Blen.Sele(name)
	for a in range(16):
		valx = Math.RandRang(-0.25, 0.25)
		valy = Math.RandRang(-0.25, 0.25)
		vaax = Math.RandRang(-0.25, 0.25)
		vaay = Math.RandRang(-0.25, 0.25)
		bpy.context.object.game.properties["jog_LegsX" + Pyth.Pad_(a, 2)].value += valx
		bpy.context.object.game.properties["jog_LegsY" + Pyth.Pad_(a, 2)].value += valy
		bpy.context.object.game.properties["jog_ArmsX" + Pyth.Pad_(a, 2)].value += vaax
		bpy.context.object.game.properties["jog_ArmsY" + Pyth.Pad_(a, 2)].value += vaay

	# axles
	legx = Math.RandRang(-0.1, 0.1)
	legz = Math.RandRang(-0.1, 0.1)
	armx = Math.RandRang(-0.1, 0.1)
	armz = Math.RandRang(-0.1, 0.1)
	Blen.Sele(name + "." + "axle.legs.l")
	loca = Blen.LocaRead()
	Blen.Loca((loca[0] + legx, loca[1], loca[2] + legz))
	Blen.Sele(name + "." + "axle.legs.r")
	loca = Blen.LocaRead()
	Blen.Loca((loca[0] + legx, loca[1], loca[2] + legz))

	Blen.Sele(name + "." + "axle.arms.l")
	loca = Blen.LocaRead()
	Blen.Loca((loca[0] + armx, loca[1], loca[2] + armz))
	Blen.Sele(name + "." + "axle.arms.r")
	loca = Blen.LocaRead()
	Blen.Loca((loca[0] + armx, loca[1], loca[2] + armz))

	Blen.Sele(name)
	BlenGame.Cont(faci = (1.0, 0.0), tracHeig = 4.0, grav = -9.8, veloInit = 1.5, coun = coun)
	#Blen.Sele(name)
	#BlenGame.CharCame(cameName = "Camera", tab = False, faci = (1.0, 0.0), scroSens = 10, lookY___Limi = True, lookY___LimiInve = False, lookY___Uppe = 1.710422666954443, lookY___Lowe = 1.2915436464758039, charList = [])

	Blen.Sele("Camera")
	Blen.Loca((0.0, -3.0, 1.6))
	Blen.RotaSet_((80.0, 0.0, 0.0))
	
	Blen.Sele("Sun")
	Blen.Loca((0.0, -2.0, 2.0))
	Blen.RotaSet_((45.0, -45.0, 35.0))

	bpy.data.objects["scen_obje"].game.controllers["Python"].active = False
	#bpy.data.objects["matt"].game.controllers["Python.002"].active = False
	Blen.Sele(name)
	BlenGame.Prop(propName = "spee", propType = 'FLOAT')
	BlenGame.Prop(propName = "dire", propType = 'INT')
	BlenGame.PropSet_(propName = "move", propValu = True)
	BlenGame.PropSet_(propName = "jog_", propValu = 1)

	BlenGame.Pref(leve)

	return scenNew_

# TODO: add to blengame
def Scri(text, sensName = "", use_priority = False):
	sens = "ALWAYS"
	sensDict = BlenGame.LogiSensDict(typ_ = sens)
	sensOpti = BlenGame.LogiSensOpti()
	contDict = BlenGame.LogiContDict()
	contOpti = BlenGame.LogiContOpti()
	sensOpti["use_pulse_true_level"] = True
	contDict["text"] = text
	if use_priority:
		contOpti["use_priority"] = True
	BlenGame.Logi(sensName = sensName, sensDict = sensDict, sensOpti = sensOpti, contDict = contDict, contOpti = contOpti)

def LeveInit(name = "", scenNew_ = False, resx = 1360, resy = 768, glsl = True):
	import bpy
	if scenNew_ == False:
		Blen.DeleDefa()
		scenNew_ = True
	else:
		Blen.ScenNew_()
	Blen.ScenName(name)
	BlenGame.Reso(resx, resy)
	BlenGame.EngiGame()
	BlenGame.FramExte()
	BlenGame.Debu()
	if glsl == True:
		BlenGame.Glsl()
	bpy.data.worlds["World"].horizon_color = (0.0, 0.0, 0.0)
	return scenNew_

main()

