
def JoysNorm(valu, thre, maxi):
	if valu < 0:
		valu += thre
	else:
		valu -= thre
	valu /= (maxi - thre)
	return valu

def main():
	import bge
	import math
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	tole = 0.0001
	up__ = 0.0
	righ = 0.0
	keyb = owne["keyb"]
	joys = owne["joys"]
	# TODO
	keybActi = True
	magn = 0.0
	if joys == True:
		maxi = 2 ** 15 - 1
		thre = owne["joysThre"]
		if owne.sensors["RIGHTAXIS"].positive:
			keybActi = False
			righ = JoysNorm(owne.sensors["RIGHTAXIS"].axisSingle, thre, maxi)
		else:
			righ = 0.0
		if owne.sensors["UPAXIS"].positive:
			keybActi = False
			up__ = JoysNorm(-owne.sensors["UPAXIS"].axisSingle, thre, maxi)
		else:
			up__ = 0.0
	if keyb == True:
		inpuRighPrev = owne["inpuRighPrev"]
		inpuUp__Prev = owne["inpuUp__Prev"]
		# TODO: a is ""weak"", w is ""weak"". might depend on sensor order
		if cont.sensors['A_T'].positive:
			inpuRighPrev = -1.0
		if cont.sensors['D_T'].positive:
			inpuRighPrev = 1.0
		if cont.sensors['W_T'].positive:
			inpuUp__Prev = 1.0
		if cont.sensors['S_T'].positive:
			inpuUp__Prev = -1.0
		owne["inpuRighPrev"] = inpuRighPrev
		owne["inpuUp__Prev"] = inpuUp__Prev
		if cont.sensors['A'].positive:
			righ = -1.0
			if inpuRighPrev > 0.0:
				if cont.sensors['D'].positive:
					righ = 1.0
			magn = 1.0
		elif cont.sensors['D'].positive:
			righ = 1.0
			magn = 1.0
		if cont.sensors['W'].positive:
			up__ = 1.0
			if inpuUp__Prev < 0.0:
				if cont.sensors['S'].positive:
					up__ = -1.0
			magn = 1.0
		elif cont.sensors['S'].positive:
			up__ = -1.0
			magn = 1.0
	leftShif = owne["leftShif"]
	if keybActi == True:
		if owne.sensors["LEFT_SHIFT"].positive:
			leftShif = not leftShif
		if leftShif == False:
			if magn == 1.0:
				magn = 0.7
	else:
		magn = (righ * righ + up__ * up__) ** 0.5
	owne["leftShif"] = leftShif
	owne["inpuMagn"] = magn
	owne["inpuDire"] = math.degrees(math.atan2(up__, righ) - math.pi / 2.0)
	keybActi = True
	if joys == True:
		maxi = 2 ** 15 - 1
		thre = owne["joysThre"]
		if owne.sensors["joysAxisRigh"].positive:
			keybActi = False
			axisRigh = JoysNorm(owne.sensors["joysAxisRigh"].axisSingle, thre, maxi)
			axisRigh /= bge.render.getWindowWidth()
			# TODO: look up
			axisRigh *= 50.0
			owne["axisRigh"] = axisRigh
		else:
			owne["axisRigh"] = 0.0
		if owne.sensors["joysAxisUp__"].positive:
			keybActi = False
			axisUp__ = JoysNorm(owne.sensors["joysAxisUp__"].axisSingle, thre, maxi)
			axisUp__ /= bge.render.getWindowWidth()
			# TODO: look up
			axisUp__ *= 50.0
			owne["axisUp__"] = axisUp__
		else:
			# TODO: mouse
			owne["axisUp__"] = 0.0
	if keyb == True:
		if keybActi == True:
			# TODO: call this mous
			if owne.sensors["look"].positive:
				axisRighPrev = owne["axisRighPrev"]
				difx = bge.logic.mouse.position[0] - axisRighPrev
				sens = owne["lookX___Sens"]
				difx *= sens
				owne["axisRigh"] = difx
				axisUp__Prev = owne["axisUp__Prev"]
				dify = bge.logic.mouse.position[1] - axisUp__Prev
				# TODO: apply to joystick
				sens = owne["lookY___Sens"]
				dify *= sens
				owne["axisUp__"] = dify
			# TODO: see if this still works with tuto 5
			mousCentX___ = owne["mousCentX___"]
			mousCentY___ = owne["mousCentY___"]
			if mousCentX___ and mousCentY___:
				bge.logic.mouse.position = (0.5, 0.5)
				owne["axisRighPrev"] = 0.5
				owne["axisUp__Prev"] = 0.5
			else:
				if mousCentX___:
					bge.logic.mouse.position = (0.5, bge.logic.mouse.position[1])
					owne["axisRighPrev"] = 0.5
				else:
					owne["axisRighPrev"] = bge.logic.mouse.position[0]
				if mousCentY___:
					bge.logic.mouse.position = (bge.logic.mouse.position[0], 0.5)
					owne["axisUp__Prev"] = 0.5
				else:
					owne["axisUp__Prev"] = bge.logic.mouse.position[1]
	if owne.sensors["clic"].positive:
		#print("here")
		owne["clic"] = True
main()
