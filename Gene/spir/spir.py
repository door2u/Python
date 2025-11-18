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
	import math
	import random

	print()

	# TODO: figure out how see++ worked, will probably give different results

	# TODO: does starting at 0 0 skew the result

	# TODO: add a z dimension

	#  rmdir(path, *, dir_fd=None)

	pi = math.pi

	startx = 0
	starty = 0

	rotate = []
	length = []

	

	# six sided star
	swap = True
	swap = False
	if swap == True:
		line = True
		rotate.append(7.0)
		rotate.append(7.0)
		rotate.append(29.0)
		rotate.append(49.0)
		length.append(0.017000000923871994)
		length.append(0.7820002436637878)
		length.append(0.5950000286102295)
		length.append(0.5950000286102295)

	this = True
	#this = False
	if this == True:
		line = True
		#rotate.append(23)
		#rotate.append(17)
		#length.append(0.5)
		#length.append(0.5)

		rotate.append(7.0)
		rotate.append(2.0)
		rotate.append(7.0)
		length.append(0.10200001299381256)
		length.append(0.017000000923871994)
		length.append(0.17000003159046173)

	this = True
	this = False
	if this == True:
		line = True
		rotate.append(5.0)
		#length.append((2.0 * math.pi) / 360.0)
		length.append(.068)
		rotate.append(8.0)
		#length.append((2.0 * math.pi) / 360.0)
		length.append(.119)
		rotate.append(8.0)
		#length.append((2.0 * math.pi) / 360.0)
		length.append(.068)
		

	rando =  True
	rando = False
	if rando == True:
		line = True
		random.seed()
		rand = random.randint(2, 10)
		#rand = 6
		for a in range(rand):
			random.seed()
			angl = random.random()
			angl *= 40.0
			########################
			if angl >= 1.0:
				angl = math.floor(angl)
			else:
				angl = 1
			rotate.append(angl)
			random.seed()
			leng = random.random()
			########################
			leng *= 10.0
			leng *= (2.0 * math.pi) / 360.0
			length.append(leng)

		# [25, 10, 19]
		# [0.0748187546554903, 0.07564669369654953, 0.007874560826860545]

		# [31, 22, 28]
		# [0.043225342411075056, 0.1695471642427596, 0.10787568131055468]

		# [10, 26]
		# [0.14925600854171744, 0.14724538035241183]

		# [1.0, 25, 6]
		# [0.001881957911782393, 0.16331741514009868, 0.11470299117705007]

		# [9, 17, 33]
		# [0.0023971820415967177, 0.09051212820845325, 0.06413653903529035]

		# rotate = [35, 30, 18, 28, 18, 10]
		# length = [0.008279849869246115, 0.12868128462883255, 0.12511175339008412, 0.028536641031640077, 0.09362344305371632, 0.1507844719754551]

		# [5, 37, 21]
		# [0.020608035967804784, 0.0482236254935739, 0.0010273474160629535]

		# [25, 19]
		# [0.039058447245568215, 0.07847879015833764]

		# [8, 39]
		# [0.08327506678444697, 0.04927283790866379]

		# [27, 14, 28]
		# [0.030259275237863904, 0.13745721822707657, 0.08800663949399243]

		# [30, 38, 38, 29, 30, 24, 22, 20, 2]
		# [0.09167653001429754, 0.02388299280918569, 0.14310383744318633, 0.039189255028440596, 0.10838244222830357, 0.10919341559532851, 0.030802315041190707, 0.17278763831368962, 0.031581857634083645]

		print(rotate)
		print(length)

	frequenc = True
	frequenc = False
	if frequenc == True:

		freq = []

		random.seed()
		#rand = random.randint(2, 10)
		rand = 2
		for a in range(rand):
			random.seed()
			freq.append(5.0 * random.random())
		t = 0.0
		incr = 0.01
		vertList = []
		i = 1000
		#i = 720
		while i > 0:

			x = 0.0
			y = 0.0
			for a in range(rand):
				x += math.cos(t * freq[a] * 2.0 * pi)
				y += math.sin(t * freq[a] * 2.0 * pi)
			vertList.append((x, y, 0.0))
			
			t += incr
			i -= 1

		print(freq)

		freq = [2.5, .25]
		# freq = [0.25498623289132605, 2.511701484329491]

		edgeList = Math.EdgeLine(len(vertList))
		Blen.Uplo([vertList, edgeList, []])

		line = False

		# [1.9084712687163914, 4.242192949032859]

	# [13, 27, 9, 37, 5, 1.0]
	# [0.04339722262783449, 0.13145133763109193, 0.08264260142923065, 0.02281377151391625, 0.17289695054813609, 0.039431206048090306]

	# [2, 4, 24]
	# [0.0423629924669904, 0.14878765285792825, 0.07404754427252873]

	read_file = True
	read_file = False
	if read_file == True:
		filenum = python.file_to_lines("filenum")
		filenum = int(filenum[0])
		rotate = python.file_to_lines("out/" + blender.pad(filenum))
		length = rotate[1].split(" ")
		lenn = []
		for thing in length:
			lenn.append(float(thing))
		length = lenn
		rotn = []
		rotate = rotate[0].split(" ")
		for thing in rotate:
			rotn.append(float(thing))
		rotate = rotn

	degrees = []
	for a in range(len(rotate)):
		degrees.append(0)

	
	
	if line == True:

		startx = 0.0
		starty = 0.0

		dir_ = 0
		#switAngl = 45.0
		#lastAngl = 45.0
		#lastVect = (0.0, 0.0, 0.0)
		#lastVect = 0
		lastQuad = 0
		swit = False
		switch = True
		switch = False

		beginx = startx
		beginy = starty
		vert_list = []
		#i = 18000
		i = 720
		while i != 0:
			endx = length[0] * math.cos(math.radians(degrees[0]))
			endy = length[0] * math.sin(math.radians(degrees[0]))
			for a in range(1, len(rotate)):
				endx += length[a] * math.cos(math.radians(degrees[a]))
				endy += length[a] * math.sin(math.radians(degrees[a]))
			endx += beginx
			endy += beginy
			vert_list.append((beginx, beginy, 0.0))


			if switch == True:
				dire = Math.Vect((beginx, beginy, 0.0), (endx, endy, 0.0))
				angl = math.degrees(math.atan2(dire[1], dire[0]))
				while angl < 0.0:
					angl += 360.0
				#if dir_ == 0 and angl >= direAngl:
				#if angl >= dir_ * lastAngl:
				#	swit = not swit
				quad = 0
				if angl < 90.0:
					quad = 0
				if angl >= 90.0 and angl < 180.0:
					quad = 1
				elif angl >= 180.0 and angl < 270.0:
					quad = 2
				else:
					quad = 3

				# switch every half circle
				"""
				if quad == 1 and lastQuad == 0:
					swit = not swit
					lastQuad = 1
				if quad == 3 and lastQuad == 1:
					swit = not swit
					#lastQuad = 0
				"""

				# switch every half circle
				"""
				if quad == 1 and lastQuad == 0:
					swit = not swit
					lastQuad = 1
				if quad == 2 and lastQuad == 1:
					swit = not swit
					#lastQuad = 0
				"""

				# switch every quarter?
				if quad == 2 and lastQuad == 0:
					swit = not swit
					lastQuad = 1
				if quad == 3 and lastQuad == 1:
					swit = not swit
					lastQuad = 0
				

				#if quad != dir_:
				#	swit = not swit

				#lastVect = quad - 1




			for a in range(len(rotate)):
				#print(swit)
				if swit == False:
					degrees[a] += rotate[a]
				else:
					degrees[a] -= rotate[a]

			

			beginx = endx
			beginy = endy
			i -= 1

		vert_list.append((beginx, beginy, 0.0))
		edge_list = Math.EdgeLine(len(vert_list))
		Blen.Uplo([vert_list, edge_list, []])

		Blen.OrigGeom()
		Blen.Loca((0.0, 0.0, 0.0))

		#bpy.ops.object.modifier_add(type='SKIN')

		#Blen.Mate(colo = (1.0, 1.0, 1.0), use_shadeless = True)

	if read_file == True:
		bpy.ops.wm.save_as_mainfile(filepath= "out/" + blender.pad(filenum) + ".blend", check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', compress=False, relative_remap=True, copy=False, use_mesh_compat=False)


main()

