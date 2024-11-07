import importlib.util
import os

spec = importlib.util.spec_from_file_location("Modu", os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Modu" + os.sep + "Modu.py")
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

def main():

	print()

	expr = "(psi^/psi * /psi^psi)^2 + psi^/psi * /psi^psi = -e^(i * pi)"

	makeNode = True
	#makeNode = False
	mesh = True
	#mesh = False
	game = True
	game = False
	Node(expr, spee = 2, makeNode = makeNode, mesh = mesh, game = game)

####################

# spee - speed
# 2. fast. replace all instances of a conversion in an expression at once
# 1. slow. replace one instance at a time from left to right
# 0. thorough. replace a combination of all instances
def Node(expr, spee = 0, makeNode = True, mesh = True, game = True):
	import math
	# read node lists from a file
	equa = Pyth.FileTo__Line("data/equa")
	# TODO: make a class
	connList = []
	a = 0
	while a < len(equa):
		connList = Writ(connList, a, a + 1)
		a += 2
	iden = Pyth.FileTo__Line("data/iden")
	# convert iden to a list of lists
	a = len(iden) - 1
	while a > 0:
		iden[a - 1] = [iden[a - 1], iden[a]]
		iden.pop(a)
		a -= 2
	expr = Pyth.Whit(expr)
	expr = expr.split("=")
	if (expr[0] in equa) == False:
		equa.append(expr[0])
	if (expr[1] in equa) == False:
		equa.append(expr[1])
	equa, connList = PurgNode(equa, connList)
	new_ = len(equa)
	if makeNode == True:
		# TODO: will ExprPars and Join give all the ways a function can be broken apart and redefined
		a = 0
		while a < len(equa):
			#print("a", a)
			brea = False
			var1List = ExprPars(equa[a])
			b = 0
			while b < len(var1List):
				entr = var1List[b]
				expr = Join(entr, var1List)
				# check iden for conversions
				c = 0
				while c < len(iden):
					d = 0
					while d < 2:
						node = int(not bool(d))
						node = iden[c][node]
						conv = Conv(ExprPars(iden[c][d]), ExprPars(expr), node)
						if conv != "":
							repl = conv
							conn = -1
							equa, connList, brea = ExprRepl(equa, connList, a, expr, repl, len(var1List), conn, spee)
							if brea == True:
								a = -1
								break
						d += 1
					if brea == True:
						break
					c += 1
				if brea == False:
					# check equa for conversions
					c = 0
					while c < len(equa):
						if c != a:
							if expr == equa[c]:
								d = 0
								appe = False
								leng = len(connList[c])
								while d < leng:
									if d != c:
										if connList[c][d]:
											repl = equa[d]
											conn = d
											equa, connList, brea = ExprRepl(equa, connList, a, expr, repl, len(var1List), conn, spee)
											if brea == True:
												a = -1
												break
									d += 1
						if brea == True:
							break
						c += 1
				if brea == True:
					break
				b += 1
			a += 1
		print(equa)
		#for a in range(len(connList)):
		#	print(a, equa[a])
		#	print(connList[a])

	# TODO: untangle then write to a list to be loaded
	if mesh == True:
		import bpy
		locaList = [(-5.70644998550415, -4.864696502685547, 0.003027748316526413), (-5.701447010040283, -2.1761131286621094, -4.884600639343262e-05), (1.207383632659912, -2.967954158782959, -0.0336163192987442), (-10.208662033081055, -1.2175874710083008, -0.01423506997525692), (-3.910322666168213, 6.463778495788574, 0.0025204652920365334), (17.47657012939453, 3.987089157104492, 0.00567894522100687), (-3.873164653778076, 4.060976028442383, -0.027349984273314476), (18.463478088378906, -0.8006901741027832, -0.03203725814819336), (14.9710054397583, 1.4813480377197266, 0.019613375887274742), (-3.9243898391723633, 2.084589958190918, 0.013092147186398506), (1.3846049308776855, -0.6708745956420898, 0.010862449184060097)]
		# convert connList to edgeList
		edgeList = ConnTo__Edge(connList)
		if edgeList != []:
			Blen.Uplo([locaList, edgeList, []])
		for a in range(len(equa)):
			Blen.Text(equa[a])
			name = "text." + Blen.Pad_(a)
			Blen.Name(name)
			dime = bpy.context.object.dimensions
			xmin = Blen.Xyz_Most(axis = 0, reverse = False)
			ymin = Blen.Xyz_Most(axis = 1, reverse = False)
			Blen.Curs((xmin + dime[0] / 2.0, ymin + dime[1] / 2.0, 0.0))
			Blen.OrigCurs()
			Blen.Loca(locaList[a])

	if game == True:
		import bpy
		locaList = []
		radi = 0.0
		angl = 0.0
		for a in range(len(equa)):
			locaList.append((radi * math.cos(angl), radi * math.sin(angl), 0.0))
			radi += 0.75
			angl += 1.5
		coun = []
		for a in range(len(equa)):
			coun.append(0)
		BlenGame.Mous()
		BlenGame.FramExte()
		Blen.Sele("came")
		# scroll sensitivity
		scroSens = 5.0
		# logic sensor type
		sens = 'MOUSE'
		sensOpti = BlenGame.LogiSensOpti()
		sensDict = BlenGame.LogiSensDict(typ_ = sens)
		contDict = BlenGame.LogiContDict(typ_ = 'LOGIC_AND')
		actuDict = BlenGame.LogiActuDict(typ_ = 'MOTION')
		sensOpti["use_tap"] = True
		sensDict["mouse_event"] = 'WHEELUP'
		actuDict["offset_location"] = (0.0, 0.0, -scroSens)
		BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict, actuDict = actuDict)
		sensDict["mouse_event"] = 'WHEELDOWN'
		actuDict["offset_location"] = (0.0, 0.0, scroSens)
		BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict, actuDict = actuDict)
		a = 0
		for text in equa:
			Blen.Text(text)
			name = "text." + Blen.Pad_(a)
			Blen.Name(name)
			dime = bpy.context.object.dimensions
			xmin = Blen.Xyz_Most(axis = 0, reverse = False)
			ymin = Blen.Xyz_Most(axis = 1, reverse = False)
			Blen.Curs((xmin + dime[0] / 2.0, ymin + dime[1] / 2.0, 0.0))
			Blen.OrigCurs()
			Blen.Loca((0.0, 0.0, 0.0))
			Blen.Plan()
			Blen.Scal((dime[0] / 2.0, dime[1] / 2.0, 1.0))
			Blen.Name("plan." + Blen.Pad_(a))
			mate = Blen.Mate()
			bpy.data.materials[mate].use_transparency = True
			bpy.data.materials[mate].alpha = 0.0
			bpy.data.materials[mate].specular_alpha = 0.0

			sens = 'MOUSE'
			sensOpti = BlenGame.LogiSensOpti()
			sensDict = BlenGame.LogiSensDict(typ_ = sens)
			contDict = BlenGame.LogiContDict(typ_ = 'LOGIC_AND')
			actuDict = BlenGame.LogiActuDict(typ_ = 'PROPERTY')
			sensOpti["use_tap"] = True
			sensDict["mouse_event"] = 'MOUSEOVER'
			actuDict["mode"] = 'ASSIGN'
			actuDict["property"] = 'over'
			actuDict["value"] = 'True'
			BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict, actuDict = actuDict)
			sensOpti["invert"] = True
			actuDict["value"] = 'False'
			BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict, actuDict = actuDict)
			BlenGame.Prop(propName = "over", propType = 'BOOL')
			Blen.Pare(name)

			Blen.Sele(name)
			Blen.Loca(locaList[a])
			sensOpti = BlenGame.LogiSensOpti()
			contDict = BlenGame.LogiContDict()
			sensOpti["use_pulse_true_level"] = True
			contDict["text"] = "game.py"
			BlenGame.Logi(sensOpti = sensOpti, contDict = contDict)
			sens = 'MOUSE'
			sensOpti = BlenGame.LogiSensOpti()
			sensDict = BlenGame.LogiSensDict(typ_ = sens)
			sensOpti["use_tap"] = True
			sensDict["mouse_event"] = 'LEFTCLICK'
			BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, sensName = 'clic', contDict = "linkCont")
			sensOpti["invert"] = True
			BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, sensName = 'clii', contDict = "linkCont")
			sens = 'MOUSE'
			sensOpti = BlenGame.LogiSensOpti()
			sensDict = BlenGame.LogiSensDict(typ_ = sens)
			contDict = BlenGame.LogiContDict(typ_ = 'LOGIC_AND')
			actuDict = BlenGame.LogiActuDict(typ_ = 'PROPERTY')
			sensOpti["use_tap"] = True
			sensDict["mouse_event"] = 'MOUSEOVER'
			actuDict["mode"] = 'ASSIGN'
			actuDict["property"] = 'over'
			actuDict["value"] = 'True'
			BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict, actuDict = actuDict)
			sensOpti["invert"] = True
			actuDict["value"] = 'False'
			BlenGame.Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict, actuDict = actuDict)
			BlenGame.Prop(propName = "over", propType = 'BOOL')
			BlenGame.Prop(propName = "clic", propType = 'BOOL')
			BlenGame.Prop(propName = "drag", propType = 'BOOL')
			BlenGame.Prop(propName = "prex", propType = 'FLOAT')
			BlenGame.Prop(propName = "prey", propType = 'FLOAT')
			if a < new_:
				BlenGame.Prop(propName = "colo", propType = 'BOOL')
			else:
				BlenGame.Prop(propName = "colo", propType = 'BOOL', propValu = True)
			a += 1
		Blen.Sele("came")
		for a in range(len(connList)):
			for b in range(a + 1, len(connList[a])):
				if connList[a][b] == True:
					BlenGame.Prop(propName = "node." + Blen.Pad_(a) + "." + Blen.Pad_(coun[a]), propType = 'INT', propValu = b)
					coun[a] += 1
		for a in range(len(coun)):
			BlenGame.Prop(propName = "coun." + Blen.Pad_(a), propType = 'INT', propValu = coun[a])

