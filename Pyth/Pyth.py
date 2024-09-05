
def Swap(firs, seco):
	temp = firs
	firs = seco
	seco = temp
	return firs, seco

#######################

# read from a FILE. STRIP LINES
def FileTo__Line(filePath, stri = True):
	fileObje = open(filePath, mode = "r")
	retu = fileObje.read()
	fileObje.close()
	if stri == True:
		retu = retu.strip()
	retu = retu.split("\n")
	return retu

# write a LIST OF STRINGS to a FILE. mode defaults to "w" for write but can be set to "a" for append. other flags can be set as well
def LineTo__File(line, filePath, mode = "w"):
	fileObje = open(filePath, mode = mode)
	writ = ""
	a = 0
	while a < len(line):
		writ += line[a] + "\n"
		a += 1
	fileObje.write(writ)
	fileObje.close()

# return the file name from a FILE PATH
def FileName(path):
	import os
	retu = path.split(os.sep)
	return retu[len(retu) - 1]

#######################

# convert a STRING to a bool
def StriTo__Bool(stri):
	retu = False
	if len(stri) > 0:
		if stri[0] == "T" or stri[0] == "t" or stri[0] == "1":
			valu = True
	return retu

# convert a STRING to a tuple
def StriTo__Tupl(stri, cast = "f"):
	retu = stri.split("(")
	retu = retu[1]
	retu = retu.split(")")
	retu = retu[0]
	retu = retu.split(",")
	if cast == "f":
		for a in range(len(retu)):
			retu[a] = float(retu[a])
	if cast == "i":
		for a in range(len(retu)):
			retu[a] = int(retu[a])
	return tuple(retu)

# convert a LIST OF STRINGS into a list to tuples
# TODO: update
"""
def StriListTo__Tupl(striList, cast = "f"):
	retu = []
	a = 0
	while a < len(striList):
		retu.append(StriTo__Tupl(striList[a], cast = cast))
		a += 1
	return retu
"""

def StriListTo__Tupl(striList, cast = "f"):
	retu = []
	#striList = 
	retuStri = ""
	copy = False
	a = 0
	while a < len(striList):
		if striList[a] == "(":
			copy = True
		if copy == True:
			retuStri += striList[a]
		if striList[a] == ")":
			copy = False
			retu.append(retuStri)
			retuStri = ""
		a += 1
	a = 0
	while a < len(retu):
		retu[a] = StriTo__Tupl(retu[a], cast = cast)
		a += 1
	return retu

"""
# TODO: this might not be needed if there aren't any scripts that depend on it
def TuplListTo__Stri(list):
	retu = []
	for a in range(len(list)):
		retu.append(str(list[a]))
	return retu
"""

def TuplListTo__Stri(list, remoBrac = True):
	retu = str(list)
	if remoBrac == True:
		retu = retu[1:len(retu) - 1]
	return retu

def StriListTo__Int_List(stri):
	stri = stri.replace("[", "")
	stri = stri.replace("]", "")
	stri = stri.split(",")
	for a in range(len(stri)):
		stri[a] = int(stri[a])
	return stri

#######################

# arrange a LIST from least to greatest, determined by a certain DIMENSION OR ELEMENT. arrange greatest to least if REVERSE is True
def SortDime(list, dime, reverse = False):
	if dime != 0:
		sortList = []
		a = 0
		while a < len(list):
			sortList.append([list[a][dime], a])
			a += 1
		sortList = sorted(sortList, reverse = reverse)
		retu = []
		a = 0
		while a < len(sortList):
			retu.append(list[sortList[a][1]])
			a += 1
		list = retu
	else:
		list = sorted(list, reverse = reverse)
	return list

