
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
	cont = bge.logic.getCurrentController()
	owne = cont.owner
	# SONG LOOP. two actuators have the same track.
	# play the first, then the second, then the first, etc.
	# each track has a reverb tail at the end that plays over the beginning of "itself".
	# TODO
	music = owne["audi"]
	if music >= 0:
		leng = owne["audiCoun"]
		if music < leng:
			t = owne["timer"]
			a = owne["audiTime"]
			if t >= a:
				looped = owne["audiLooped." + Pad_(music)]
				# if a track is to be looped, "loop" is true if the current track playing is the second version. loops have two tracks so that a music file can loop over its own audio tail
				if looped == True:
					this_loop = owne["audiLoop." + Pad_(music)]
				actu_name = owne["audiName." + Pad_(music)]
				if looped == True:
					if this_loop == True:
						actu_name += ".loop"
				cont.activate(owne.actuators[actu_name])
				if looped == True:
					this_loop = not this_loop
					owne["audiLoop." + Pad_(music)] = this_loop
				# set the trigger for the next loop to play
				time = owne["audiTime." + Pad_(music)]
				owne["audiTime"] = t + time
				if looped == False:
					music += 1
				owne["audi"] = music
		elif music == leng:
			t = owne["timer"]
			a = owne["audiTime"]
			if t >= a:
				music += 1
				owne["audi"] = music

main()