def ExprRepl(equa, connList, inde, expr, repl, leng, conn, spee):
	brea = False
	exprNew_ = []
	# form a replaced expression
	if spee == 2:
		exprNew_ = [equa[inde].replace(expr, "(" + repl + ")")]
	if spee == 1:
		exprNew_ = [equa[inde].replace(expr, "(" + repl + ")", 1)]
	if spee == 0:
		# get all instances of expr
		find = FindAll_(equa[inde], expr)
		# replace all combinations
		baseList = []
		for a in range(len(find)):
			baseList.append(2)
		if len(baseList) > 0:
			end = baseList[0]
		a = 1
		while a < len(baseList):
			end *= baseList[a]
			a += 1
		a = 1
		while a < end:
			replList = Math.Coun(baseList, a)
			striNew_ = equa[inde]
			for b in range(len(replList)):
				if replList[b] == 1:
					striNew_ = StriReplAbov(striNew_, expr, "(" + repl + ")", find[b] - 1)
			exprNew_.append(striNew_)
			a += 1
	for exprNe__ in exprNew_:
		exprList = ExprPars(exprNe__)
		# expressions can keep growing and growing. only add if the expression is reduced
		if len(exprList) <= leng:
			exprNe__ = Join(exprList[0], exprList)
			# if its not in the list, add it and reset counters
			exis = Pyth.Exis(equa, exprNe__, inde = True)
			if exis[0] == False:
				# connect the nodes
				connList = Writ(connList, inde, len(equa))
				# add the new node
				equa.append(exprNe__)
				brea = True
				break
			else:
				# add a connection
				if conn != -1:
					connList = Writ(connList, inde, conn)
				else:
					connList = Writ(connList, inde, exis[1])
	return equa, connList, brea

