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

	#import bpy
	import math
	import random

	####

	random.seed()
	rand = random.randint(4, 10)
	roomDime = []
	for a in range(rand):
		size = Math.RandRang(2.0, 10.0)
		rati = Math.RandRang(0.5, 2.0)
		roomDime.append([rati * size * size, rati * size, size])

	roomDime = sorted(roomDime, reverse = True)

	minx = maxx = miny = maxy = locx = locy = 0.0
	locxList = []
	locyList = []
	for a in range(len(roomDime)):
		locx = 0.0
		locy = 0.0
		radx = roomDime[a][1] / 2.0
		rady = roomDime[a][2] / 2.0
		if a > 0:
			# get max x / y paths
			#coux = 0
			#couy = 0
			coux = []
			couy = []
			x___ = -1.0
			y___ = -1.0
			tole = 0.0001
			inde = 0
			while inde < len(locxList):
				if locxList[inde][3] == 1:
					if x___ == -1.0 or math.fabs(x___ - locxList[inde][0]) > tole:
						x___ = locxList[inde][0]
						#coux += 1
						coux.append(inde)
				inde += 1
			inde = 0
			while inde < len(locyList):
				if locyList[inde][3] == 1:
					if y___ == -1.0 or math.fabs(y___ - locyList[inde][0]) > tole:
						y___ = locyList[inde][0]
						#couy += 1
						couy.append(inde)
				inde += 1
			print("a", a, coux, couy)
			# get all paths
			pathList = []
			#for b in range(coux):
			#	for c in range(couy):
			#		pathList.append([b, c])
			for b in range(len(coux)):
				for c in range(len(couy)):
					pathList.append([coux[b], couy[c]])
			#for path in pathList:
			#	print(path)
			print("before", len(pathList))
			# pop paths that overlap
			overList = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
			b = len(pathList) - 1
			while b >= 0:
				pop_ = False
				minx = locxList[pathList[b][0]][0]
				maxx = locxList[pathList[b][0]][0] + 2.0 * radx
				miny = locyList[pathList[b][1]][0]
				maxy = locyList[pathList[b][1]][0] + 2.0 * rady
				for c in range(len(objeList)):
					ovex = False
					ovey = False
					x___ = [[minx, 0], [maxx, 0], [objeList[c][0], 1], [objeList[c][1], 1]]
					x___ = sorted(x___)
					x___ = [x___[0][1], x___[1][1], x___[2][1], x___[3][1]]
					if x___ in overList: ovex = True
					y___ = [[miny, 0], [maxy, 0], [objeList[c][2], 1], [objeList[c][3], 1]]
					y___ = sorted(y___)
					y___ = [y___[0][1], y___[1][1], y___[2][1], y___[3][1]]
					if y___ in overList: ovey = True
					if ovex and ovey and math.fabs(maxx - objeList[c][0]) > tole and math.fabs(minx - objeList[c][1]) > tole and math.fabs(maxy - objeList[c][2]) > tole and math.fabs(miny - objeList[c][3]) > tole:
						pop_ = True
						break
				if pop_: pathList.pop(b)
				b -= 1
			print("after", len(pathList))
			if len(pathList) > 0:
				# get the path that results in the smallest total area
				area = 0.0
				areaInde = -1
				mi_x = ma_x = mi_y = ma_y = 0.0
				for b in range(len(locxList)):
					if locxList[b][0] < mi_x: mi_x = locxList[b][0]
					if locxList[b][0] > ma_x: ma_x = locxList[b][0]
				for b in range(len(locyList)):
					if locyList[b][0] < mi_y: mi_y = locyList[b][0]
					if locyList[b][0] > ma_y: ma_y = locyList[b][0]
				for b in range(len(pathList)):
					#if locxList[pathList[b][0]][0] - 0.0 < mi_x: mi_x = locxList[pathList[b][0]][0]
					if locxList[pathList[b][0]][0] + 2.0 * radx > ma_x: ma_x = locxList[pathList[b][0]][0] + 2.0 * radx
					#if locyList[pathList[b][1]][0] - 0.0 < mi_y: mi_y = locyList[pathList[b][1]][0]
					if locyList[pathList[b][1]][0] + 2.0 * rady > ma_y: ma_y = locyList[pathList[b][1]][0] + 2.0 * rady
					are_ = (ma_x - mi_x) * (ma_y - mi_y)
					if areaInde == -1 or are_ < area:
						area = are_
						areaInde = b
				print(areaInde, len(pathList))
				#prevRadx = locxList[pathList[areaInde][0]][1] / 2.0
				#prevRady = locyList[pathList[areaInde][1]][1] / 2.0
				#locx = locxList[pathList[areaInde][0]][0] + prevRadx + radx
				#locy = locyList[pathList[areaInde][1]][0] + prevRady + rady
				locx = locxList[pathList[areaInde][0]][0] + radx
				locy = locyList[pathList[areaInde][1]][0] + rady
		Blen.Plan()
		Blen.Scal((roomDime[a][1], roomDime[a][2], 1.0))
		Blen.Name(str(a) + "_" + str(roomDime[a][1]) + "_" + str(roomDime[a][2]))
		Blen.Loca((locx, locy, 0.0))

		locxList.append((locx - radx, roomDime[a][1], a, 0))
		locxList.append((locx + radx, roomDime[a][1], a, 1))
		locyList.append((locy - rady, roomDime[a][2], a, 0))
		locyList.append((locy + rady, roomDime[a][2], a, 1))
		locxList = sorted(locxList)
		locyList = sorted(locyList)
		objeList = []
		for b in range(len(locxList)):
			inde = locxList[b][2]
			while inde >= len(objeList): objeList.append([0.0, 0.0, 0.0, 0.0])
			if locxList[b][3] == 0: objeList[inde][0] = locxList[b][0]
			if locxList[b][3] == 1: objeList[inde][1] = locxList[b][0]
		for b in range(len(locyList)):
			inde = locyList[b][2]
			while inde >= len(objeList): objeList.append([0.0, 0.0, 0.0, 0.0])
			if locyList[b][3] == 0: objeList[inde][2] = locyList[b][0]
			if locyList[b][3] == 1: objeList[inde][3] = locyList[b][0]
		print()
		for obje in objeList: print(obje)

	####

def NodeUpda(key1, key2, nodeList, key_List):
	nodeList[key_List[key1]][key2] = True
	nodeList[key_List[key2]][key1] = True
	return nodeList

main()