# find the index of the smallest value in a LIST OF FLOATS OR INTEGERS larger than EXCLUDING
def Mini(valuList, excl = None):
	a = 0
	# index of the minimum value
	retu = -1
	miniValu = None
	while a < len(valuList):
		set_Mini = True
		if miniValu != None:
			if valuList[a] >= miniValu:
				set_Mini = False
			if excl != None:
				if valuList[a] <= excl:
					set_Mini = False
		if set_Mini == True:
			miniValu = valuList[a]
			retu = a
		a += 1
	return retu

# find the index of the largest value in a LIST OF FLOATS OR INTEGERS smaller than EXCLUDING
def Maxi(valuList, excl = None):
	a = 0
	# index of the minimum value
	retu = -1
	maxiValu = None
	while a < len(valuList):
		set_Maxi = True
		if maxiValu != None:
			if valuList[a] < maxiValu:
				set_Maxi = False
			if excl != None and valuList[a] >= excl:
				set_Maxi = False
		if set_Maxi == True:
			maxiValu = valuList[a]
			retu = a
		a += 1
	return retu

# purge a LIST. remove identical values
# TODO: slow
def Purg(lis_):
	retu = []
	a = 0
	while a < len(lis_):
		exis = False
		b = 0
		while b < len(retu):
			if retu[b] == lis_[a]:
				exis = True
			b += 1
		if exis == False:
			retu.append(lis_[a])
		a += 1
	return retu

# flatten a multi-dimensional LIST of lists or tuples into a single-dimensional list
def Flat(lis_):
	retu = []
	a = 0
	while a < len(lis_):
		if type(lis_[a]) == list or type(lis_[a]) == tuple:
			b = 0
			while b < len(lis_[a]):
				lis_.append(lis_[a][b])
				b += 1
		else:
			retu.append(lis_[a])
		a += 1
	return retu

# convert a LIST OF VARIABES to a COMMA-SEPARATED (or SPACE-SEPARATED, etc.) string
def ListTo__Stri(list = [], sepa = ", "):
	retu = ""
	a = 0
	while a < len(list):
		if str(list[a]) == "":
			retu += "None"
		else:
			retu += str(list[a])
		if a < len(list) - 1:
			retu += str(sepa)
		a += 1
	return retu

#######################

# given an INTEGER, convert to a string INTEGER characters long (eg, (100, 4) becomes "0100")
def Pad_(numb, digi):
	retu = ""
	a = 1
	while a < digi:
		if numb < 10 ** a:
			retu += "0"
		a += 1
	retu += str(numb)
	return retu

# split a STRING by a SEPARATOR and return the INDEX(th) element
def SpliInde(stri, sepa, inde):
	stri = stri.split(sepa)
	if len(stri) > inde:
		return stri[inde].strip()
	else:
		return str(inde)

# return an inclusive substring from a STRING. (similar to stri = stri[star:stop + 1])
def Sub_Stri(stri, star, stop):
	retu = ""
	while star < len(stri) and star <= stop:
		retu += stri[star]
		star += 1
	return retu

# return the starting index of a SUBSTRING in a STRING, beginning at INDEX STAR
def Find(stri, sear, star):
	a = star
	b = 0
	retu = -1
	while a < len(stri):
		if stri[a] == sear[b]:
			b += 1
		else:
			b = 0
		if b == len(sear) - 1:
			if stri[a + 1] == sear[b]:
				break
			else:
				b = 0
		a += 1
	if a < len(stri):
		retu = a - len(sear) + 1
	return retu

#######################