def FindAll_(stri, find):
	retu = []
	ret_ = 0
	while ret_ != -1:
		ret_ = stri.find(find)
		if ret_ != -1:
			appe = ret_
			if len(retu) > 0:
				appe += retu[len(retu) - 1] + len(find)
			retu.append(appe)
			stri = stri[ret_ + len(find):len(stri)]
	return retu

# replace once higher than inde
def StriReplAbov(stri, find, repl, inde):
	fin_ = 0
	star = 0
	while fin_ <= inde and fin_ < len(stri) and fin_ != -1:
		fin_ = stri.find(find, star)
		star = fin_ + 1
	str1 = stri[fin_:len(stri)]
	str1 = str1.replace(find, repl, 1)
	stri = stri[0:fin_] + str1
	return stri

###################

# PARSING

# form a list of expressions from a larger expression
def ExprPars(expr):
	variList = [expr]
	brea = False
	while brea == False:
		brea = True
		for a in range(len(variList)):
			variList, appe = ExprSepaEncl(a, variList)
			if appe == True:
				brea = False
	operList = ["^", "*", "+"]
	for oper in operList:
		brea = False
		while brea == False:
			brea = True
			for a in range(len(variList)):
				variList, appe = ExprSepaVari(a, variList, oper = oper)
				if appe == True:
					brea = False
	for oper in operList:
		brea = False
		while brea == False:
			brea = True
			for a in range(len(variList)):
				variList, appe = ExprSepaOper(a, variList, oper = oper)
				if appe == True:
					brea = False
	return variList

