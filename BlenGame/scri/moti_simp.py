import bge
cont = bge.logic.getCurrentController()
scen = bge.logic.getCurrentScene()
owne = cont.owner
f = scen.objects[owne.name + ".forward"]["pathChec"]
l = scen.objects[owne.name + ".left"]["pathChec"]
b = scen.objects[owne.name + ".back"]["pathChec"]
r = scen.objects[owne.name + ".right"]["pathChec"]
if owne.sensors['W'].positive and f:
	cont.activate(owne.actuators['W'])
	owne["dire"] = 2
else:
	cont.deactivate(owne.actuators['W'])
if owne.sensors['A'].positive and l:
	cont.activate(owne.actuators['A'])
	owne["dire"] = 0
else:
	cont.deactivate(owne.actuators['A'])
if owne.sensors['S'].positive and b:
	cont.activate(owne.actuators['S'])
	owne["dire"] = 3
else:
	cont.deactivate(owne.actuators['S'])
if owne.sensors['D'].positive and r:
	cont.activate(owne.actuators['D'])
	owne["dire"] = 1
else:
	cont.deactivate(owne.actuators['D'])
if not owne.sensors['W'].positive and not owne.sensors['A'].positive and not owne.sensors['S'].positive and not owne.sensors['D'].positive:
	owne["dire"] = -1