# dictionary to lines
# eg {"height":10.0, "count":2} becomes:
# <class 'float'>
# height
# 10.0
# <class 'int'>
# count
# 2
# if a dictionary value is a list or tuple it's contents must be the same data type
# this function won't store the '<' character. it's used to identify the start of a new entry
# if these functions cause problems use the pickle module
def DictTo__Line(dic_):
	retu = []
	ite_ = dic_.keys()
	for key_ in ite_:
		typ_ = type(dic_[key_])
		if typ_ != list and typ_ != tuple:
			retu.append(str(typ_))
		else:
			if len(dic_[key_]) > 0:
				if typ_ == list:
					typ_ = "<list "
				elif typ_ == tuple:
					typ_ = "<tuple "
				if type(dic_[key_][0]) == int:
					typ_ += "'int'>"
				elif type(dic_[key_][0]) == float:
					typ_ += "'float'>"
				elif type(dic_[key_][0]) == bool:
					typ_ += "'bool'>"
				elif type(dic_[key_][0]) == str:
					typ_ += "'float'>"
			else:
				typ_ = str(typ_)
			retu.append(typ_)
		retu.append(key_)
		if type(dic_[key_]) != list and type(dic_[key_]) != tuple:
			retu.append(str(dic_[key_]))
		else:
			for valu in dic_[key_]:
				retu.append(str(valu))
	return retu

# lines to dictionary, a list of strings, type \n key \n value \n [value \n...]
# eg a text file like this:
# <class 'float'>
# height
# 10.0
# <class 'int'>
# count
# 2
# returns {"height":10.0, "count":2}
# TODO: conf
def LineTo__Dict(line, conf = 1):
	retu = {}
	a = 0
	while a < len(line):
		if conf == 0:
			typ_ = line[a + 2]
		if conf == 1:
			typ_ = line[a]
		if Sub_Stri(typ_, 1, 4) != "list" and Sub_Stri(typ_, 1, 5) != "tuple":
			if conf == 0:
				key_ = line[a]
				valu = line[a + 1]
			if conf == 1:
				key_ = line[a + 1]
				valu = line[a + 2]
			if typ_ == "<class 'float'>":
				valu = float(valu)
			elif typ_ == "<class 'int'>":
				valu = int(valu)
			elif typ_ == "<class 'bool'>":
				valu = StriTo__Bool(valu)
			elif typ_ == "<class 'tuple'>":
				valu = StriTo__Tupl(valu)
			a += 3
		else:
			typ_ = typ_.split("'")
			if len(typ_) > 1:
				typ_ = typ_[1]
			lis_ = False
			if Sub_Stri(typ_, 1, 4) == "list":
				lis_ = True
			key_ = line[a + 1]
			a += 2
			valu = []
			while 1:
				if a < len(line):
					if len(line[a]) > 0:
						if line[a][0] != "<":
							if typ_ == "float":
								line[a] = float(line[a])
							elif typ_ == "int":
								line[a] = int(line[a])
							elif typ_ == "bool":
								line[a] = StriTo__Bool(line[a])
							elif typ_ == "tuple":
								line[a] = StriTo__Tupl(line[a])
							valu.append(line[a])
							a += 1
						else:
							break
				else:
					break
			if lis_ == False:
				valu = tuple(valu)
		retu.update({key_:valu})
	return retu

#######################

# dictionary to variables
# read a DICTIONARY and place each entry on the separate line of a string
# used for prepending variables to a python expression
def DictTo__Vari(dic):
	retu = ""
	ite = dic.keys()
	for key in ite:
		retu += key + " = "
		if type(dic[key]) == str:
			retu += "\""
		retu += str(dic[key])
		if type(dic[key]) == str:
			retu += "\""
		retu += "\n"
	return retu

# add escape characters to a STRING
def Esca(stri):
	retu = ""
	for a in range(len(stri)):
		if stri[a] == "\"":
			retu += "\\\""
		else:
			retu += stri[a]
	return retu

# add escape characters to \
def EscaPath(stri):
	retu = ""
	for a in range(len(stri)):
		if stri[a] == "\\":
			retu += "\\\\"
		else:
			retu += stri[a]
	return retu

# read a SCRIPT and convert it to a string
# used for python expressions
def ScriTo__Stri(scri):
	line = FileTo__Line(scri, stri = False)
	retu = ""
	for a in range(len(line) - 1):
		retu += Esca(line[a])
		if a < len(line) - 2:
			retu += "\n"
	retu += "\n"
	return retu

