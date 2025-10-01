
def Pad_(numb):
	retu = ""
	if numb < 100:
		retu += "0"
	if numb < 10:
		retu += "0"
	retu += str(numb)
	return retu

def main():

	import bge
	import math
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner

	startx = 0
	starty = 0

	rota = []
	leng = []

	a = 0
	for a in range(10):
		obje = scen.objects["loop." + Pad_(a)]
		if obje["acti"] == True:
			rota.append(obje["rota"])
			leng.append(obje["leng"])
			scen.objects["high." + Pad_(a)].visible = True
		else:
			scen.objects["high." + Pad_(a)].visible = False

	loop = 720

	degrees = []
	for a in range(len(rota)):
		degrees.append(0)

	startx = 0.0
	starty = 0.0

	beginx = startx
	beginy = starty	

	lowestx = 1000.0
	lowesty = 1000.0
	highestx = -1000.0
	highesty = -1000.0

	vert_list = []
	i = loop
	while i != 0:
		if beginx < lowestx:
			lowestx = beginx
		if beginx > highestx:
			highestx = beginx
		if beginy < lowesty:
			lowesty = beginy
		if beginy > highesty:
			highesty = beginy
		endx = leng[0] * math.cos(math.radians(degrees[0]))
		endy = leng[0] * math.sin(math.radians(degrees[0]))
		for a in range(1, len(rota)):
			endx += leng[a] * math.cos(math.radians(degrees[a]))
			endy += leng[a] * math.sin(math.radians(degrees[a]))
		endx += beginx
		endy += beginy
		for a in range(len(rota)):
			degrees[a] += rota[a]
		bge.render.drawLine((beginx, beginy, 0.0), (endx, endy, 0.0), (0.0, 1.0, 0.0))
		beginx = endx
		beginy = endy
		i -= 1

	scen.objects["Camera"].worldPosition[0] = lowestx + (highestx - lowestx) / 2.0
	scen.objects["Camera"].worldPosition[1] = lowesty + (highesty - lowesty) / 2.0
	scen.objects["base"].worldPosition[0] = lowestx + (highestx - lowestx) / 2.0
	scen.objects["base"].worldPosition[1] = lowesty + (highesty - lowesty) / 2.0

	load = owne["load"]
	if load == True:
		for a in range(10):
			obje = scen.objects["loop." + Pad_(a)]
			obje.visible = True
		owne["load"] = False

	if owne.sensors["spac"].positive:
		a = 0
		for a in range(10):
			obje = scen.objects["loop." + Pad_(a)]
			if obje["acti"]:
				print("rotate.append(" + obje["rota"] + ")")
		a = 0
		for a in range(10):
			obje = scen.objects["loop." + Pad_(a)]
			if obje["acti"]:
				print("length.append(" + obje["leng"] + ")")

main()

