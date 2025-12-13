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

def main():

	print()

	import math

	radi = 1.0
	voluSphe = (4.0 / 3.0) * math.pi * radi ** 2.0

	# TODO: just get a vector and use vectmagn
	# cube with 2 divisions
	# center cube within sphere. how to tell
	# get radius to corner of cube
	#divi = 2
	#cubeRadi = 1.0
	# center cube
	#radi = ((cubeRadi / (divi + 1)) ** 2.0 + (cubeRadi / (divi + 1)) ** 2.0 + (cubeRadi / (divi + 1)) ** 2.0) ** 0.5
	# less than radius of sphere
	#print(radi)

	# cube with 2 divisions
	# get the volume of the cap left from a slice at 1/3
	prog = 1.0 / 3.0
	voluCap_ = ((math.pi * (1.0 - prog) ** 2.0) / 3.0) * (3.0 * radi - (1.0 - prog))
	# get the ratio of cap volume to total volume
	rati = voluCap_ / voluSphe
	# get cap of cap
	voluEdge = voluCap_ * rati
	# get corner volume
	voluCorn = voluEdge * rati
	# get center border
	voluCeed = voluEdge - 2.0 * voluCorn
	# get center cap
	voluCent = voluCap_ - 4.0 * voluCorn - 4.0 * voluCeed

	# tree dist:
	# start at branch nodes closest to trunk
	# tree dist scoring:
	# get the ratio of the section volume to sphere volume

	# try:
	divi = 2
	cent = (0.0, 0.0, 0.0)
	radi = 1.0
	inte = 2.0 * radi / (divi + 1)
	a = 0
	chec = 2
	x = 0
	while x <= divi:
		y = 0
		while y <= divi:
			z = 0
			while z <= divi:
				# for each cube section:
				# check if the section is entirely within the sphere, or entirely outside the sphere
				# get minimum radius
				xsig = x >= divi / 2.0
				ysig = y >= divi / 2.0
				zsig = z >= divi / 2.0
				if xsig == False:
					xmin = (x + 1) * inte
					xmax = x * inte
				else:
					xmax = (x + 1) * inte
					xmin = x * inte
				xmin = xmin - radi
				xmax = xmax - radi
				#if a == 0:
				#	print(xmin, xmax)
				if ysig == False:
					ymin = (y + 1) * inte
					ymax = y * inte
				else:
					ymax = (y + 1) * inte
					ymin = y * inte
				ymin = ymin - radi
				ymax = ymax - radi
				if zsig == False:
					zmin = (z + 1) * inte
					zmax = z * inte
				else:
					zmax = (z + 1) * inte
					zmin = z * inte
				zmin = zmin - radi
				zmax = zmax - radi
				mini = (xmin, ymin, zmin)
				miniMagn = Math.VectMagn(mini)
				maxi = (xmax, ymax, zmax)
				maxiMagn = Math.VectMagn(maxi)
				#print(x, y, z, xsig, ysig, zsig)
				#print(x, y, z, mini, maxi)

				if a == chec:
					#print(x, y, z)
					#Blen.Curs(mini)
					Blen.Curs(maxi)
					#print(mini, maxi)

				a += 1
				z += 1
			y += 1
		x += 1
	
	# if not, get xcap, ycap, and zcap ratios

main()