def ExprSepaEncl(inde, variList):
	encl = Encl(variList[inde])
	# was a change to the list made
	appe = False
	while encl != None:
		appe = True
		variList[inde] = variList[inde].replace("(" + encl + ")", "@" + str(len(variList)), 1)
		variList.append(encl)
		encl = Encl(variList[inde])
	return variList, appe

def Encl(stri):
	retu = ""
	pareCoun = 0
	pareStar = False
	star = 0
	a = 0
	while a < len(stri):
		if stri[a] == ")":
			if pareCoun > 0:
				pareCoun -= 1
		if pareStar == True:
			if pareCoun == 0:
				retu = stri[star + 1:a]
				pareStar = False
				break
		if stri[a] == "(":
			pareCoun += 1
			if pareStar == False:
				star = a
			pareStar = True
		a += 1
	if a == len(stri):
		retu = None
	return retu

def ExprSepaVari(inde, variList, oper = "^"):
	variStri = Vari(variList[inde], oper = oper)
	# was a change to the list made
	appe = False
	a = 0
	while variStri != None:
		appe = True
		variList[inde] = ReplExpr(variList[inde], "@" + str(len(variList)), variStri)
		variList.append(variStri)
		variStri = Vari(variList[inde], oper = oper)
		a += 1
	return variList, appe

def Vari(expr, oper = "^"):
	retu = ""
	operFlag = False
	a = 0
	while a < len(expr):
		if expr[a].isnumeric():
			inde = False
			b = a
			while b >= 0:
				if expr[b] == "@":
					inde = True
					break
				if expr[b].isnumeric() == False:
					break
				b -= 1
			if inde == False:
				retu += expr[a]
		if expr[a] == "/" or expr[a] == "-" or expr[a].isalpha():
			retu += expr[a]
		if OperIs__(expr[a]) or a == len(expr) - 1:
			if expr[a] == oper:
				operFlag = True
			if operFlag and retu != "":
				break
		a += 1
	if a == len(expr):
		retu = None
	return retu

def ExprSepaOper(inde, variList, oper = "^"):
	sepa = Oper(variList[inde], oper = oper)
	# was a change to the list made
	appe = False
	while sepa != None:
		appe = True
		variList[inde] = ReplExpr(variList[inde], "@" + str(len(variList)), sepa)
		variList.append(sepa)
		sepa = Oper(variList[inde], oper = oper)
	return variList, appe

def Oper(expr = "", oper = "^"):
	stri = ""
	retu = []
	inde = -1
	a = 0
	while a < len(expr):
		if OperIs__(expr[a]):
			retu.append(stri)
			if inde != -1 and len(retu) > 2:
				break
			stri = ""
			if inde == -1 and expr[a] == oper:
				inde = len(retu)
		else:
			stri += expr[a]
		a += 1
	if a == len(expr) and stri != "":
		retu.append(stri)
	if inde != -1 and len(retu) > 2:
		retu = retu[inde - 1] + oper + retu[inde]
	else:
		retu = None
	return retu

# replace something thats not already an index
def ReplExpr(stri, repl, find):
	strc = stri
	shif = 0
	brea = False
	while True:
		inde = strc.find(find)
		if inde == -1:
			break
		indc = inde
		while indc >= 0:
			indc -= 1
			if strc[indc] == "@":
				break
			if strc[indc].isalnum() == False:
				brea = True
				
				break
		if brea == True:
			break
		if indc == -1:
			break
		while strc[inde].isnumeric():
			inde += 1
		strc = strc[inde + 1:len(strc)]
		shif += inde + 1
	if inde != -1:
		inde += shif
		strc = ""
		a = 0
		while a < inde + 0:
			strc += stri[a]
			a += 1
		strc += repl
		a += len(find)
		while a < len(stri):
			strc += stri[a]
			a += 1
	else:
		strc = stri
	return strc

