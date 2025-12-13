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

	import bpy

	scenName = bpy.context.scene.name

	dire = "/home/christopher/Documents/prog/gene/face/face_out_/"
	# TODO
	# get image size
	widt = 960
	heig = 540
	# TODO
	# count vertex groups
	grouCoun = 12

	fileList = os.listdir(dire)
	a = len(fileList) - 1
	while a >= 0:
		exte = fileList[a].split(".")
		if exte[len(exte) - 1] != "png":
			fileList.pop(a)
		a -= 1

	fileList = sorted(fileList)

	Blen.Sele(scenName + "." + "scen_obje")
	opti = BlenGame.LogiSensOpti()
	sens = BlenGame.LogiSensDict()
	cont = BlenGame.LogiContDict()
	opti["use_pulse_true_level"] = True
	cont['text'] = "/home/christopher/Documents/prog/Pyth/Gene/face/game.py"
	BlenGame.Logi(sensOpti = opti, sensDict = sens, contDict = cont)
	opti = BlenGame.LogiSensOpti()
	sens = BlenGame.LogiSensDict(typ_ = "KEYBOARD")
	opti["use_tap"] = True
	sens["key"] = "RET"
	BlenGame.Logi(sensOpti = opti, sensDict = sens, sensName = 'ente', contDict = 'linkSens')
	BlenGame.Prop(propName = "coun", propType = 'INT', propValu = len(fileList))
	BlenGame.Prop(propName = "curr", propType = 'INT', propValu = -1)
	BlenGame.Prop(propName = "grouCoun", propType = 'INT', propValu = grouCoun)
	for a in range(grouCoun):
		typeList = ['f', 't']
		for typ_ in typeList:
			# TODO
			if scenName == "Scene":
				Blen.Sele("grou." + Blen.Pad_(a) + "." + typ_)
			else:
				Blen.Sele(scenName + "." + "grou." + Blen.Pad_(a) + "." + typ_)
			opti = BlenGame.LogiSensOpti()
			sens = BlenGame.LogiSensDict(typ_ = "MOUSE")
			cont = BlenGame.LogiContDict()
			opti["use_tap"] = True
			sens["mouse_event"] = "LEFTCLICK"
			cont['text'] = "/home/christopher/Documents/prog/Pyth/Gene/face/grou.py"
			BlenGame.Logi(sensOpti = opti, sensDict = sens, contDict = cont)

			opti = BlenGame.LogiSensOpti()
			sens = BlenGame.LogiSensDict(typ_ = "MOUSE")
			cont = BlenGame.LogiContDict(typ_ = "LOGIC_AND")
			actu = BlenGame.LogiActuDict(typ_ = "PROPERTY")
			sens["mouse_event"] = "MOUSEOVER"
			actu["property"] = "over"
			actu["value"] = "True"
			BlenGame.Logi(sensOpti = opti, sensDict = sens, contDict = cont, actuDict = actu)

			opti["invert"] = True
			actu["value"] = "False"
			BlenGame.Logi(sensOpti = opti, sensDict = sens, contDict = cont, actuDict = actu)

			BlenGame.Prop(propName = "over", propType = 'BOOL')

			if typ_ == 't':
				bpy.context.object.hide = True
				bpy.context.object.hide_render = True

		Blen.Sele(scenName + "." + "scen_obje")
		BlenGame.Prop(propName = "set_." + Blen.Pad_(a), propType = 'BOOL')

	for a in range(len(fileList)):
		numb = fileList[a]
		numb = numb[5:9]
		# set plane size
		Blen.Plan()
		Blen.Name(scenName + "." + "plan." + numb)
		Blen.Loca((-5.1, 0.0, -0.1))
		bpy.context.object.dimensions = (widt / 100.0, heig / 100.0, 1.0)
		# TODO:
		Blen.Scal((2.5, 2.5, 2.5))
		# apply image
		mate = "mate." + numb
		text = "text." + numb
		imag = "/home/christopher/Documents/prog/gene/face/face_out_/face_" + numb + "0001.png"
		Blen.Mate(name = mate, use_shadeless = True)
		Blen.MateText(text)
		Blen.Imag(imag, text)
		# TODO: didnt work in Blen.Imag()
		bpy.context.object.active_material.texture_slots[0].texture_coords = 'ORCO'
		bpy.context.object.hide = True
		bpy.context.object.hide_render = True

main()

