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

def FahrTo__Cels(fahr):
	return (fahr - 32.0) * 5.0 / 9.0

def CounZero(termList):
	import math
	retu = 0
	### get all maximums and all minimums of all terms
	### zip the positions into a list and track source, max, min
	tole = 0.0001
	#termList = [1.0, 8.0]
	# TODO: name
	inflList = []
	for a in range(len(termList)):
		b = 0
		while True:
			# maximum
			x = (2.0 * b) * math.pi / termList[a][0]
			if x < 2.0 * math.pi + tole:
				inflList.append([x, a, 0])
			else:
				break
			# minimum
			x = (1.0 + 2.0 * b) * math.pi / termList[a][0]
			if x < 2.0 * math.pi + tole:
				inflList.append([x, a, 1])
			else:
				break
			b += 1
	inflList = sorted(inflList)
	### purge duplicates
	a = len(inflList) - 2
	while a >= 0:
		if math.fabs(inflList[a][0] - inflList[a + 1][0]) < tole:
			inflList.pop(a + 1)
		a -= 1
	### check if y changes from positive to negative or negative to positive
	for a in range(len(inflList) - 1):
		x1 = inflList[a][0]
		y1 = termList[0][1] * math.cos(termList[0][0] * x1) + termList[1][1] * math.cos(termList[1][0] * x1)
		x2 = inflList[a + 1][0]
		y2 = termList[0][1] * math.cos(termList[0][0] * x2) + termList[1][1] * math.cos(termList[1][0] * x2)
		if math.fabs(y1) < tole:
			retu += 1
		else:
			if (y1 < 0.0 and y2 > 0.0) or (y1 > 0.0 and y2 < 0.0):
				retu += 1
	return retu

def main():

	print()

	import math

	#print(FahrTo__Cels(212.0))

	grap = True
	grap = False
	if grap:
		x = 0.0
		vertList = []
		end_ = 2.0 * math.pi
		incr = (end_ - x) / 200.0
		while x < end_:
			y = math.cos(x) + math.cos(8.0 * x)
			vertList.append((x, y, 0.0))
			x += incr
		edgeList = Math.EdgeLine(len(vertList) - 1)
		Blen.Uplo([vertList, edgeList, []])

	#termList = [1.0, 8.0]
	#zeroCoun = CounZero(termList)
	#print(zeroCoun)

	brut = True
	brut = False
	if brut:
		import random
		termList = [[0.0, 1.0], [212.0, 1.0]]
		while True:
			random.seed()
			nume = random.randint(1, 1000)
			random.seed()
			deno = random.randint(1, 1000)
			termList[0][0] = nume / deno
			random.seed()
			nume = random.randint(1, 1000)
			random.seed()
			deno = random.randint(1, 1000)
			termList[0][1] = nume / deno
			random.seed()
			nume = random.randint(1, 1000)
			random.seed()
			deno = random.randint(1, 1000)
			termList[1][1] = nume / deno
			#brea = False
			#for a in range(1, 1000):
			#	print(a)
			#	for b in range(1, 1000):
			#	nume = a
			#	deno = b
			counZero = CounZero(termList)
			#print(counZero)
			#if counZero != 424:
			#	print("counZero", counZero)
			if math.fabs(100 - counZero) < 20:
				print("counZero", counZero, termList)
			if counZero == 100:
				print(nume, deno)
				#brea = True
				break
			#if brea: break

	brut = True
	#brut = False
	if brut:
		import random
		termList = [[0.7948717948717948, 2.892857142857143], [32.0, 0.8523573200992556]]
		while True:
			random.seed()
			nume = random.randint(1, 10000)
			random.seed()
			deno = random.randint(1, 10000)
			termList[0][0] = nume / deno
			random.seed()
			nume = random.randint(1, 10000)
			random.seed()
			deno = random.randint(1, 10000)
			termList[0][1] = nume / deno
			random.seed()
			nume = random.randint(1, 10000)
			random.seed()
			deno = random.randint(1, 10000)
			termList[1][1] = nume / deno
			ter1 = False
			ter2 = False
			if CounZero(termList) == 0: ter1 = True
			termList[1][0] = 212.0
			if CounZero(termList) == 100: ter2 = True
			if ter1 and ter2:
				print(termList)
				break

main()