#############

# REJOIN A PARSED EXPRESSION

def Join(expr, variList):
	while IndeHas_(expr):
		entr = Entr(expr)
		expr = IndeRepl(expr, entr, variList)
	return expr

def Entr(entr, inde = 0):
	retu = ""
	a = 0
	while a < len(entr):
		if entr[a] == "@":
			a += 1
			while a < len(entr) and entr[a].isnumeric():
				retu += entr[a]
				a += 1
			break
		a += 1
	if retu == "":
		retu = "-1"
	return int(retu)

def IndeRepl(entr, inde, variList):
	retu = ""
	star = -1
	end_ = -1
	inte = ""
	pare = False
	opel = ""
	a = IndeFind(entr, inde)
	while a >= 0:
		if entr[a] == "(":
			break
		if OperIs__(entr[a]):
			opel = entr[a]
			break
		a -= 1
	oper = ""
	if opel == "":
		a = IndeFind(entr, inde)
		if a != -1:
			while a < len(entr):
				if entr[a] == ")":
					break
				if OperIs__(entr[a]):
					oper = entr[a]
					break
				a += 1
	# TODO: have to consider l / r?
	if opel != "" or oper != "":
		if oper == "":
			oper = opel
		pare = ParePrec(variList[inde], oper)
	a = 0
	while a < len(entr):
		if entr[a] == "@":
			star = a
			a += 1
			while a < len(entr) and entr[a].isnumeric():
				inte += entr[a]
				a += 1
			end_ = a - 1
			if len(inte) > 0 and int(inte) == inde:
				break
		a += 1
	a = 0
	while a < len(entr):
		if a < star or a > end_:
			retu += entr[a]
		else:
			if pare:
				retu += "("
			retu += variList[inde]
			if pare:
				retu += ")"
			a = end_
		a += 1
	return retu

def IndeFind(entr, inde):
	retu = -1
	a = 0
	while a < len(entr):
		if entr[a] == "@":
			retu = a
			numb = ""
			a += 1
			while a < len(entr) and entr[a].isnumeric():
				numb += entr[a]
				a += 1
			if int(numb) == inde:
				break
			else:
				retu = -1
		a += 1
	return retu

def ParePrec(expr, oper):
	retu = False
	if oper != "":
		opee = OperType(expr)
		if opee != "":
			pre1 = Prec(oper)
			pre2 = Prec(opee)
			if pre1 >= pre2:
				retu = True
	return retu

# TODO: ()
def Prec(oper):
	retu = 0
	if oper == "^":
		retu = 3
	if oper == "*":
		retu = 2
	if oper == "+":
		retu = 1
	return retu

##############

# CONVERSION

