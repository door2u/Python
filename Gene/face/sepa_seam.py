
	# index 0: name of the vertex group
	# other indices: names of vertex groups that border the vertex group
	overlap_ = []
	overlap_.append(["neck", "chin", "jaw"])
	overlap_.append(["chin", "neck", "jaw", "mouth", "cheeks_lower"])
	overlap_.append(["jaw", "neck", "chin", "mouth", "cheeks_lower"])
	overlap_.append(["mouth", "chin", "lips", "jaw", "nose", "cheeks_lower"])
	overlap_.append(["lips", "mouth"])
	overlap_.append(["cheeks_lower", "chin", "mouth", "cheeks_upper", "nose", "jaw"])
	overlap_.append(["cheeks_upper", "cheeks_lower", "nose", "eyesockets", "brow"])
	overlap_.append(["nose", "eyesockets", "mouth", "cheeks_lower", "cheeks_upper", "brow"])
	overlap_.append(["eyesockets", "eyes", "nose", "brow", "cheeks_upper"])
	overlap_.append(["eyes", "eyesockets"])
	overlap_.append(["brow", "eyesockets", "nose", "cheeks_upper", "forehead"])
	overlap_.append(["forehead", "brow"])

	# get each border group
	# get each group

	seam = []

	for b in range(0, len(overlap_[grou])):
		Blen.Sele("face")
		Blen.Dupl()
		### get a section
		Blen.VertDese()
		Blen.VertGrouSele(overlap_[grou][b])
		Blen.Edit()
		bpy.ops.mesh.select_all(action = 'INVERT')
		Blen.Edit()
		Blen.VertDele()
		Blen.Name(overlap_[grou][b])

		if b > 0:
			#Blen.Sele(over[0])
			vert = Blen.VertList()
			#vertList += vert
			seam.append([])
			for c in range(len(vert)):
				#seam.append([vert[a][0], vert[a][1], vert[a][2], a, over[0]])
				#seam[b - 1].append([vert[c][0], vert[c][1], vert[c][2], c, overlap_[grou][b]])
				#seam[b - 1].append((vert[c][0], vert[c][1], vert[c][2]))
				seam[b - 1].append([vert[c][0], vert[c][1], vert[c][2], c])
		else:
			vertList = Blen.VertList()
			c = 0
			while c < len(vertList) - 1:
				if vertList[c][0] == vertList[c + 1][0]:
					if vertList[c][1] > vertList[c + 1][1]:
						temp = vertList[c]
						vertList[c] = vertList[c + 1]
						vertList[c + 1] = temp
						c = -1
				c += 1
			c = 0
			while c < len(vertList) - 1:
				if vertList[c][0] == vertList[c + 1][0]:
					if vertList[c][1] == vertList[c + 1][1]:
						if vertList[c][2] > vertList[c + 1][2]:
							temp = vertList[c]
							vertList[c] = vertList[c + 1]
							vertList[c + 1] = temp
							c = -1
				c += 1

	#seam = []
	#for over in overlap_:
	#	Blen.Sele(over[0])
	#	vert = Blen.VertList()
	#	vertList += vert
	#	for a in range(len(vert)):
	#		seam.append([vert[a][0], vert[a][1], vert[a][2], a, over[0]])

	for b in range(len(seam)):
		# TODO: make a VectSort() function
		seam[b] = sorted(seam[b])
		c = 0
		while c < len(seam[b]) - 1:
			if seam[b][c][0] == seam[b][c + 1][0]:
				if seam[b][c][1] > seam[b][c + 1][1]:
					temp = seam[b][c]
					seam[b][c] = seam[b][c + 1]
					seam[b][c + 1] = temp
					c = -1
			c += 1
		c = 0
		while c < len(seam[b]) - 1:
			if seam[b][c][0] == seam[b][c + 1][0]:
				if seam[b][c][1] == seam[b][c + 1][1]:
					if seam[b][c][2] > seam[b][c + 1][2]:
						temp = seam[b][c]
						seam[b][c] = seam[b][c + 1]
						seam[b][c + 1] = temp
						c = -1
			c += 1

		# TODO: slow
		seamList = []
		for c in range(len(vertList)):
			for d in range(len(seam[b])):
				#print(vertList[c], seam[b][d])
				if vertList[c][0] == seam[b][d][0] and vertList[c][1] == seam[b][d][1] and vertList[c][2] == seam[b][d][2]:
					seamList.append(seam[b][d])

		"""
		coun = 0
		c = len(seam[b]) - 1
		while c >= 1:
			if seam[b][c][0] == seam[b][c - 1][0] and seam[b][c][1] == seam[b][c - 1][1] and seam[b][c][2] == seam[b][c - 1][2]:
				coun += 1
			else:
				if coun == 0:
					seam[b].pop(c)
				coun = 0
			c -= 1
		if coun == 0:
			seam[b].pop(0)
		"""

		seam[b] = seamList[:]

	#print(seam)
	# find nodes
	# TODO: should vertList be checked
	for b in range(len(seam) - 1):
		for d in range(b + 1, len(seam)):
			for c in range(len(seam[b])):
				for e in range(len(seam[d])):
					if seam[b][c][0] == seam[d][e][0] and seam[b][c][1] == seam[d][e][1] and seam[b][c][2] == seam[d][e][2]:
						#print(b, d + 1)
						seam[b][c].append(d + 1)
						seam[b][c].append(e)

	
				
	for b in range(len(seam)):
		#seamList = seam[b][:]
		line = []
		for c in range(len(seam[b])):
			#line.append(str(seamList[b][0]) + " " + str(seamList[b][1]) + " " + str(seamList[b][2]) + " " + str(seamList[b][3]) + " " + seamList[b][4])
			#line.append(str(seamList[c][0]) + " " + str(seamList[c][1]) + " " + str(seamList[c][2]))
			appe = ""
			for d in range(len(seam[b][c])):
				appe += str(seam[b][c][d])
				if d < len(seam[b][c]) - 1:
					appe += " "
			line.append(appe)
		Pyth.LineTo__File(line, "face/seam/" + overlap_[grou][0] + "_" + overlap_[grou][b + 1])


	"""

	brea = False
	grouOrde = overlap_[grou][1 : len(overlap_[grou]) - 1]
	for a in range(len(grouOrde)):
		#if overlap_[a]
		for b in range(len(overlap_)):
			if overlap_[b][0] == grou[a]:
				if b > grou:
					grouOrde.insert(a, overlap_[grou][0]
					brea = True
					break
		if brea: break
	"""

	# read seam file
	#seamList = Pyth.FileTo__Line("face/seam/seam")
	# each line should be a list of vertices that correspond to each group, -1 for unused groups
	# 

	

	
	#for a in range(len(seam)):
	#	
	#Pyth.LineTo__File(line, "face/seam/" + overlap_[grou][0])

	Blen.Sele(overlap_[grou][0])

	# duplicate mesh
	#Blen.Sele("face")
	#Blen.Dupl()
	### get a section
	#Blen.VertDese()
	#Blen.VertGrouSele(overlap_[grou][0])
	#Blen.Edit()
	#bpy.ops.mesh.select_all(action='INVERT')
	#Blen.Edit()
	#Blen.VertDele()

