
# TODO
def main():
	import bge
	import random
	cont = bge.logic.getCurrentController()
	scen = bge.logic.getCurrentScene()
	owne = cont.owner
	trig = owne["blinTrig"]
	if trig == 0:
		# TODO: pass
		mini = 3.0
		maxi = 8.0
		random.seed()
		rand = random.random()
		rang = maxi - mini
		rand *= rang
		rand += mini
		owne['blin'] = rand
		owne['blinTime'] = scen.objects[scen.name + "." + "scen_obje"]['timer']
		trig += 1
	if trig == 1:
		timer = scen.objects[scen.name + "." + "scen_obje"]["timer"]
		blin = owne["blin"]
		blinTime = owne['blinTime']
		if timer > blin + blinTime:
			scen.objects[owne.name + "." + "eyes.lids.closed"].visible = True
			mini = 3.0
			maxi = 8.0
			mini /= 20.0
			maxi /= 20.0
			random.seed()
			rand = random.random()
			rang = maxi - mini
			rand *= rang
			rand += mini
			owne['blin'] = rand
			owne['blinTime'] = scen.objects[scen.name + "." + "scen_obje"]['timer']
			trig += 1
	if trig == 2:
		timer = scen.objects[scen.name + "." + "scen_obje"]["timer"]
		blin = owne["blin"]
		blinTime = owne['blinTime']
		if timer > blin + blinTime:
			scen.objects[owne.name + "." + "eyes.lids.closed"].visible = False
			trig = 0
	own['blinTrig'] = trig

main()