# convert an expression (parsed into var2List) from one form (parsed into var1List) into a new form (node)
# a joined expression from var1List should have the same variables as node
def Conv(var1List, var2List, node):

	def ReplAppe(inde, variList, replList):
		join = Join(variList[inde], variList)
		join = PareStri(join)
		join = ExprPars(join)
		for joi_ in join:
			replList.append(joi_)
		return replList

	retu = ""
	rep1List = []
	rep2List = []
	if len(var1List) > 0:
		acco = []
		for a in range(len(var1List)):
			if IndeHas_Two_(var1List[a]):
				acco.append(False)
			else:
				acco.append(True)
		# to check. list of indices that need to be checked
		toc1 = [0]
		matcInde = -1
		if OperType(var1List[toc1[0]]) == OperType(var2List[0]):
			matcInde = 0
		if matcInde != -1:
			toc2 = [matcInde]
			while False in acco:
				appe = False
				ind1 = EntrList(var1List[toc1[0]])
				ind2 = EntrList(var2List[toc2[0]])
				matc = False
				commMatc = False
				ope1 = OperType(var1List[ind1[0]])
				ope2 = OperType(var2List[ind2[0]])
				if ope1 == "":
					# get the replacement
					rep1List = ReplAppe(ind1[0], var1List, rep1List)
					rep1List = ReplAppe(ind1[1], var1List, rep1List)
					rep2List = ReplAppe(ind2[0], var2List, rep2List)
					rep2List = ReplAppe(ind2[1], var2List, rep2List)
					acco[toc1[0]] = True
					# delete the matched indices
					toc1.pop(0)
					toc2.pop(0)
					# update toc1 toc2
					toc1.append(ind1[0])
					toc1.append(ind1[1])
					toc2.append(ind2[0])
					toc2.append(ind2[1])
				else:
					if ope1 == ope2:
						matc = True
					if matc == False:
						comm = Comm(ope1)
						# if comm check 0 1
						if comm == False:
							ope2 = OperType(var2List[ind2[1]])
							matc = True
							commMatc = True
						else:
							break
					# if a match has been made
					if matc:
						ope1 = OperType(var1List[ind1[1]])
						# if not comm, match same inde
						inde = 1
						# else match reverse inde
						if commMatc:
							inde = 0
						ope2 = OperType(var2List[ind2[inde]])
						if ope1 == ope2:
							acco[toc1[0]] = True
							# delete the matched indices
							toc1.pop(0)
							toc2.pop(0)
							# update toc1 toc2
							toc1.append(ind1[0])
							toc1.append(ind1[1])
							toc2.append(ind2[int(not bool(inde))])
							toc2.append(ind2[inde])
						else:
							break
			if not (False in acco):
				matc = True
				brea = False
				if len(rep1List) == len(rep2List) and len(rep1List) > 0:
					a = len(rep1List) - 1
					while a > 0:
						b = a - 1
						while b >= 0:
							if VariSame(rep1List[a], rep1List[b]):
								if VariSame(rep2List[a], rep2List[b]) == False:
									matc = False
									brea = True
									break
								if SignSame(rep1List[a], rep1List[b]) != SignSame(rep2List[a], rep2List[b]):
									matc = False
									brea = True
									break
								rep1List.pop(a)
								rep2List.pop(a)
								break
							b -= 1
						if brea == True:
							break
						a -= 1
				else:
					matc = False
				for a in range(len(rep1List)):
					typ1 = EntrType(rep1List[a])
					typ2 = EntrType(rep2List[a])
					if typ1 != typ2:
						matc = False
						break
					# TODO: this shouldnt happen. leaving for now in case it does
					if typ1 == 2:
						matc = False
						break
					if typ1 == 0:
						if rep1List[a] != rep2List[a]:
							matc = False
							break
				if matc:
					retuStri = node
					iden = Join(var1List[0], var1List)
					# remove sign from rep1List and move it to rep2List
					for a in range(len(rep1List)):
						sign = SignRead(rep1List[a])
						if len(sign) > 0:
							rep1List[a] = rep1List[a][1:len(rep1List[a])]
							rep2List[a] = sign + rep2List[a]
					for a in range(len(rep1List)):
						sigf, sigt = SignChan(iden, node, rep1List[a])
						find = rep1List[a]
						repl = rep2List[a]
						retuStri = retuStri.replace(find, repl)
					retu = ""
					a = 0
					while a < len(retuStri) - 1:
						if (retuStri[a] == "/" and retuStri[a + 1] == "/") or (retuStri[a] == "-" and retuStri[a + 1] == "-"):
							a += 2
						retu += retuStri[a]
						if a == len(retuStri) - 2:
							retu += retuStri[a + 1]
						a += 1	
	return retu

def IndeHas_Two_(expr):
	retu = False
	coun = 0
	for a in range(len(expr)):
		if expr[a] == "@":
			coun += 1
		if coun >= 2:
			retu = True
			break
	return retu

def EntrList(entr):
	retu = []
	retu.append(Entr(entr))
	if retu[0] != -1:
		# TODO: will an entry ever be something like @0^@0, or would it matter. maybe dont flatten exprpars
		entr = entr.replace("@" + str(retu[0]), "", 1)
		retu.append(Entr(entr))
	else:
		retu.append(-1)
	return retu

def PareStri(stri):
	stri = stri.replace("(", "")
	stri = stri.replace(")", "")
	return stri

def Comm(oper):
	retu = None
	if oper == "^":
		retu = False
	if oper == "*" or oper == "+":
		retu = True
	return retu

def VariSame(var1, var2):
	retu = False
	if EntrType(var1) == EntrType(var2):
		if EntrType(var1) == 0 or EntrType(var1) == 1:
			if len(var1) > 0:
				if var1[0] == "-":
					var1 = var1[1:len(var1)]
				elif var1[0] == "/":
					var1 = var1[1:len(var1)]
			if len(var2) > 0:
				if var2[0] == "-":
					var2 = var2[1:len(var2)]
				elif var2[0] == "/":
					var2 = var2[1:len(var2)]
			if var1 == var2:
				retu = True
	return retu

def SignSame(var1, var2):
	retu = False
	if len(var1) > 0 and len(var2) > 0:
		if (var1[0] == "/" and var2[0] == "/") or (var1[0] == "-" and var2[0] == "-") or (var1[0].isalnum() and var2[0].isalnum()):
			retu = True
	return retu

# True: entry is a number. False: entry is a variable or operation
# 0 if the entry is a number
# 1 if the entry is a var
# 2 if the entry holds indices
def EntrType(entr):
	retu = -1
	if len(entr) > 0:
		if entr[0].isnumeric():
			retu = 0
		if entr[0] == "/" or entr[0] == "-" or entr[0].isalpha():
			retu = 1
	if IndeHas_(entr):
		retu = 2
	return retu

def SignRead(entr):
	retu = ""
	if len(entr) > 0:
		if entr[0] == "/" or entr[0] == "-":
			retu = entr[0]
	return retu

def SignChan(iden, node, vari):
	# sign from
	sigf = ""
	# sign to
	sigt = ""
	inde = iden.find(vari)
	inde -= 1
	if inde >= 0:
		if iden[inde] == "-" or iden[inde] == "/":
			sigf = iden[inde]
	inde = node.find(vari)
	inde -= 1
	if inde >= 0:
		if node[inde] == "-" or node[inde] == "/":
			sigt = node[inde]
	return sigf, sigt

##############

# NODE FUNCTIONS

def Writ(connList, node, conn, unse = False):
	while len(connList) <= node or len(connList) <= conn:
		connList.append([])
	while len(connList[node]) <= conn:
		connList[node].append(False)
	while len(connList[conn]) <= node:
		connList[conn].append(False)
	connList[node][conn] = not unse
	connList[conn][node] = not unse
	return connList

def Read(connList, node, conn):
	retu = False
	if node < len(connList) and conn < len(connList[node]):
		retu = connList[node][conn]
	return retu

# remove identical nodes
def PurgNode(nodeList, connList):
	pop_List = []
	a = len(nodeList) - 1
	while a >= 1:
		b = 0
		while b < a:
			if nodeList[a] == nodeList[b]:
				# delete the node
				nodeList.pop(a)
				pop_List.append([a, b])
				break
			b += 1
		a -= 1
	a = 0
	while a < len(pop_List):
		b = len(connList) - 1
		while b >= 0:
			# remove the connection to the old node
			if pop_List[a][0] < len(connList[b]):
				connList[b].pop(pop_List[a][0])
			# copy old connections to the new node
			if Read(connList, pop_List[a][0], b):
				connList = Writ(connList, pop_List[a][1], b)
			b -= 1
		# remove the connection list for the node
		connList.pop(pop_List[a][0])
		a += 1
	return nodeList, connList

# convert a connList (connection list), ie [[False, True], [True]], to an edgeList, ie [[0, 1]]
def ConnTo__Edge(connList):
	retu = []
	a = 0
	while a < len(connList):
		b = a + 1
		while b < len(connList[a]):
			if connList[a][b] == True:
				retu.append([a, b])
			b += 1
		a += 1
	return retu

#################

# GENERAL FUNCTIONS

def OperType(entr):
	retu = ""
	for a in range(len(entr)):
		if OperIs__(entr[a]):
			retu = entr[a]
			break
	return retu

def OperIs__(char):
	return char == "^" or char == "*" or char == "+"

def IndeHas_(expr):
	retu = False
	for a in range(len(expr)):
		if expr[a] == "@":
			retu = True
			break
	return retu

##################

main()
