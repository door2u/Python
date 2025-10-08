
#import functools

def PythLink(Pyth = None):
	return Pyth
def MathLink(Math = None):
	return Math
def BlenGameLink(BlenGame = None):
	return BlenGame
def HeadLink(Head = None):
	return Head
def BlenCommLink(blenComm = None):
	return blenComm
def BlenDireLink(blenDire = None):
	return blenDire

#################################################

# SELECTION

# select an object by NAME
def Sele(name, dese = True):
	import bpy
	scen = bpy.context.scene
	retu = None
	if name in Objects():
		retu = scen.objects[name]
		if dese == True:
			bpy.ops.object.select_all(action='DESELECT')
		# TODO: is this the right cutoff
		vers = bpy.app.version
		if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
			bpy.context.view_layer.objects.active = scen.objects[name]
			bpy.data.objects[name].select_set(True)
		else:
			scen.objects.active = scen.objects[name]
			scen.objects[name].select = True
	else:
		print("warning: " + name + " object not found")
	return retu

# select an object by NAME from another scene by NAME
def SeleOthe(objeName, scenName):
	import bpy
	scen = bpy.context.scene
	for obje in scen.objects:
		vers = bpy.app.version
		if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
			obje.select_set(False)
		else:
			obje.select = False
	scen = bpy.data.scenes[scenName]	
	# deselect all
	for obje in scen.objects:
		obje.select = False
	# select object
	scene.objects.active = scene.objects[objeName]
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		scene.objects[objeName].select_set(True)
	else:
		scene.objects[objeName].select = True
	return scene.objects[objeName]

def SeleAll_(action = 'SELECT'):
	import bpy
	bpy.ops.object.select_all(action = action)

#################################################

# OBJECT

# select child, then call, and pass PARENT NAME
def Pare(pare = ""):
	import bpy
	chil = bpy.context.object.name
	Sele(pare)
	# TODO: this should be a function
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.data.objects[chil].select_set(True)
	else:
		bpy.data.objects[chil].select = True
	bpy.ops.object.parent_set(type = 'OBJECT', xmirror = False, keep_transform = True)
	Sele(chil)

def PareList(pare = "", pareList = []):
	for chil in pareList:
		Sele(chil)
		Pare(pare)

def PareClea():
	import bpy
	bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

# select the first object, then call join, and pass the NAME of the second object. joined object inherits the name of the first object
def Join(name):
	import bpy
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.data.objects[name].select_set(True)
	else:
		bpy.data.objects[name].select = True
	bpy.ops.object.join()

# duplicate the selected object
def Dupl():
	import bpy
	bpy.ops.object.duplicate_move()

# delete the selected object
def Dele():
	import bpy
	bpy.ops.object.delete()

#################################################

# TRANSFORMS

# scale selected object by SCAL
def Scal(scal, proportional_size = 1.0):
	import bpy
	value = (scal[0], scal[1], scal[2])
	constraint_axis = (scal[0] != 1.0, scal[1] != 1.0, scal[2] != 1.0)
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.transform.resize(value = value, constraint_axis = constraint_axis, orient_type = 'GLOBAL')
	else:
		bpy.ops.transform.resize(value = value, constraint_axis = constraint_axis, constraint_orientation = 'GLOBAL')

# rotate the selected object by ROTA. set loca to TRUE for a local rotation. set PIVOT to CURSOR to translate the object around the z-axis of the cursor
def Rota(rota = (0.0, 0.0, 0.0), loca = False, pivo = ""):
	import bpy
	import math
	cons = 'GLOBAL'
	if loca == True:
		cons = 'LOCAL'
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.transform.rotate(value = math.radians(rota[0]), orient_axis = 'X', constraint_axis = (True, False, False), orient_type = cons)
		bpy.ops.transform.rotate(value = math.radians(rota[1]), orient_axis = 'Y', constraint_axis = (False, True, False), orient_type = cons)
		bpy.ops.transform.rotate(value = math.radians(rota[2]), orient_axis = 'Z', constraint_axis = (False, False, True), orient_type = cons)
	else:
		bpy.ops.transform.rotate(value = math.radians(rota[0]), axis = (1, 0, 0), constraint_axis = (True, False, False), constraint_orientation = cons)
		bpy.ops.transform.rotate(value = math.radians(rota[1]), axis = (0, 1, 0), constraint_axis = (False, True, False), constraint_orientation = cons)
		bpy.ops.transform.rotate(value = math.radians(rota[2]), axis = (0, 0, 1), constraint_axis = (False, False, True), constraint_orientation = cons)
	# pivot in z
	if pivo == "CURSOR":
		x = bpy.context.object.location[0] - bpy.context.scene.cursor_location[0]
		y = bpy.context.object.location[1] - bpy.context.scene.cursor_location[1]
		magn = Math.VectMagn((x, y))
		angl = math.atan2(y, x)
		angl += math.radians(rota[2])
		while angl > math.pi:
			angl -= 2.0 * math.pi
		x = math.cos(angl)
		y = math.sin(angl)
		bpy.context.object.location[0] = bpy.context.scene.cursor_location[0] + magn * x 
		bpy.context.object.location[1] = bpy.context.scene.cursor_location[1] + magn * y

# set ROTATION of the selected object
def RotaSet_(rota):
	import bpy
	import math
	bpy.context.object.rotation_euler = (math.radians(rota[0]), math.radians(rota[1]), math.radians(rota[2]))

# set the LOCATION of the selected object
# if loca is the name of another object, the selected object will be copied to the same location
def Loca(loca, worl = True):
	import bpy
	if type(loca) == str:
		if worl == True:
			cont = bpy.context.object.name
			Sele(loca)
		loca = LocaRead(worl = worl)
		if worl == True:
			Sele(cont)
	bpy.context.object.location = loca

# transfrom the selected object by SCALE, ROTATION, and LOCATION
def Tran(scal, rota, loca):
	Scal(scal)
	RotaSet_(rota)
	Loca(loca)

# TODO: update
# translate selected object
def Move(vect, prop = False):
	import bpy
	if prop:
		prop = 'ENABLED'
	else:
		prop = 'DISABLED'
	bpy.ops.transform.translate(value = vect, constraint_axis=(False, False, False), constraint_orientation='LOCAL', mirror=False, proportional = prop, proportional_edit_falloff='SMOOTH', proportional_size=1)

#############################################

# OBJECT OPERATIONS

def ApplScal():
	import bpy
	bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

def ApplRota():
	import bpy
	bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

def ApplLoca():
	import bpy
	bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)

def Appl():
	import bpy
	bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

def Conv():
	import bpy
	bpy.ops.object.convert(target='MESH')

##################################

# CURSOR

# set the cursor to a LOCATION
def Curs(loca):
	import bpy
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.context.scene.cursor.location = loca
	else:
		bpy.context.scene.cursor_location = loca

def CursRead():
	import bpy
	retu = None
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		retu = tuple(bpy.context.scene.cursor.location)
	else:
		retu = tuple(bpy.context.scene.cursor_location)
	return retu

# cursor to selected
def CursTo__Sele(edit = False, all_ = False):
	import bpy
	Math = MathLink()
	if all_ == False:
		if edit == False:
			x, y, z = LocaRead()
		else:
			aver = VertListSele()
			aver = VertLoca(aver)
			x, y, z = Math.VectAver(aver)
	else:
		aver = []
		for obje in bpy.context.scene.objects:
			sele = False
			vers = bpy.app.version
			if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
				if obje.select_get() == True:
					sele = True
			else:
				if obje.select == True:
					sele = True
			if sele == True:
				aver.append(tuple(obje.location))
		x, y, z = Math.VectAver(aver)
	Curs((x, y, z))

def CursTo__Vert(inde):
	Math = MathLink()
	x, y, z = VertLoca(inde)
	scal, rota, loca = TranRead()
	x, y, z = Math.Tran3d__((x, y, z), scal, rota, loca)
	Curs((x, y, z))

def CursTo__Edge(inde):
	Math = MathLink()
	x, y, z = EdgeLoca(inde)
	scal, rota, loca = TranRead()
	x, y, z = Math.Tran3d__((x, y, z), scal, rota, loca)
	Curs((x, y, z))

def CursTo__Poly(inde):
	Math = MathLink()
	x, y, z = PolyCent(inde)
	scal, rota, loca = TranRead()
	x, y, z = Math.Tran3d__((x, y, z), scal, rota, loca)
	Curs((x, y, z))

##################################

# ORIGIN

def OrigCurs():
	import bpy
	bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

def OrigGeom():
	import bpy
	bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

# set the origin of the selected object to a NEW LOCATION
def Orig(loca):
	Curs(loca)
	OrigCurs()

# set the origin of the selected object to a different object by NAME
def OrigCopy(name):
	import bpy
	cont = bpy.context.object.name
	Curs(bpy.data.objects[name].location)
	OrigCurs()
	Sele(cont)

# return the geometric location of the selected object without (permanently) changing it's origin
def LocaGeomRead():
	import bpy
	Curs(LocaRead())
	OrigGeom()
	retu = LocaRead()
	OrigCurs()
	return retu

#################################################

# MESH SELECTION

# switch to edit mode
def Edit():
	import bpy
	bpy.ops.object.editmode_toggle()

# select the indices of the vertices in a VERTEX LIST (list of integers)
def VertSele(vert, dese = True, mode = 0):
	import bpy
	# backup current context
	name = bpy.context.object.name
	mode = bpy.context.tool_settings.mesh_select_mode
	# TODO: where else should this be implemented? if a function doesn't that uses edit_mode, check mesh_select_mode
	if mode == 0:
		bpy.context.tool_settings.mesh_select_mode = (True, False, False)
	if mode == 1:
		bpy.context.tool_settings.mesh_select_mode = (False, True, False)
	if mode == 2:
		bpy.context.tool_settings.mesh_select_mode = (False, False, True)
	# create a new vertex group and add the vertices in the passed list to the new group
	VertGrou("temp", vert)
	# reselect the object
	Sele(name)
	# deselect all verts
	if dese:
		VertDese()
	# select the group created above
	VertGrouSele("temp")
	# delete the group
	bpy.ops.object.vertex_group_remove()
	# restore select mode
	bpy.context.tool_settings.mesh_select_mode = mode

# selected all the vertices of a selected object
def VertSeleAll_():
	import bpy
	Edit()
	bpy.ops.mesh.select_all(action = 'SELECT')
	Edit()

# deselect all vertices of the selected object
def VertDese():
	import bpy
	Edit()
	bpy.ops.mesh.select_all(action='DESELECT')
	Edit()

# select the polygon of the given INDEX
def PolySele(inde, dese = True):
	import bpy
	VertSele(PolyVert(inde), dese = dese, mode = 2)

# TODO: make a PolySeleList function. delete, reupload and join almost works except doubles need to be removed. automerge doesnt come into effect with join.
def PolyMark(polyList):
	import bpy
	#poly = []
	#if len(polyList) > 0:
	#	VertSele(PolyVert(polyList[0]), dese = True, mode = 2)
	name = bpy.context.object.name
	for a in range(0, len(polyList)):
		#poly.append([PolyVert(polyList[a]), bpy.context.object.data.polygons[polyList[a]].material_index])
		#VertSele(PolyVert(polyList[a]), dese = False, mode = 2)
		Sele(name)
		# TODO: world
		cent = bpy.context.object.data.polygons[polyList[a]].center
		#Curs(cent)
		Empt()
		Loca(cent)
	#for pol_ in poly:
	#	print(pol_)

def VertDele():
	import bpy
	Edit()
	bpy.ops.mesh.delete(type = 'VERT')
	Edit()

def PolyDele():
	import bpy
	Edit()
	bpy.ops.mesh.delete(type = 'FACE')
	Edit()

def VertGrou(name, lis_ = [], weig = 1.0):
	import bpy
	bpy.ops.object.vertex_group_add()
	grouNumb = -1
	for a in range(len(bpy.context.object.vertex_groups)):
		grouName = bpy.context.object.vertex_groups[a].name
		# TODO:
		# where else is this needed
		grouName = grouName.split(".")
		if len(grouName) > 0:
			if grouName[0] == 'Group':
				grouNumb = a
	bpy.context.object.vertex_groups[grouNumb].add(lis_, weig, type = 'ADD')
	bpy.context.object.vertex_groups[grouNumb].name = name

def VertGrouSele(name):
	import bpy
	Edit()
	bpy.ops.object.vertex_group_set_active(group = name)
	bpy.ops.object.vertex_group_select()
	Edit()

def VertGrouDele(name):
	import bpy
	bpy.ops.object.vertex_group_set_active(group = name)
	bpy.ops.object.vertex_group_remove()

# use blenders shortest path function to find the shortest path between START INDEX and FINISHING INDEX
def PathShor(star, fini):
	import bpy
	VertDese()
	VertSele([star, fini])
	Edit()
	bpy.ops.mesh.shortest_path_select()
	Edit()
	coun = 0
	a = 0
	while a < len(bpy.context.object.data.vertices):
		if bpy.context.object.data.vertices[a].select == True:
			coun += 1
		if coun == 2:
			break
		a += 1
	if coun < 2:
		VertSele([star, fini])

def Loop():
	import bpy
	Edit()
	bpy.ops.mesh.loop_multi_select()
	Edit()

def Regi():
	import bpy
	Edit()
	bpy.ops.mesh.loop_to_region()
	Edit()

#############################################

# MESH OPERATIONS

def Face():
	import bpy
	Edit()
	bpy.ops.mesh.edge_face_add()
	Edit()

def Fill():
	import bpy
	Edit()
	bpy.ops.mesh.fill()
	Edit()

def Extr(value = (0.0, 0.0, 0.0)):
	import bpy
	Edit()
	bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value": value, "constraint_axis":(False, False, False), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":39.7397, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
	Edit()

def Inse(thic = 0.1):
	import bpy
	Edit()
	bpy.ops.mesh.inset(thickness = thic)
	Edit()

def Subd(cuts = 1):
	import bpy
	Edit()
	bpy.ops.mesh.subdivide(number_cuts = cuts)
	Edit()

def Merg(typ_ = 'CENTER'):
	import bpy
	Edit()
	bpy.ops.mesh.merge(type = typ_)
	Edit()

# traiangulate all the faces of the selected object
def Tria():
	import bpy
	VertSeleAll_()
	Edit()
	bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
	Edit()

# remove double vertices
def VertDoub(threshold = 0.001):
	import bpy
	VertSeleAll_()
	Edit()
	bpy.ops.mesh.remove_doubles(threshold = threshold)
	Edit()
	VertDese()

# limited dissolve
def Diss():
	import bpy
	VertSeleAll_()
	Edit()
	bpy.ops.mesh.dissolve_limited()
	Edit()
	VertDese()

# flip all normals of the selected object
def Flip():
	import bpy
	VertSeleAll_()
	Edit()
	bpy.ops.mesh.flip_normals()
	Edit()

# scale vertices
def ScalMesh(vect):
	import bpy
	Edit()
	bpy.ops.transform.resize(value = vect, constraint_axis=(vect[0] != 1.0, vect[0] != 1.0, vect[0] != 1.0), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=39.7397)
	Edit()

def VertTran(tran, prop = False):
	import bpy
	if prop:
		prop = 'ENABLED'
	else:
		prop = 'DISABLED'
	Edit()
	bpy.ops.transform.translate(value=(tran[0], tran[1], tran[2]), constraint_axis=(tran[0] != 0.0, tran[1] != 0.0, tran[2] != 0.0), constraint_orientation='GLOBAL', mirror=False, proportional = prop, proportional_edit_falloff='SMOOTH', proportional_size=39.7397, release_confirm=True)
	Edit()

# move each of the faces of an object into a new object and delete the original
def PolyTo__Obje():
	import bpy
	name = bpy.context.object.name
	scal, rota, loca = TranRead()
	uplo = []
	for a in range(len(bpy.context.object.data.polygons)):
		poly = bpy.context.object.data.polygons[a]
		vert = PolyVert(a)
		vert = VertLoca(vert)
		poly = []
		for b in range(len(vert)):
			poly.append(b)
		poly = tuple(poly)
		poly = [poly]
		uplo.append([vert, [], poly])
	for a in range(len(uplo)):
		#Uplo(uplo[a], name = "poly" + "." + Pad_(a))
		Uplo(uplo[a], name = name + "." + Pad_(a))
		Tran(scal, rota, loca)
	Sele(name)
	Dele()

#########################################

# MODIFIERS

def ModiSkin(scalFact = 20.0, inde = 0, scal = False, applModi = False, tranInde = False, appl = False):
	import bpy
	bpy.ops.object.modifier_add(type='SKIN')
	if scal:
		Edit()
		Scal((scalFact, scalFact, scalFact))
		Edit()
		Scal((1.0 / scalFact, 1.0 / scalFact, 1.0 / scalFact))
	if applModi:
		bpy.ops.object.modifier_apply(modifier = "Skin")
	if tranInde:
		loca = bpy.context.object.data.vertices[inde].co
		Loca((-1.0 * loca[0] / scalFact, -1.0 * loca[1] / scalFact, -1.0 * loca[2] / scalFact))
	if appl:
		Appl()

#########################################

# MATERIAL / TEXTURE / IMAGE

def Mate(name = "", colo = (1.0, 1.0, 1.0), use_shadeless = False, check = True, uniq = True):
	import bpy
	inst = -1
	if name == "":
		name = "Material"
	if check == True:
		for mate in bpy.data.materials:
			if mate.name == name:
				uniq = False
				inst = Inst(mate.name)
				break
	if uniq == False:
		name = InstRepl(name, Pad_(inst + 1))
		uniq = False
		while uniq == False:
			try_agai = False
			for mate in bpy.data.materials:
				if mate.name == name:
					try_agai = True
					inst = Inst(mate.name)
					name = InstRepl(name, Pad_(inst + 1))
					break
			if try_agai == False:
				uniq = True
	bpy.data.materials.new(name)
	bpy.data.materials[name].diffuse_intensity = 1.0
	bpy.data.materials[name].specular_intensity = 0.0
	bpy.data.materials[name].diffuse_color = colo
	bpy.data.materials[name].use_shadeless = use_shadeless
	MateSet_(name)
	return name

# add a new material slot and set it to an existing material by NAME
def MateSet_(name):
	import bpy
	bpy.ops.object.material_slot_add()
	bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material = bpy.data.materials[name]

# add a texture of NAME to the active material in the Blender engine
def MateText(name):
	import bpy
	if name != None:
		if len(name) > 0:
			bpy.data.textures.new(name, 'IMAGE')
			inde = bpy.context.object.active_material.active_texture_index
			bpy.context.object.active_material.texture_slots.create(inde)
			bpy.context.object.active_material.texture_slots[inde].texture = bpy.data.textures[name]
			bpy.data.textures[name].type = 'IMAGE'
			bpy.context.object.active_material.texture_slots[inde].texture_coords = 'ORCO'

# add an image to a texture in the Blender engine
def Imag(path, name):
	import bpy
	import os
	Pyth = PythLink()
	if path != None and path != "":
		fina = Pyth.FileName(path)
		bpy.ops.image.open(filepath = path, files=[{"name":fina, "name":fina}], relative_path = False)
		if name != None and name != "":
			bpy.data.textures[name].image = bpy.data.images[fina]
			# TODO
			#bpy.context.object.active_material.texture_slots[len(bpy.context.object.active_material.texture_slots) - 1].texture_coords = 'ORCO'
			#print(bpy.context.object.active_material.name)

# for each material of an object, create vari more VARIATIONS. spre is the MAXIMUM VALUE OF A VARIATION
def ColoVary(vari = 2, spre = 0.6):
	import bpy
	import random
	engi = bpy.context.scene.render.engine
	coun = len(bpy.context.object.data.materials)
	a = 0
	while a < coun:
		name = bpy.context.object.material_slots[a].material.name
		down = True
		for b in range(vari):
			bpy.ops.object.material_slot_add()
			bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material = bpy.data.materials[name]
			bpy.ops.object.make_single_user(material = True)
			v = spre / (int(vari / 2) - int(b / 2))
			if down == True:
				down = False
				v *= -1.0
			else:
				down = True
			v += 1.0
			if engi == 'CYCLES':
				for c in range(len(bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material.node_tree.nodes)):
					node = bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material.node_tree.nodes[c]
					if ShadHas_Colo(node.type):
						node.inputs[0].default_value = (v * node.inputs[0].default_value[0], v * node.inputs[0].default_value[1], v * node.inputs[0].default_value[2], node.inputs[0].default_value[3])
			else:
				bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material.diffuse_color = (v * bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material.diffuse_color[0], v * bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material.diffuse_color[1], v * bpy.context.object.material_slots[len(bpy.context.object.material_slots) - 1].material.diffuse_color[2])
		a += 1
	for poly in bpy.context.object.data.polygons:
		prev = poly.material_index
		if prev < coun:
			random.seed()
			rand = random.randint(0, vari - 0)
			if rand != 0:
				rand += coun + prev * vari - 1
				poly.material_index = rand

def ShadHas_Colo(typ_):
	retu = False
	if typ_ == 'AMBIENT_OCCLUSION':
		retu = True
	elif typ_ == 'BSDF_ANISOTROPIC':
		retu = True
	elif typ_ == 'BSDF_DIFFUSE':
		retu = True
	elif typ_ == 'EMISSION':
		retu = True
	elif typ_ == 'BSDF_GLASS':
		retu = True
	elif typ_ == 'BSDF_GLOSSY':
		retu = True
	elif typ_ == 'BSDF_HAIR':
		retu = True
	elif typ_ == 'BSDF_REFRACTION':
		retu = True
	elif typ_ == 'SUBSURFACE_SCATTERING':
		retu = True
	elif typ_ == 'BSDF_TOON':
		retu = True
	elif typ_ == 'BSDF_TRANSLUCENT':
		retu = True
	elif typ_ == 'BSDF_TRANSPARENT':
		retu = True
	elif typ_ == 'BSDF_VELVET':
		retu = True
	elif typ_ == 'VOLUME_ABSORPTION':
		retu = True
	elif typ_ == 'VOLUME_SCATTER':
		retu = True
	return retu

# create a new object consisting of polygons that were assigned the same material
def SpliMate(mate, dele = True):
	import bpy
	name = bpy.context.object.name
	Dupl()
	bpy.context.object.name = name + "." + mate
	# delete other materials of the new object
	a = 0
	while a < len(bpy.context.object.data.polygons):
		poly = bpy.context.object.data.polygons[a]
		if poly.material_index >= 0 and poly.material_index < len(bpy.context.object.material_slots):
			if bpy.context.object.material_slots[poly.material_index].name != mate:
				vert = PolyVert(a)
				VertSele(vert)
				PolyDele()
				a = -1
		a += 1
	# delete the material on the original object
	if dele == True:
		Sele(name)
		a = 0
		while a < len(bpy.context.object.data.polygons):
			poly = bpy.context.object.data.polygons[a]
			if poly.material_index >= 0 and poly.material_index < len(bpy.context.object.material_slots):
				if bpy.context.object.material_slots[poly.material_index].name == mate:
					vert = PolyVert(a)
					VertSele(vert)
					PolyDele()
					a = -1
			a += 1

# purge unused materials
def MatePurgScen():
	import bpy
	for mate in bpy.data.materials:
		if mate.users == 0:
			mate.user_clear()

#############################################

# CURVE

# place the given index of a curve at the given location. create a new point if the index is greater than the existing point length
def CurvLoca(inde, loca):
	import bpy
	leng = len(bpy.context.object.data.splines[0].bezier_points)
	if inde < leng:
		bpy.context.object.data.splines[0].bezier_points[inde].co = loca
	else:
		Edit()
		bpy.ops.curve.select_all(action = 'DESELECT')
		Edit()
		diff = leng - inde + 1
		for a in range(diff):
			Edit()
			bpy.context.object.data.splines[0].bezier_points[leng + a - 1].select_control_point = True
			bpy.context.object.data.splines[0].bezier_points[leng + a - 1].select_left_handle = True
			bpy.context.object.data.splines[0].bezier_points[leng + a - 1].select_right_handle = True
			bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":"TRANSLATION"}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.0), "constraint_axis":(False, False, False), "constraint_orientation":"GLOBAL", "mirror":False, "proportional":"DISABLED", "proportional_edit_falloff":"SHARP", "proportional_size":8.14027, "snap":False, "snap_target":"CLOSEST", "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
			bpy.context.object.data.splines[0].bezier_points[leng + a - 1].select_control_point = False
			bpy.context.object.data.splines[0].bezier_points[leng + a - 1].select_left_handle = False
			bpy.context.object.data.splines[0].bezier_points[leng + a - 1].select_right_handle = False
			Edit()
		bpy.context.object.data.splines[0].bezier_points[inde].co = loca

# align handles to make the line between branch points straight
def CurvHand():
	import bpy
	Edit()
	bpy.ops.curve.select_all(action = 'SELECT')
	bpy.ops.curve.handle_type_set(type='FREE_ALIGN')
	bpy.ops.curve.select_all(action = 'DESELECT')
	Edit()
	bpy.context.object.data.splines[0].bezier_points[0].handle_left.xyz = bpy.context.object.data.splines[0].bezier_points[0].co
	bpy.context.object.data.splines[0].bezier_points[len(bpy.context.object.data.splines[0].bezier_points) - 1].handle_right.xyz = bpy.context.object.data.splines[0].bezier_points[len(bpy.context.object.data.splines[0].bezier_points) - 1].co
	for a in range(len(bpy.context.object.data.splines[0].bezier_points) - 1):
		poi1 = bpy.context.object.data.splines[0].bezier_points[a]
		poi2 = bpy.context.object.data.splines[0].bezier_points[a + 1]
		difx = poi2.co.x - poi1.co.x
		dify = poi2.co.y - poi1.co.y
		difz = poi2.co.z - poi1.co.z
		poi1.handle_right.xyz = (poi1.co.x + difx / 2.0, poi1.co.y + dify / 2.0, poi1.co.z + difz / 2.0)
		poi2.handle_left.xyz = (poi1.co.x + difx / 2.0, poi1.co.y + dify / 2.0, poi1.co.z + difz / 2.0)

##############################################

# CHARACTER

def CharLeftTo__Righ(name = "", lis_ = [[".shou.l", ".body"], [".hip_.l", ".body"]], faci = (1.0, 0.0), exceList = [], axle = True, axleList = ["axle.arms", "axle.legs"], dele = True, deleList = []):
	import bpy
	if lis_ == [[".shou.l", ".body"], [".hip_.l", ".body"]]:
		for a in range(len(lis_)):
			for b in range(len(lis_[a])):
				lis_[a][b] = name + lis_[a][b]
	if dele == True:
		if deleList == []:
			deleList = [name + ".axle.arms.r", name + ".axle.legs.r", name + ".shou.r", name + ".elbo.r", name + ".wris.r", name + ".hand.r", name + ".hip_.r", name + ".knee.r", name + ".ankl.r", name + ".foot.r"]
		for obje in deleList:
			Sele(obje)
			Dele()
	# get all children of the root bones (eg shoulder and hip)
	chilList = []
	for root in lis_:
		rootList = []
		if len(root) > 0:
			if len(root) > 1:
				rootList.append(root[1])
			rootList.append(root[0])
			#if bpy.data.objects[root[0]].hide_select == False:
			Sele(root[0])
			rootList = Chil(rootList)
			chilList.append(rootList)
	for chil in chilList:
		a = 1
		while a < len(chil):
			exce = False
			b = 0
			while b < len(exceList):
				if chil[a] == exceList[b]:
					exce = True
					break
				b += 1
			if exce == False:
				Sele(chil[a])
				# remove mirror modifiers if they exist
				mirrList = []
				b = 0
				while b < len(bpy.context.object.modifiers):
					if bpy.context.object.modifiers[b].type == 'MIRROR':
						mirrList.append(bpy.context.object.modifiers[b].name)
					b += 1
				for mirr in mirrList:
					bpy.ops.object.modifier_remove(modifier = mirr)
				CharMirr(faci = faci)
			a += 1
	# reparent
	c = 0
	while c < len(chilList):
		lis_ = chilList[c]
		a = 0
		while a < len(lis_) - 1:
			exce = False
			b = 0
			while b < len(exceList):
				if lis_[a] == exceList[b]:
					exce = True
					break
				b += 1
			if exce == False:
				pare = CharMirrName(lis_[a])
				chil = CharMirrName(lis_[a + 1])
				Sele(chil)
				Pare(pare)
				Sele(chil)
				ApplRota()
				ApplScal()
				if bpy.context.object.type == 'MESH':
					Flip()
			a += 1
		c += 1
	# axles are empties, parented to the body, which the hands and feet rotate around in walk and run animations
	if axle == True:
		for axl_ in axleList:
			Sele(name + "." + axl_ + "." + "l")
			CharMirr(faci = faci, reve = False)
			Sele(name + "." + axl_ + "." + "r")
			Pare(name + ".body")

# mirror the geometry of a mesh on one axis
# TODO: only tested for two directions, +x and -y
def CharMirr(faci = (1.0, 0.0), reve = True):
	import bpy
	import math
	Math = MathLink()
	cont = bpy.context.object.name
	name = CharMirrName(cont)
	Dupl()
	bpy.context.object.name = name
	PareClea()
	angl = math.atan2(faci[1], faci[0])
	angl -= math.pi / 2.0
	loca = (bpy.context.object.location[0] + math.cos(angl) * 2.0 * bpy.context.object.location[0], bpy.context.object.location[1] + math.sin(angl) * 2.0 * bpy.context.object.location[1], bpy.context.object.location[2])
	Loca(loca)
	if reve == True and (bpy.context.object.type == 'MESH' or bpy.context.object.type == 'CURVE'):
		scal = ScalRead()
		Scal((scal[0] + 2.0 * math.cos(angl) * scal[0], scal[1] + 2.0 * math.sin(angl) * scal[1], scal[2]))
	Sele(cont)

# look for ".l" or ".r" and switch
def CharMirrName(name):
	import bpy
	Pyth = PythLink()
	retu = name.split(".")
	if retu[len(retu) - 1] == "l":
		retu[len(retu) - 1] = "r"
	elif retu[len(retu) - 1] == "r":
		retu[len(retu) - 1] = "l"
	return Pyth.ListTo__Stri(retu, sepa = ".")

# give bone origins the same x and y
def CharAlig(name = ""):
	import bpy
	rootList = [name + ".shoulder.l", name + ".shoulder.r", name + ".hip.l", name + ".hip.r"]
	chilList = [[name + ".elbow.l", name + ".wrist.l"], [name + ".elbow.r", name + ".wrist.r"], [name + ".knee.l", name + ".ankle.l"], [name + ".knee.r", name + ".ankle.r"]]
	tip_List = [name + ".hand.l", name + ".hand.r", name + ".foot.l", name + ".foot.r"]
	a = 0
	while a < len(rootList):
		root = rootList[a]
		lis_ = chilList[a]
		tip_ = tip_List[a]
		for bone in lis_:
			Sele(root)
			loca = LocaRead()
			Sele(bone)
			Curs((loca[0], loca[1], bpy.context.object.location[2]))
			OrigCurs()
		Sele(tip_)
		Loca((loca[0], loca[1], bpy.context.object.location[2]))
		a += 1

#############################################

# RIGGING / SKINNING

# example usage:

# charName = "char"
# RIGGING / SKINNING
# spinCoun = 3
# shouCoun = 1
# hip_Coun = 1
# rig_List = Rig_Read()
# rig_List, bra1List, bra2List, bra3List, bra4List, bra5List, locaList, switList, regiList = Rig_List(rig_List, spinCoun = spinCoun, shouCoun = shouCoun, hip_Coun = hip_Coun)
# make markers
# MarkCrea(rig_List, locaList, charName + "." + "body", charName = charName)
# align markers
# Alig(bra1List, charName = charName)
# Alig(bra2List, aligInde = 1, charName = charName)
# Alig(bra3List, aligInde = 1, charName = charName)
# MarkRefl(rig_List, charName = charName)
# create armature
# Rig_(charName + "." + "body", rig_List, bra1List, charName = charName, spinCoun = spinCoun, shouCoun = shouCoun, hip_Coun = hip_Coun)
# Rig_(charName + "." + "body", rig_List, bra2List, charName = charName, spinCoun = spinCoun, shouCoun = shouCoun, hip_Coun = hip_Coun)
# Rig_(charName + "." + "body", rig_List, bra3List, charName = charName, spinCoun = spinCoun, shouCoun = shouCoun, hip_Coun = hip_Coun)
# Rig_(charName + "." + "body", rig_List, bra4List, charName = charName, spinCoun = spinCoun, shouCoun = shouCoun, hip_Coun = hip_Coun)
# Rig_(charName + "." + "body", rig_List, bra5List, charName = charName, spinCoun = spinCoun, shouCoun = shouCoun, hip_Coun = hip_Coun)
# BoneRollRese()
# BoneRotaMode()
# apply mirror
# parent mesh to armature (and skin)
# Blen.Sele(charName + "." + "body")
# ArmaVolu()
# skin extra
# SPLIT MESH INTO SEPARATE "BONES"
# use / rename markers created above
# spliList, switList, pareDict, flipList = SpliRead(charName = charName)
# make switch list
# test individual loops
# inde = 0
# mark = MarkRead(rig_List, spliList[inde], charName = charName)
# LoopNear(charName + "." + "body", mark, swit = switList[inde])
# back up loops to a file
# loopList = LoopList(charName + "." + "body", spliList, rig_List, switList, charName = charName)
# LoopListWrit(loopList)
# loopList = LoopListRead()
# split mesh
# MeshSpli(charName + "." + "body", spliList, loopList, rig_List, flipList, charName = charName)
# parent "bones"
# for key_ in pareDict:
#	Blen.Sele(key_)
#	Blen.Pare(pareDict[key_])
# VERTEX GROUPS
# make regions list ("s", "f", [0, 1, 2], None)
# test individual vertex groups
# inde = 0
# LoopRegi(charName + "." + "body", inde, rig_List, switList, typ_ = regiList[inde], charName = charName)
# create vertex groups
# SkinAll_(name + "." + "body", rig_List, switList, regiList, charName = charName, pref = pref)
# OTHER FUNCTIONS
# backup / restore vertex positions
# VertBack()
# VertRest()
# backup / restore vertex weights
# WeigBack()
# WeigRest()

def BoneNameSpli(boneName):
	retu = []
	boneName = boneName.split(".")
	inst = True
	if boneName[len(boneName) - 1] == "l" or boneName[len(boneName) - 1] == "m" or boneName[len(boneName) - 1] == "r":
		inst = False
	nameInde = 0
	prefInde = 1
	indeInde = 2
	boneInde = 3
	sideInde = 4
	instInde = 5
	if inst == False:
		instInde = -1
	if len(boneName) < 4 or (len(boneName) == 4 and inst == True):
		nameInde = -2
		prefInde = -2
	if len(boneName) == 4 and inst == False:
		indeInde = -2
		instInde = -2
	if len(boneName) == 5 and inst == True:
		indeInde = -1
		instInde = 4
	if len(boneName) == 4 and inst == False:
		boneInde = 2
		sideInde = 3
	if (len(boneName) == 4 and inst == True) or (len(boneName) == 3 and inst == False):
		indeInde = 0
		boneInde = 1
		sideInde = 2
		if len(boneName) == 4:
			instInde = 3
	if (len(boneName) == 3 and inst == True) or len(boneName) == 2:
		indeInde = -1
		boneInde = 0
		sideInde = 1
		if len(boneName) == 3:
			instInde = 2
	if nameInde != -2:
		retu.append(boneName[nameInde])
	if prefInde != -2:
		retu.append(boneName[prefInde])
	if indeInde != -2:
		if indeInde == -1:
			retu.append("-1")
		else:
			retu.append(boneName[indeInde])
	retu.append(boneName[boneInde])
	retu.append(boneName[sideInde])
	if instInde != -2:
		if instInde == -1:
			retu.append("-1")
		else:
			retu.append(boneName[instInde])
	return retu

# concatenate strings with a period if the string aren't empty
def Conc(conc, stri = "", sepa = ".", empt = ""):
	# restore defaults if sepa or empt are None (so that defaults don't have to be listed again in ConcList)
	# TODO: probably a better way to do this
	if sepa == None:
		sepa = "."
	if empt == None:
		empt = ""
	if conc != empt:
		if stri != "":
			stri += sepa
		stri += conc
	return stri

# concatenate a list of strings
# TODO: this could maybe be a generic function
def ConcList(concList, stri = "", sepaList = [], emptList = []):
	for a in range(len(concList)):
		# TODO: what if a user wanted to pass None
		sepa = None
		if sepaList != []:
			sepa = sepaList[a]
		empt = None
		if emptList != []:
			empt = emptList[a]
		stri = Conc(concList[a], stri = stri, sepa = sepa, empt = empt)
	return stri

def Rig_Read(conf = 0):
	Pyth = PythLink()
	retu = []
	if type(conf) == int:
		if conf == 0:
			retu.append("spin.m.000, spin.m.001, spin.m.000, (0.0,0.0,1.0)")
			retu.append("spin.m.001, spin.m.002, spin.m.001, (0.0,0.0,1.1)")
			retu.append("spin.m.002, neck.m, spin.m.002, (0.0,0.0,1.6)")
			retu.append("neck.m, head.m, neck.m, (0.0,0.0,1.65)")
			retu.append("head.m, top_.m, head.m, (0.0,0.0,1.7)")
			retu.append("top_.m, None, top_.m, (0.0,0.0,1.8)")
			retu.append("")
			# TODO: new branches are extruded from the head
			retu.append("spin.m.002, shou.l, clav.l, None")
			retu.append("shou.l, elbo.l, shou.l, (0.0,0.21,1.55)")
			retu.append("elbo.l, wris.l, elbo.l, (0.0,0.21,1.2)")
			retu.append("wris.l, hand.l, wris.l, (0.0,0.21,1.0)")
			retu.append("hand.l, None, hand.l, (0.0,0.21,0.9)")
			retu.append("")
			retu.append("spin.m.000, hip_.l, pelv.l, None")
			retu.append("hip_.l, knee.l, hip_.l, (0.0,0.15,1.05)")
			retu.append("knee.l, ankl.l, knee.l, (0.0,0.15,0.7)")
			retu.append("ankl.l, foot.l, ankl.l, (0.0,0.15,0.15)")
			retu.append("foot.l, None, foot.l, (0.0,0.15,0.0)")
			retu.append("")
			retu.append("spin.m.002, shou.r, clav.r, None")
			retu.append("shou.r, elbo.r, shou.r, (0.0,-0.21,1.55)")
			retu.append("elbo.r, wris.r, elbo.r, (0.0,-0.21,1.2)")
			retu.append("wris.r, hand.r, wris.r, (0.0,-0.21,1.0)")
			retu.append("hand.r, None, hand.r, (0.0,-0.21,0.9)")
			retu.append("")
			retu.append("spin.m.000, hip_.r, pelv.r, None")
			retu.append("hip_.r, knee.r, hip_.r, (0.0,-0.15,1.05)")
			retu.append("knee.r, ankl.r, knee.r, (0.0,-0.15,0.7)")
			retu.append("ankl.r, foot.r, ankl.r, (0.0,-0.15,0.15)")
			retu.append("foot.r, None, foot.r, (0.0,-0.15,0.0)")
		# fingers
		elif conf == 1:
			retu.append("spin.m.000, spin.m.001, spin.m.000, (0.0,0.0,1.0)")
			retu.append("spin.m.001, spin.m.002, spin.m.001, (0.0,0.0,1.1)")
			retu.append("spin.m.002, neck.m, spin.m.002, (0.0,0.0,1.6)")
			retu.append("neck.m, head.m, neck.m, (0.0,0.0,1.65)")
			retu.append("head.m, top_.m, head.m, (0.0,0.0,1.7)")
			retu.append("top_.m, None, top_.m, (0.0,0.0,1.8)")
			retu.append("")
			retu.append("spin.m.002, shou.l, clav.l, None")
			retu.append("shou.l, elbo.l, shou.l, (0.0,0.21,1.55)")
			retu.append("elbo.l, wris.l, elbo.l, (0.0,0.21,1.2)")
			retu.append("wris.l, hand.l, wris.l, (0.0,0.21,1.0)")
			retu.append("thum.l.000, thum.l.001, thum.l.000, (0.04,0.21,0.98)")
			retu.append("thum.l.001, thum.l.002, thum.l.001, (0.04,0.21,0.96)")
			retu.append("thum.l.002, thum.l.003, thum.l.002, (0.04,0.21,0.94)")
			retu.append("thum.l.003, None, thum.l.003, (0.04,0.21,0.92)")
			retu.append("")
			retu.append("inde.l.000, inde.l.001, inde.l.000, (0.02,0.21,0.96)")
			retu.append("inde.l.001, inde.l.002, inde.l.001, (0.02,0.21,0.94)")
			retu.append("inde.l.002, inde.l.003, inde.l.002, (0.02,0.21,0.92)")
			retu.append("inde.l.003, None, inde.l.003, (0.02,0.21,0.9)")
			retu.append("")
			retu.append("midd.l.000, midd.l.001, midd.l.000, (0.0,0.21,0.96)")
			retu.append("midd.l.001, midd.l.002, midd.l.001, (0.0,0.21,0.94)")
			retu.append("midd.l.002, midd.l.003, midd.l.002, (0.0,0.21,0.92)")
			retu.append("midd.l.003, None, midd.l.003, (0.0,0.21,0.9)")
			retu.append("")
			retu.append("ring.l.000, ring.l.001, ring.l.000, (-0.02,0.21,0.96)")
			retu.append("ring.l.001, ring.l.002, ring.l.001, (-0.02,0.21,0.94)")
			retu.append("ring.l.002, ring.l.003, ring.l.002, (-0.02,0.21,0.92)")
			retu.append("ring.l.003, None, ring.l.003, (-0.02,0.21,0.9)")
			retu.append("")
			retu.append("pink.l.000, pink.l.001, pink.l.000, (-0.04,0.21,0.96)")
			retu.append("pink.l.001, pink.l.002, pink.l.001, (-0.04,0.21,0.94)")
			retu.append("pink.l.002, pink.l.003, pink.l.002, (-0.04,0.21,0.92)")
			retu.append("pink.l.003, None, pink.l.003, (-0.04,0.21,0.9)")
			retu.append("")
			retu.append("spin.m.000, hip_.l, pelv.l, None")
			retu.append("hip_.l, knee.l, hip_.l, (0.0,0.15,1.05)")
			retu.append("knee.l, ankl.l, knee.l, (0.0,0.15,0.7)")
			retu.append("ankl.l, foot.l, ankl.l, (0.0,0.15,0.15)")
			retu.append("foot.l, None, foot.l, (0.0,0.15,0.0)")
			retu.append("")
			retu.append("spin.m.002, shou.r, clav.r, None")
			retu.append("shou.r, elbo.r, shou.r, (0.0,0.21,1.55)")
			retu.append("elbo.r, wris.r, elbo.r, (0.0,0.21,1.2)")
			retu.append("wris.r, hand.r, wris.r, (0.0,0.21,1.0)")
			retu.append("thum.r.000, thum.r.001, thum.r.000, (0.04,0.21,0.98)")
			retu.append("thum.r.001, thum.r.002, thum.r.001, (0.04,0.21,0.96)")
			retu.append("thum.r.002, thum.r.003, thum.r.002, (0.04,0.21,0.94)")
			retu.append("thum.r.003, None, thum.r.003, (0.04,0.21,0.92)")
			retu.append("")
			retu.append("inde.r.000, inde.r.001, inde.r.000, (0.02,0.21,0.96)")
			retu.append("inde.r.001, inde.r.002, inde.r.001, (0.02,0.21,0.94)")
			retu.append("inde.r.002, inde.r.003, inde.r.002, (0.02,0.21,0.92)")
			retu.append("inde.r.003, None, inde.r.003, (0.02,0.21,0.9)")
			retu.append("")
			retu.append("midd.r.000, midd.r.001, midd.r.000, (0.0,0.21,0.96)")
			retu.append("midd.r.001, midd.r.002, midd.r.001, (0.0,0.21,0.94)")
			retu.append("midd.r.002, midd.r.003, midd.r.002, (0.0,0.21,0.92)")
			retu.append("midd.r.003, None, midd.r.003, (0.0,0.21,0.9)")
			retu.append("")
			retu.append("ring.r.000, ring.r.001, ring.r.000, (-0.02,0.21,0.96)")
			retu.append("ring.r.001, ring.r.002, ring.r.001, (-0.02,0.21,0.94)")
			retu.append("ring.r.002, ring.r.003, ring.r.002, (-0.02,0.21,0.92)")
			retu.append("ring.r.003, None, ring.r.003, (-0.02,0.21,0.9)")
			retu.append("")
			retu.append("pink.r.000, pink.r.001, pink.r.000, (-0.04,0.21,0.96)")
			retu.append("pink.r.001, pink.r.002, pink.r.001, (-0.04,0.21,0.94)")
			retu.append("pink.r.002, pink.r.003, pink.r.002, (-0.04,0.21,0.92)")
			retu.append("pink.r.003, None, pink.r.003, (-0.04,0.21,0.9)")
			retu.append("")
			retu.append("spin.m.000, hip_.r, pelv.r, None")
			retu.append("hip_.r, knee.r, hip_.r, (0.0,0.15,1.05)")
			retu.append("knee.r, ankl.r, knee.r, (0.0,0.15,0.7)")
			retu.append("ankl.r, foot.r, ankl.r, (0.0,0.15,0.15)")
			retu.append("foot.r, None, foot.r, (0.0,0.15,0.0)")
	elif type(conf) == str:
		retu = Pyth.FileTo__Line(conf)
	return retu

# faci - assumes the character is facing the positive x axis so that the z rotation of the character is 0 degrees by default in the x/y plane. to face the rig towards a different direction, pass, "-y", "+y", or "-x"
# TODO: this function assumes the armature has a certain structure
def Rig_List(rig_List, spinCoun = 3, shouCoun = 1, hip_Coun = 1, use_Inde = True, faci = "+x"):
	Pyth = PythLink()
	def Inde(name, markCoun = -1, use_Inde = use_Inde):
		retu = ""
		if use_Inde == True:
			retu = Pad_(markCoun) + "."
		retu += name
		return retu
	spinMini = 3
	shouMini = 1
	hip_Mini = 1
	if spinCoun < spinMini:
		spinCoun = spinMini
	if shouCoun < shouMini:
		shouCoun = shouMini
	if hip_Coun < hip_Mini:
		hip_Coun = hip_Mini
	spinCuttLowe = 1
	shouCuttLowe = 0
	hip_CuttLowe = 0
	spinCuttUppeDiff = 1
	shouCuttUppeDiff = 0
	hip_CuttUppeDiff = 0
	markCoun = 0
	retu = []
	bran = []
	locaList = []
	spinInst = 0
	shouInst = 0
	hip_Inst = 0
	spinBoneEnd_ = "spin" + "." + "m" + "." + Pad_(spinCoun - 1)
	shouBoneEnd_ = "elbo"
	hip_BoneEnd_ = "knee"
	# if new bones are added to the spine, update the connections loaded from Rig_Read()
	spinShif = [spinCuttLowe, 0]
	shouShif = [shouCuttLowe, 0]
	hip_Shif = [hip_CuttLowe, 0]
	shif = []
	a = 0
	while a < len(rig_List):
		if  rig_List[a] == "":
			retu.append(bran)
			bran = []
			# TODO: reset spinInst and add a way to check if a spine bone is the start of a new branch
			shouInst = 0
			hip_Inst = 0
			shouShif = [shouCuttLowe, 0]
			hip_Shif = [hip_CuttLowe, 0]
		else:
			entr =  rig_List[a].split(", ")
			name = entr[0]
			inde, bone, side, inst = BoneNameSpli(name)
			boneHead = ""
			boneTail = ""
			boneName = ""
			boneLoca = None
			if (bone == "spin" and spinCoun > spinMini and spinInst < spinCoun) or (bone == "shou" and shouCoun > shouMini and shouInst < shouCoun) or (bone == "hip_" and hip_Coun > hip_Mini and hip_Inst < hip_Coun):
				if bone == "spin":
					coun = spinCoun
					inst = spinInst
					cuttLowe = spinCuttLowe
					cuttUppe = coun - spinCuttUppeDiff
					boneEnd_ = spinBoneEnd_
					shif = spinShif
				elif bone == "shou":
					coun = shouCoun
					inst = shouInst
					cuttLowe = shouCuttLowe
					cuttUppe = coun - shouCuttUppeDiff
					boneEnd_ = shouBoneEnd_ + "." + side
					shif = shouShif
				elif bone == "hip_":
					coun = hip_Coun
					inst = hip_Inst
					cuttLowe = hip_CuttLowe
					cuttUppe = coun - hip_CuttUppeDiff
					boneEnd_ = hip_BoneEnd_ + "." + side
					shif = hip_Shif
				if inst == cuttLowe:
					star =  rig_List[a]
					star = star.split(", ")
					star = Pyth.StriTo__Tupl(star[3])
					end_ =  rig_List[a + 1]
					end_ = end_.split(", ")
					end_ = Pyth.StriTo__Tupl(end_[3])
				cuttDiff = cuttUppe - cuttLowe
				if inst < cuttLowe or inst == cuttDiff:
					inde, bone, side, boneInst = BoneNameSpli(entr[0])
					if inst > cuttLowe:
						inst = shif[0] + shif[1]
					boneHead = Inde(bone + "." + side + "." + Pad_(inst), markCoun)
					boneTail = Inde(entr[1], markCoun + 1)
					boneName = boneHead
					bran.append([boneHead, boneTail, boneName])
					loca = Pyth.StriTo__Tupl(entr[3])
					locaList.append(loca)
					inst += 1
					markCoun += 1
				else:
					# create extra (in-between) bones
					betwInst = shif[0] + shif[1]
					inst += 1
					while betwInst < cuttUppe:
						boneHead = bone + "." + side + "." + Pad_(betwInst)
						boneHead = Inde(boneHead, markCoun)
						if betwInst < cuttUppe - 1:
							boneTail = bone + "." + side + "." + Pad_(betwInst + 1)
						else:
							boneTail = boneEnd_
						boneTail = Inde(boneTail, markCoun + 1)
						bran.append([boneHead, boneTail, boneHead])
						incr = shif[1] / cuttDiff
						heig = star[2] - star[2] * incr + end_[2] * incr
						loca = (star[0], star[1], heig)
						locaList.append(loca)
						markCoun += 1
						shif[1] += 1
						betwInst = shif[0] + shif[1]
				if bone == "spin":
					spinInst = inst
				elif bone == "shou":
					shouInst = inst
				elif bone == "hip_":
					hip_Inst = inst
			else:
				if bone == "spin":
					cuttLowe = spinCuttLowe
					shif = spinShif
				elif bone == "shou":
					cuttLowe = shouCuttLowe
					shif = shouShif
				elif bone == "hip_":
					cuttLowe = hip_CuttLowe
					shif = hip_Shif
				loca = entr[3]
				if loca != "None":
					boneHead = bone + "." + side
					if int(inst) > shif[0]:
						inst = int(inst) + shif[1]
						inst = Pad_(inst)
						boneHead = ConcList([inst], stri = boneHead)
						shif[1] += 1
					else:
						boneHead = ConcList([inst], stri = boneHead, emptList = ["-1"])
					boneHead = Inde(name, markCoun)
					name = entr[1]
					if name != "None":
						boneTail = Inde(name, markCoun + 1)
					else:
						boneTail = "None"
					boneName = boneHead
					loca = Pyth.StriTo__Tupl(loca)
					locaList.append(loca)
					if bone == "spin":
						spinShif = [shif[0], shif[1]]
					elif bone == "shou":
						shouShif = [shif[0], shif[1]]
					elif bone == "hip_":
						hip_Shif = [shif[0], shif[1]]
				else:
					# find head name
					inde, bone, side, inst = BoneNameSpli(entr[0])
					brea = False
					for b in range(len(retu)):
						for c in range(len(retu[b])):
							indeComp, boneComp, sideComp, instComp = BoneNameSpli(retu[b][c][0])
							if int(inst) >= shif[0]:
								inst = shif[0] + shif[1]
								inst = Pad_(inst)
							if bone == boneComp and side == sideComp and inst == instComp:
								boneHead = ConcList([boneComp, sideComp, instComp], emptList = ["", "", "-1"])
								boneHead = Inde(boneHead, int(indeComp))
								brea = True
								break
						if brea == True:
							break
					inde, bone, side, inst = BoneNameSpli(entr[1])
					if (bone == "spin" and spinCoun > spinMini) or (bone == "shou" and shouCoun > shouMini) or (bone == "hip_" and hip_Coun > hip_Mini):
						inst = "000"
					boneTail = ConcList([bone, side, inst], emptList = ["", "", "-1"])
					boneTail = Inde(boneTail, markCoun + 1)
					boneName = Inde(entr[2], markCoun)
					locaList.append(None)
				markCoun += 1
				bran.append([boneHead, boneTail, boneName])
		a += 1
	retu.append(bran)
	rig_List = []
	for a in range(len(retu)):
		rig_List += retu[a]
	retu.insert(0, rig_List)
	if faci != "+x":
		if faci == "-x":
			for a in range(len(locaList)):
				if locaList[a] != None:
					locaList[a] = (locaList[a][0], -locaList[a][1], locaList[a][2])
		if faci == "+y":
			for a in range(len(locaList)):
				if locaList[a] != None:
					locaList[a] = (locaList[a][1], -locaList[a][0], locaList[a][2])
		if faci == "-y":
			for a in range(len(locaList)):
				if locaList[a] != None:
					locaList[a] = (locaList[a][1], locaList[a][0], locaList[a][2])
	retu.append(locaList)
	switList = []
	regiList = []
	for a in range(len(rig_List)):
		switList.append(False)
		regiList.append("s")
	retu.append(switList)
	retu.append(regiList)
	return retu

def MarkCrea(rig_List, locaList, mesh, charName = "", pref = "rig_"):
	scal = 0.2
	Empt()
	Pare(mesh)
	pare = ConcList([charName, pref])
	Name(pare)
	Scal((scal, scal, scal))
	a = 0
	while a < len(rig_List):
		rig_ = rig_List[a][0]
		loca = locaList[a]
		inde, bone, side, inst = BoneNameSpli(rig_)
		if loca != None:
			# right side will automatically be reflected from the left side
			if side != "r":
				Empt()
				Name(ConcList([charName, pref, rig_]))
				Scal((scal, scal, scal))
				ApplScal()
				Loca(loca)
				Pare(pare)
		a += 1

def Alig(branList, aligInde = 0, charName = "", pref = "rig_"):
	loca = None
	a = 0
	while a < len(branList):
		if a >= aligInde:
			if loca == None:
				if a == aligInde:
					Sele(ConcList([charName, pref, branList[a][0]]))
					loca = LocaRead()
					a = -1
			else:
				sele = ConcList([charName, pref, branList[a][0]])
				Sele(sele)
				z = LocaRead()
				Loca((loca[0], loca[1], z[2]))
		a += 1

def MarkRefl(rig_List, charName = "", pref = "rig_"):
	scal = 0.2
	pare = ConcList([charName, pref])
	for rig_ in rig_List:
		sele = ConcList([charName, pref, rig_[0]])
		obje = Sele(sele)
		if obje == None:
			reflName = MarkReflName(rig_[0], rig_List, charName = charName, pref = pref)
			Sele(reflName)
			loca = MarkReflLoca(rig_[0], rig_List, charName = charName, pref = pref, reflName = reflName)
			Empt()
			Scal((scal, scal, scal))
			ApplScal()
			Name(sele)
			Loca(loca)
			# TODO: assumes this exists
			Pare(pare)

def MarkReflLoca(markName, rig_List, charName = "", pref = "rig_", reflName = ""):
	sele = ConcList([charName, pref, markName])
	obje = Sele(sele)
	if obje == None:
		if reflName == "":
			reflName = MarkReflName(markName, rig_List, charName = charName, pref = pref)
		Sele(reflName)
	retu = LocaRead()
	if obje == None:
		# TODO: use a vector
		if retu[0] >= retu[1]:
			retu = (-retu[0], retu[1], retu[2])
		else:
			retu = (retu[0], -retu[1], retu[2])
	return retu

def MarkReflName(markName, rig_List, charName = "", pref = "rig_"):
	inde, bone, side, inst = BoneNameSpli(markName)
	for a in range(len(rig_List)):
		rig_ = rig_List[a][0]
		indeOppo, boneOppo, sideOppo, instOppo = BoneNameSpli(rig_)
		if boneOppo == bone and sideOppo != side and instOppo == inst:
			break
	return ConcList([charName, pref, indeOppo, boneOppo, sideOppo, instOppo], emptList = ["", "", "-1", "", "", "-1"])

def Rig_(mesh, rig_List, branList, charName = "", pref = "rig_", armaName = "Armature", spinCoun = 3, shouCoun = 1, hip_Coun = 1, modiName = "Armature"):
	import bpy
	Math = MathLink()
	spinMini = 3
	shouMini = 1
	hip_Mini = 1
	spinCuttLowe = 1
	shouCuttLowe = 0
	hip_CuttLowe = 0
	spinCuttUppeDiff = 1
	shouCuttUppeDiff = 0
	hip_CuttUppeDiff = 0
	def RotaMast(boneName, boneSide, coun, diff, cutt, charName = ""):
		vertList = [(0.0, 0.0, 0.0)]
		boneList = []
		for bran in branList:
			inde, bone, side, inst = BoneNameSpli(bran[0])
			if bone == boneName and side == boneSide and int(inst) >= cutt:
				longName = ConcList([inde, bone, side, inst], emptList = ["-1", "", "", "-1"])
				# TODO: can loca be used here?
				exis = False
				for a in range(len(boneList)):
					if boneList[a] == longName:
						exis = True
						break
				if exis == False:
					boneList.append(longName)
		boneList = sorted(boneList)
		if len(boneList) > 0:
			sele = ConcList([charName, pref, boneList[0]])
			Sele(sele)
			loca = LocaRead()
			Uplo([vertList, [], []])
			vers = bpy.app.version
			if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
				bpy.ops.object.move_to_collection(collection_index = 1)
			vers = bpy.app.version
			if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
				bpy.ops.object.move_to_collection(collection_index = 1)
			mastName = ConcList([charName, pref, boneName, side])
			Name(mastName)
			Loca(loca)
			# TODO: cyclic dependency
			#Pare(armaName)
			# TODO: assumes this exists
			Pare(charName)
			Sele(armaName)
			bpy.ops.object.posemode_toggle()
			for a in range(len(boneList)):
				bpy.data.objects[armaName].data.bones.active = bpy.data.objects[armaName].pose.bones[boneList[a]].bone
				bpy.ops.pose.constraint_add(type = 'COPY_ROTATION')
				bpy.data.objects[armaName].pose.bones[boneList[a]].constraints['Copy Rotation'].target = bpy.data.objects[mastName]
				bpy.data.objects[armaName].pose.bones[boneList[a]].constraints['Copy Rotation'].influence = 1.0 / diff
				bpy.data.objects[armaName].pose.bones[boneList[a]].constraints['Copy Rotation'].target_space = 'WORLD'
				bpy.data.objects[armaName].pose.bones[boneList[a]].constraints['Copy Rotation'].owner_space = 'LOCAL'
				bpy.data.objects[armaName].data.bones.active.select = False
				bpy.data.objects[armaName].data.bones.active = None
			bpy.ops.object.posemode_toggle()
	##########################
	Sele(mesh)
	bodyLoca = LocaRead()
	obje = Sele(armaName)
	fork = False
	if obje == None:
		bpy.ops.object.armature_add()
		vers = bpy.app.version
		if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
			bpy.ops.object.move_to_collection(collection_index = 1)
		Name(armaName)
		Loca(bodyLoca)
	dataName = bpy.context.object.data.name
	if len(branList) > 0:
		Sele(armaName)
		Edit()
		if branList[0][0] in bpy.data.armatures[dataName].edit_bones:
			bpy.data.armatures[dataName].edit_bones.active = bpy.data.armatures[dataName].edit_bones[branList[0][0]]
			bpy.data.armatures[dataName].edit_bones.active.select = False
			bpy.data.armatures[dataName].edit_bones.active.select_head = True
			# TODO: if a head and tail are placed in the same location, blender deletes the bone. this places it in an arbitrary position
			bpy.ops.armature.extrude_move(ARMATURE_OT_extrude = {"forked" : True}, TRANSFORM_OT_translate = {"value" : (1.23456, -1.23456, 1.23456)})
			bpy.data.armatures[dataName].edit_bones.active.select_head = False
			fork = True
		Edit()
	spinRota = False
	sholRota = False
	shorRota = False
	hiplRota = False
	hiprRota = False
	for a in range(len(branList) - 1):
		inde, bone, side, inst = BoneNameSpli(branList[a][0])
		inst = int(inst)
		locaHead = MarkReflLoca(branList[a][0], rig_List, charName = charName)
		locaTail = MarkReflLoca(branList[a][1], rig_List, charName = charName)
		Sele(armaName)
		Edit()
		# extrude a new bone
		if a != 0:
			bpy.data.armatures[dataName].edit_bones.active.select_tail = True
			# TODO: if a head and tail are placed in the same location, blender deletes the bone. this places it in an arbitrary position
			bpy.ops.armature.extrude_move(TRANSFORM_OT_translate = {"value" : (1.23456, 1.23456, 1.23456)})
			bpy.data.armatures[dataName].edit_bones.active.select_tail = False
		# place head
		if a == 0 and fork == False:
			headLoca = Math.Vect(bodyLoca, locaHead)
			bpy.data.armatures[dataName].edit_bones.active.select_head = True
			bpy.data.armatures[dataName].edit_bones.active.head = headLoca
			bpy.data.armatures[dataName].edit_bones.active.select_head = False
		# place tail
		bpy.data.armatures[dataName].edit_bones.active.select_tail = True
		bpy.data.armatures[dataName].edit_bones.active.tail = Math.Vect(bodyLoca, locaTail)
		bpy.data.armatures[dataName].edit_bones.active.select_tail = False
		# name
		bpy.data.armatures[dataName].edit_bones.active.name = branList[a][2]
		Edit()
		# master rotaters
		# TODO: what about branch bones?
		if bone == "spin" and spinCoun > spinMini and inst == 0:
			spinRota = True
		if bone == "shou" and shouCoun > shouMini and inst == shouCoun - 1:
			if side == "l":
				sholRota = True
			elif side == "r":
				shorRota = True
		if bone == "hip_" and hip_Coun > hip_Mini and inst == hip_Coun - 1:
			if side == "l":
				hiplRota = True
			elif side == "r":
				hiprRota = True
	# master rotaters
	bon_ = side = coun = cutt = ""
	# TODO: prevent branch bones from triggering master rotations
	if spinRota == True:
		bon_ = "spin"
		side = "m"
		coun = spinCoun
		diff = coun - spinCuttUppeDiff - spinCuttLowe
		cutt = spinCuttLowe
	if sholRota == True:
		bon_ = "shou"
		side = "l"
		coun = shouCoun
		diff = coun - shouCuttUppeDiff - shouCuttLowe
		cutt = shouCuttLowe
	if shorRota == True:
		bon_ = "shou"
		side = "r"
		coun = shouCoun
		diff = coun - shouCuttUppeDiff - shouCuttLowe
		cutt = shouCuttLowe
	if hiplRota == True:
		bon_ = "hip_"
		side = "l"
		coun = hip_Coun
		diff = coun - hip_CuttUppeDiff - hip_CuttLowe
		cutt = hip_CuttLowe
	if hiprRota == True:
		bon_ = "hip_"
		side = "r"
		coun = hip_Coun
		diff = coun - hip_CuttUppeDiff - hip_CuttLowe
		cutt = hip_CuttLowe
	if bon_ != "":
		RotaMast(bon_, side, coun, diff, cutt, charName = charName)

def BoneRollRese(armaName = "Armature"):
	import bpy
	Sele(armaName)
	dataName = bpy.context.object.data.name
	Edit()
	for bone in bpy.context.object.data.edit_bones:
		bone.roll = 0.0
	Edit()

def BoneRotaMode(armaName = "Armature"):
	import bpy
	Sele(armaName)
	bpy.ops.object.posemode_toggle()
	for bone in bpy.context.object.pose.bones:
		bone.rotation_mode = 'XYZ'
	bpy.ops.object.posemode_toggle()

def ArmaVolu(modiName = "Armature"):
	import bpy
	bpy.context.object.modifiers[modiName].use_deform_preserve_volume = True

def MarkRead(rig_List, boneName, charName = "", pref = "rig_"):
	for b in range(len(rig_List)):
		inde, bone, side, inst = BoneNameSpli(rig_List[b][0])
		indeComp, boneComp, sideComp, instComp = BoneNameSpli(boneName)
		if bone == boneComp and side == sideComp and inst == instComp:
			break
	return ConcList([charName, pref, inde, bone, side, inst], emptList = ["", "", "-1", "", "", "-1"])

# override - markers are selected automatically. override automatic selection:
# "rig_": select "rig_" marker
# "loop": select "rig_.loop" marker
def LoopNear(mesh, mark, swit = False, override = ""):
	import bpy
	obje = Sele(mark + "." + "loop.000")
	retu = []
	if obje != None and override != "rig_" and override != "loop":
		vertList = []
		a = 1
		while obje != None:
			loca = LocaRead()
			Sele(mesh)
			vertList.append(VertIndeBy__Loca(loca, False))
			obje = Sele(mark + "." + "loop." + Pad_(a))
			a += 1
		loop = []
		for a in range(len(vertList) - 1):	
			PathShor(vertList[a], vertList[a + 1])
			loop += VertListSele()
		VertSele(loop)
		if len(loop) > 1:
			retu = [loop[0], loop[1]]
	else:
		if override != "loop":
			obje = Sele(mark)
		if override != "rig_" or obje == None:
			Sele(mark + "." + "loop")
		loca = LocaRead()
		Sele(mesh)
		inde = VertIndeBy__Loca(loca, False)
		vertList = VertConn(inde)
		# select all combinations and get the vert count
		vertCoun = -1
		vertInde = -1
		for a in range(len(vertList)):
			VertSele([inde, vertList[a]])
			Loop()
			try:
				import numpy
				leng = len(Vertices())
				sele = numpy.zeros(leng, dtype = bool)
				bpy.context.object.data.vertices.foreach_get('select', sele)
				sele = sele[sele]
				coun = len(sele)
			except:
				# TODO: doesnt work. maybe this is not updated?
				#coun = bpy.context.object.data.total_vert_sel
				coun = 0
				for b in range(len(Vertices())):
					if bpy.context.object.data.vertices[b].select == True:
						coun += 1
			if vertCoun == -1 or (swit != True and coun < vertCoun) or (swit == True and coun > vertCoun):
				vertCoun = coun
				vertInde = a
		retu = [inde, vertList[vertInde]]
		VertSele(retu)
		Loop()
	return retu

# "s" - successive. select the region between two loops
# "f" - fill. select all vertices from a loop to the end of an appendage
# [] - list. select the region between a set of loops
def LoopRegi(mesh, inde, rig_List, switList, typ_ = "s", charName = "", pref = "rig_"):
	import bpy
	fill = True
	if typ_ == "s" or typ_ == "f":
		mark = MarkRead(rig_List, rig_List[inde][0], charName = charName, pref = pref)
		LoopNear(mesh, mark, swit = switList[inde])
		ver1List = VertListSele()
		mark = MarkRead(rig_List, rig_List[inde + 1][0], charName = charName, pref = pref)
		LoopNear(mesh, mark, swit = switList[inde + 1])
		ver2List = VertListSele()
		if typ_ == "f":
			ver2List = []
		vertList = ver1List + ver2List
		# if one loop is connected to the other, don't fill
		brea = False
		for a in range(len(ver1List)):
			conn = VertConn(ver1List[a])
			for con_ in conn:
				for b in range(len(ver2List)):
					if con_ == ver2List[b]:
						fill = False
						brea = True
						break
				if brea == True:
					break
			if brea == True:
				break
	if type(typ_) == list:
		vertList = []
		for loop in typ_:
			mark = MarkRead(rig_List, rig_List[loop][0], charName = charName, pref = pref)
			LoopNear(mesh, mark, swit = switList[loop])
			vertList += VertListSele()
	if typ_ == "f":
		fill = True
	VertSele(vertList)
	if fill == True:
		Regi()

def Skin(mesh, inde, rig_List, switList, typ_Regi = "s", charName = "", pref = "rig_"):
	if typ_Regi != None:
		LoopRegi(mesh, inde, rig_List, switList, typ_ = typ_Regi, charName = charName, pref = pref)
		vertList = VertListSele()
		VertGrou(rig_List[inde][0], vertList)
		VertDese()

# ! make sure modiName doesn't clash with an existing modifier name or the wrong one will be set
def SkinAll_(mesh, rig_List, switList, regiList, armaName = "Armature", add_Modi = True, modiName = "Armature", charName = "", pref = "rig_"):
	import bpy
	if add_Modi == True:
		Sele(mesh)
		bpy.context.object.modifiers.new(modiName, type = 'ARMATURE')
		bpy.context.object.modifiers[modiName].object = bpy.data.objects[armaName]
	Sele(mesh)
	VertDese()
	for a in range(len(regiList)):
		print("grouping", a, "of", len(regiList) - 1)
		Skin(mesh, a, rig_List, switList, typ_Regi = regiList[a], charName = charName, pref = pref)

def SkinExtr(objeList, grouName, armaName = "Armature", modiName = "Armature"):
	import bpy
	for obje in objeList:
		Sele(obje)
		# ! make sure modiName doesn't clash with an existing modifier
		bpy.context.object.modifiers.new(modiName, type = 'ARMATURE')
		bpy.context.object.modifiers[modiName].object = bpy.data.objects[armaName]
		VertSeleAll_()
		vertList = VertListSele()
		VertGrou(grouName, vertList)
		bpy.context.object.vertex_groups[grouName].add(vertList, 1.0, type = 'ADD')

def SpliRead(charName = ""):
	spliList = []
	spliList.append(charName + "." + "head.m")
	spliList.append(charName + "." + "wris.l")
	spliList.append(charName + "." + "elbo.l")
	spliList.append(charName + "." + "shou.l")
	spliList.append(charName + "." + "ankl.l")
	spliList.append(charName + "." + "knee.l")
	spliList.append(charName + "." + "hip_.l")
	spliList.append(charName + "." + "wris.r")
	spliList.append(charName + "." + "elbo.r")
	spliList.append(charName + "." + "shou.r")
	spliList.append(charName + "." + "ankl.r")
	spliList.append(charName + "." + "knee.r")
	spliList.append(charName + "." + "hip_.r")
	switList = []
	for a in range(len(spliList)):
		switList.append(False)
	pareDict = {}
	pareDict.update({charName + "." + "head.m": charName + "." + "body"})
	pareDict.update({charName + "." + "wris.l": charName + "." + "elbo.l"})
	pareDict.update({charName + "." + "elbo.l": charName + "." + "shou.l"})
	pareDict.update({charName + "." + "shou.l": charName + "." + "body"})
	pareDict.update({charName + "." + "ankl.l": charName + "." + "knee.l"})
	pareDict.update({charName + "." + "knee.l": charName + "." + "hip_.l"})
	pareDict.update({charName + "." + "hip_.l": charName + "." + "body"})
	pareDict.update({charName + "." + "wris.r": charName + "." + "elbo.r"})
	pareDict.update({charName + "." + "elbo.r": charName + "." + "shou.r"})
	pareDict.update({charName + "." + "shou.r": charName + "." + "body"})
	pareDict.update({charName + "." + "ankl.r": charName + "." + "knee.r"})
	pareDict.update({charName + "." + "knee.r": charName + "." + "hip_.r"})
	pareDict.update({charName + "." + "hip_.r": charName + "." + "body"})
	flipList = []
	flipList.append([False, True])
	flipList.append([False, True])
	flipList.append([True, False])
	flipList.append([True, False])
	flipList.append([False, True])
	flipList.append([True, False])
	flipList.append([True, False])
	flipList.append([True, False])
	flipList.append([False, True])
	flipList.append([False, True])
	flipList.append([True, False])
	flipList.append([False, True])
	flipList.append([False, True])
	return spliList, switList, pareDict, flipList

def LoopList(mesh, spliList, rig_List, switList, charName = ""):
	Sele(mesh)
	retu = []
	for a in range(len(spliList)):
		VertDese()
		mark = MarkRead(rig_List, spliList[a], charName = charName)
		ver1, ver2 = LoopNear(mesh, mark, swit = switList[a])
		ver1 = VertLoca([ver1])
		ver1 = ver1[0]
		ver2 = VertLoca([ver2])
		ver2 = ver2[0]
		retu.append([ver1, ver2])
	return retu

def LoopListRead(fileName = "list/loop"):
	Pyth = PythLink()
	retu = []
	loopList = Pyth.FileTo__Line(fileName)
	for a in range(len(loopList)):
		retu.append(Pyth.StriListTo__Tupl(loopList[a]))
	return retu

def LoopListWrit(loopList, fileName = "list/loop"):
	Pyth = PythLink()
	retu = []
	for a in range(len(loopList)):
		retu.append(Pyth.TuplListTo__Stri(loopList[a]))
	Pyth.LineTo__File(retu, fileName)

def MeshSpli(mesh, spliList, loopList, rig_List, flipList, charName = "", pref = "rig_"):
	import bpy
	for a in range(len(spliList)):
		spli = spliList[a]
		mark = MarkRead(rig_List, spli, charName = charName, pref = pref)
		# split
		MeshSpliPart(mesh, spli, mark, loopList[a], charName = charName)
		# socket
		sock = True
		# TODO: assumes 0 is the head
		if a == 0:
			sock = not sock
		BallAnd_Sock(mesh, mark, loopList[a], sock = sock, flip = flipList[a][0])
		# ball
		BallAnd_Sock(spli, mark, loopList[a], sock = not sock, flip = flipList[a][1])
		print("split", a + 1, "of", len(spliList))

def MeshSpliPart(copy, spli, mark, vertList, charName = ""):
	import bpy
	Math = MathLink()
	Sele(copy)
	Name("mesh_spli_temp")
	vertLocaList = []
	for a in range(len(vertList)):
		vertLocaList.append(VertIndeBy__Loca(vertList[a]))
	VertSele(vertLocaList)
	Loop()
	Dupl()
	Name(copy)
	ver1List = VertListSele()
	Regi()
	ver2List = VertListSele()
	for a in range(len(ver1List)):
		b = 0
		while b < len(ver2List):
			if ver1List[a] == ver2List[b]:
				ver2List.pop(b)
				b = -1
			b += 1
	VertDese()
	VertSele(ver2List)
	VertDele()
	# remove unused materials from the object
	MatePurgObje()
	Sele("mesh_spli_temp")
	# set origin
	# TODO: using cursor to selected on a loop doesn't match vect average
	#Edit()
	#CursTo__Sele(edit = True)
	#Edit()
	# workaround
	ver2List = VertListSele()
	ver2List = VertLoca(ver2List)
	aver = Math.VectAver(ver2List)
	Curs(aver)
	OrigCurs()
	Regi()
	Edit()
	bpy.ops.mesh.select_all(action = 'INVERT')
	Edit()
	VertDele()
	Name(spli)
	MatePurgObje()

def BallAnd_Sock(part, mark, vertList, sock = False, flip = False):
	import bpy
	Math = MathLink()
	Sele(part)
	# store the transformation of the object
	scal, rota, loca = TranRead()
	# get the locations of the vertices in the loop
	vertLocaList = []
	for a in range(len(vertList)):
		vertLocaList.append(VertIndeBy__Loca(vertList[a]))
	VertSele(vertLocaList)
	Loop()
	vertLocaList = VertListSele()
	vertLocaList = VertLoca(vertLocaList)
	cent = Math.VectAver(vertLocaList)
	for a in range(len(vertLocaList)):
		vertLocaList[a] = Math.Vect(cent, vertLocaList[a])
	# sort the vertex list by angle from center
	# TODO: slow
	vertAngl = []
	if len(vertLocaList) > 0:
		vertAngl = [[0, vertLocaList[0]]]
	a = 0
	while len(vertAngl) < len(vertLocaList):
		diffList = []
		for b in range(len(vertLocaList)):
			if a != b and vertLocaList[b] != None:
				vect = Math.Vect(vertLocaList[a], vertLocaList[b])
				diff = Math.VectMagn(vect)
				diffList.append([diff, b])
		diffList = sorted(diffList)
		inde = diffList[0][1]
		vertAngl.append([inde, vertLocaList[inde]])
		vertLocaList[a] = None
		a = inde
	vertLocaList = []
	magnList = []
	for vect in vertAngl:
		vertLocaList.append(vect[1])
		magn = Math.VectMagn(vect[1])
		magnList.append(magn)
	# get the average cross product of adjacent vectors to find the cap of a semi-sphere that joins the loop
	# TODO: better way to do this
	magnTota = 0.0
	crosList = []
	a = 0
	while a < len(vertLocaList) - 1:
		vec1 = vertLocaList[a]
		vec2 = vertLocaList[a + 1]
		crosVect = Math.VectCros3d__(vec1, vec2)
		# if the vector is pointing down, flip it
		# TODO: (0.0, 0.0, 1.0) might be arbitrary
		faci = Math.Faci((0.0, 0.0, 1.0), (0.0, 0.0, 0.0), crosVect)
		if faci == False:
			crosVect = Math.VectScal(crosVect, -1.0)
		if Math.VectMagn(crosVect) <= 0.01:
			crosVect = Math.VectScal(crosVect, 10.0)
		crosList.append(crosVect)
		magn = Math.VectMagn(vertLocaList[a])
		magnTota += magn
		a += 1
	vec1 = vertLocaList[0]
	vec2 = vertLocaList[a]
	crosList.append(Math.VectCros3d__(vec1, vec2))
	magn = Math.VectMagn(vertLocaList[a])
	magnTota += magn
	magnTota /= a + 1
	head = Math.VectAver(crosList)
	head = Math.VectNorm(head)
	head = Math.VectScal(head, magnTota)
	# get the material of a polygon adjacent to the loop
	Edit()
	bpy.ops.mesh.select_more()
	Edit()
	try:
		import numpy
		leng = len(Polygons())
		sele = numpy.zeros(leng, dtype = bool)
		inte = numpy.arange(leng)
		bpy.context.object.data.polygons.foreach_get('select', sele)
		sele = inte[sele]
		sele = list(sele)
	except:
		sele = []
		for a in range(len(Polygons())):
			if bpy.context.object.data.polygons[a].select == True:
				sele.append(a)
	mateSlot = -1
	if len(sele) > 0:
		mateSlot = bpy.context.object.data.polygons[sele[0]].material_index
	Edit()
	bpy.ops.mesh.select_less()
	Edit()
	# build a semi-sphere
	# TODO: try to preserve loop selections (look at Math.Sphe())
	new_VertList = []
	edgeList = []
	polyList = []
	segsNumb = 8
	brea = False
	i = 0
	a = 0
	while a < len(vertLocaList):
		# get the length of the vector from the center of the loop to the vertex
		magn = magnList[a]
		vect = vertLocaList[a]
		axis = Math.VectCros3d__(vect, head)
		axis = Math.VectNorm(axis)
		for b in range(segsNumb):
			# draw an arc that connects the vertex to the direction vector
			angl = b * 90.0 / segsNumb
			magnAdju = magn + (b / (segsNumb - 1)) * (magnTota - magn)
			vectNew_ = Math.Quat(vect, angl, axis)
			vectNew_ = Math.VectNorm(vectNew_)
			vectNew_ = Math.VectScal(vectNew_, magnAdju)
			new_VertList.append(vectNew_)
			# rings
			if b < segsNumb - 1:
				edgeList.append((i, i + 1))
			i += 1
			# loops
			if a > 0 and a < len(vertLocaList) - 1 or (a == 0 and b == segsNumb - 1) or (a == len(vertLocaList) - 1 and b != segsNumb - 1):
				edgeList.append((i, i - segsNumb))
			# add faces
			if a > 0 and b < segsNumb - 1:
				polyList.append((i - segsNumb, i, i - 1, i - 1 - segsNumb))
		a += 1
	# last ring
	for a in range(segsNumb):
		edgeList.append((a, i - segsNumb))
		i += 1
		if a < segsNumb - 1:
			polyList.append((a + 1, a, i - segsNumb - 1, i - segsNumb))
	# cap
	new_VertList.append(head)
	a = 0
	while a < len(vertLocaList):
		edgeList.append((a * segsNumb + segsNumb - 1, len(new_VertList) - 1))
		if a < len(vertLocaList) - 1:
			polyList.append(((a + 1) * segsNumb + segsNumb - 1, a * segsNumb + segsNumb - 1, len(new_VertList) - 1))
		a += 1
	polyList.append((segsNumb - 1, (a - 1) * segsNumb + segsNumb - 1, len(new_VertList) - 1))
	# apply global position to all vertices
	for a in range(len(new_VertList)):
		new_VertList[a] = Math.Tran3d__(new_VertList[a], scal, rota, loca)
	# upload
	Uplo([new_VertList, edgeList, polyList])
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = 1)
	if flip == True:
		Flip()
	Loca(cent)
	new_Obje = bpy.context.object.name
	# shade smooth
	Edit()
	bpy.ops.mesh.faces_shade_smooth()
	Edit()
	Sele(part)
	# join
	Join(new_Obje)
	# remove doubles
	VertDoub()
	# flip the normals to the inside if the cap is a socket
	# TODO: socket will be see-through in game mode unless the material is set to two-sided
	if sock == True:
		vertLocaList = []
		for a in range(len(vertList)):
			vertLocaList.append(VertIndeBy__Loca(vertList[a]))
		VertSele(vertLocaList)
		Loop()
		Regi()
		Edit()
		bpy.ops.mesh.flip_normals()
		Edit()
		VertDese()
	if mateSlot != -1:
		vertLocaList = []
		for a in range(len(vertList)):
			vertLocaList.append(VertIndeBy__Loca(vertList[a]))
		VertSele(vertLocaList)
		Loop()
		Regi()
		Edit()
		bpy.context.object.active_material_index = mateSlot
		bpy.ops.object.material_slot_assign()
		Edit()
		VertDese()

def MatePurgObje():
	import bpy
	VertDese()
	mode = tuple(bpy.context.tool_settings.mesh_select_mode)
	bpy.context.tool_settings.mesh_select_mode = (False, False, True)
	remo = []
	for a in range(len(bpy.context.object.material_slots)):
		bpy.context.object.active_material_index = a
		Edit()
		bpy.ops.object.material_slot_select()
		Edit()
		try:
			import numpy
			leng = len(Polygons())
			sele = numpy.zeros(leng, dtype = bool)
			bpy.context.object.data.polygons.foreach_get('select', sele)
			sele = sele[sele]
			coun = len(sele)
		except:
			coun = 0
			for a in range(len(Polygons())):
				if bpy.context.object.data.polygons[a].select == True:
					coun += 1
		VertDese()
		if coun == 0:
			remo.append(a)
	a = len(remo) - 1
	while a >= 0:
		bpy.context.object.active_material_index = remo[a]
		bpy.ops.object.material_slot_remove()
		a -= 1
	bpy.context.tool_settings.mesh_select_mode = mode

# back up vertex positions
def VertBack(fileName = "vert_loca"):
	Pyth = PythLink()
	vertList = VertListSele()
	vertListLoca = VertLoca(vertList)
	retu = []
	retu.append(Pyth.ListTo__Stri(vertList))
	retu.append(Pyth.ListTo__Stri(vertListLoca))
	Pyth.LineTo__File(retu, fileName)

# restore vertex positions
def VertRest(fileName = "vert_loca"):
	import bpy
	Pyth = PythLink()
	vertList = Pyth.FileTo__Line(fileName)
	vertListLoca = vertList[1]
	vertList = vertList[0]
	vertList = Pyth.StriListTo__Int_List(vertList)
	vertListLoca = Pyth.StriListTo__Tupl(vertListLoca)
	for a in range(len(vertList)):
		bpy.context.object.data.vertices[vertList[a]].co = vertListLoca[a]

def WeigBack(fileName = "weig"):
	import bpy
	Pyth = PythLink()
	retu = []
	for a in range(len(bpy.context.object.vertex_groups)):
		grou = bpy.context.object.vertex_groups[a]
		grouLine = ""
		VertDese()
		# get vertices in group
		VertGrouSele(grou.name)
		grouLine = grou.name + " "
		vertList = VertListSele(meth = 2)
		for b in range(len(vertList)):
			grouLine += str(vertList[b]) + " " + str(grou.weight(vertList[b])) + " "
		grouLine = grouLine[0:len(grouLine) - 1]
		retu.append(grouLine)
	Pyth.LineTo__File(retu, fileName)

def WeigRest(fileName = "weig"):
	import bpy
	Pyth = PythLink()
	weig = Pyth.FileTo__Line(fileName)
	nameList = []
	vertList = []
	weigList = []
	for a in range(len(weig)):
		grouVertList = []
		grouWeig = weig[a].split(" ")
		nameList.append(grouWeig[0])
		grouWeigList = []
		b = 1
		while b < len(grouWeig):
			grouVertList.append(int(grouWeig[b]))
			grouWeigList.append(float(grouWeig[b + 1]))
			b += 2
		vertList.append(grouVertList)
		weigList.append(grouWeigList)
	for a in range(len(nameList)):
		bpy.ops.object.vertex_group_add()
		grouNumb = -1
		for b in range(len(bpy.context.object.vertex_groups)):
			grouName = bpy.context.object.vertex_groups[b].name
			grouName = grouName.split(".")
			if len(grouName) > 0:
				if grouName[0] == 'Group':
					grouNumb = b
		bpy.context.object.vertex_groups[grouNumb].name = nameList[a]
		for b in range(len(vertList[a])):
			bpy.context.object.vertex_groups[grouNumb].add([vertList[a][b]], weigList[a][b], type = 'ADD')

#############################################

# ANIMATION FUNCTIONS

def Fram(fram):
	import bpy
	bpy.context.scene.frame_current = fram

# TODO: should set_ default to True
def Key_Rota(obje, rota, glob = True, set_ = False):
	import bpy
	if obje == None:
		obje = bpy.context.object.name
	Sele(obje)
	if rota != None:
		# TODO: local?
		if set_ == False:
			if glob == True:
				Rota(rota)
			else:
				Rota(rota, loca = True)
		else:
			RotaSet_(rota)
	bpy.ops.anim.keyframe_insert(type='Rotation', confirm_success=False)

def Key_Loca(obje, loca, glob = True):
	import bpy
	if obje == None:
		obje = bpy.context.object.name
	Sele(obje)
	if loca != None:
		if glob == True:
			Loca(loca)
		else:
			Loca(loca, worl = False)
	bpy.ops.anim.keyframe_insert(type='Location', confirm_success=False)

def Key_Visi():
	import bpy
	bpy.context.object.keyframe_insert(data_path = 'hide')
	bpy.context.object.keyframe_insert(data_path = 'hide_render')

def Key_Arms():
	import bpy
	name = bpy.context.object.name
	lis_ = [name + ".shoulder.l", name + ".elbow.l", name + ".wrist.l", name + ".shoulder.r", name + ".elbow.r", name + ".wrist.r"]
	for bone in lis_:
		Sele(bone)
		bpy.ops.anim.keyframe_insert(type='Rotation', confirm_success = False)

def Key_Legs():
	import bpy
	name = bpy.context.object.name
	lis_ = [name + ".hip.l", name + ".knee.l", name + ".ankle.l", name + ".hip.r", name + ".knee.r", name + ".ankle.r"]
	for bone in lis_:
		Sele(bone)
		bpy.ops.anim.keyframe_insert(type='Rotation', confirm_success = False)

# TODO

#######################

#def Cycl(name, track, t, radi, speed, ik_1, ik_2, end, left, arms, arms_rati, thi, shi, facing_angle, path_star, Engi = None):

# TODO: path_star

# storProp - set to True to store the cycle path in a property list (read from a file), otherwise write to a file
def CyclPathRead(blenFile = "cycl_jog__legs", storProp = False, faci = (1.0, 0.0)):
	import os
	Pyth = PythLink()
	Head = HeadLink()
	blenComm = BlenCommLink()
	dire, blenName = FilePath(blenFile)
	# write the blend to read from a file
	writ = {}
	writ.update({"blenName":blenName})
	writ.update({"faci":faci})
	Pyth.LineTo__File(Pyth.DictTo__Line(writ), "list" + os.sep + "expo")
	# write a script to be executed in a new instance of blender which writes the length and angle of each point from "path" object to a file
	scri = Head()
	scri += "def main():\n"
	scri += "\timport bpy\n"
	scri += "\timport math\n"
	scri += "\tline = Pyth.FileTo__Line(\"list" + os.sep + "expo\")\n"
	scri += "\tline = Pyth.LineTo__Dict(line)\n"
	scri += "\tvertList = []\n"
	#scri += "\tradiList = []\n"
	scri += "\tBlen.Sele(\"path\")\n"
	scri += "\tfor vert in bpy.context.object.data.vertices:\n"
	#scri += "\t\tmagn = Math.VectMagn(vert.co)\n"
	#scri += "\t\tangl = math.atan2(vert.co.z, vert.co.x)\n"
	#scri += "\t\tif line[\"faci\"] == (0.0, 1.0) or line[\"faci\"] == (0.0, -1.0):\n"
	#scri += "\t\t\tangl = math.atan2(vert.co.z, vert.co.y)\n"
	#scri += "\t\twhile angl < 0.0:\n"
	#scri += "\t\t\tangl += 2.0 * math.pi\n"
	#scri += "\t\twhile angl >= 2.0 * math.pi:\n"
	#scri += "\t\t\tangl -= 2.0 * math.pi\n"
	#scri += "\t\tradiList.append((magn, angl))\n"
	scri += "\t\tvertList.append(tuple(vert.co))\n"
	#scri += "\tPyth.LineTo__File(Pyth.TuplListExpo(radiList), \"list\" + os.sep + line[\"blenName\"])\n"
	scri += "\tPyth.LineTo__File(Pyth.TuplListExpo(vertList), \"list\" + os.sep + line[\"blenName\"])\n"
	scri += "main()\n"
	fileObje = open("tempScri.py", mode = "w")
	fileObje.write(scri)
	fileObje.close()
	# write an expression to execute tempScri.py from the command line
	expr = ""
	expr += blenComm + " -b " + dire + blenName + ".blend"	
	expr += " --python tempScri.py"
	# execute
	os.system(expr)
	# if store as property option is true, store the vectors to properties
	if storProp == True:
		BlenGame = BlenGameLink()
		line = Pyth.FileTo__Line("list" + os.sep + blenName)
		for a in range(len(line)):
			vert = Pyth.StriTo__Tupl(line[a])
			BlenGame.Prop(propName = blenFile + "." + Pad_(a) + "." + "x", propType = 'FLOAT', propValu = vert[0])
			BlenGame.Prop(propName = blenFile + "." + Pad_(a) + "." + "y", propType = 'FLOAT', propValu = vert[1])
			BlenGame.Prop(propName = blenFile + "." + Pad_(a) + "." + "z", propType = 'FLOAT', propValu = vert[2])
			#radi = Pyth.StriTo__Tupl(line[a])
			#BlenGame.Prop(propName = blenFile + "." + Pad_(a) + "." + "magn", propType = 'FLOAT', propValu = radi[0])
			#BlenGame.Prop(propName = blenFile + "." + Pad_(a) + "." + "angl", propType = 'FLOAT', propValu = radi[1])

# TODO: end is not being used. use end or length?
def Cycl(name = "", axle = "axle.legs.l", t = 0.0, radi = 0.2, spee = 0.1, uppe = "", lowe = "", end_ = "", righ = False, arms = False, armsPath = True, armsRati = 0.05, uppeLeng = 1.0, loweLeng = 1.0, faci = (1.0, 0.0), pathStar = 2, path = [], pathName = "cycl_jog__legs", steps = 32):
	import bpy
	import math
	import mathutils
	Math = MathLink()
	#print("ar", armsRati)
	part = "axle."
	if arms == 0:
		part += "legs."
	else:
		part += "arms."
	# TODO
	phas = 0.0
	if righ == False:
		part += "l"
		if arms == False:
			phas = -math.pi / 1.0
	else:
		part += "r"
		if arms == True:
			phas = -math.pi / 1.0
	#print("phas", phas)
	nameStri = name + "." + part
	if arms == False or (arms == True and armsPath == True):
		#peda = CyclPath(t = t, acti = acti, spee = spee, radi = radi, phas = phas, righ = righ, arms = arms)
		left = 1
		if righ == True:
			left = 0
		if path != []:
			steps = len(path)
		# TODO: how to rebuild a loop
		steps = 16
		#print(steps)
		peda = CyclPath(t, spee, radi, phas, steps, left, 0, pathStar, charName = name, pathName = pathName, path = path, faci = faci)
		#print(peda)
	else:
		#print("ar", armsRati)
		# TODO: why -t
		peda = Math.Elli(t = -t, spee = spee, radi = radi, phas = phas, rati = armsRati)
	peda = Math.VectScal(peda, radi)
	#axlePosi = scen.objects[axle].localPosition
	Sele(axle)
	axlePosi = LocaRead()
	#print(axlePosi)
	tota = uppeLeng + loweLeng
	# the distance from hip where the foot should be
	#uppePosi = scen.objects[uppe].localPosition
	Sele(uppe)
	uppePosi = LocaRead()
	#print(uppePosi)
	# TODO: convert x/y to x using faci
	uppePosi = (uppePosi[0], 0.0, uppePosi[2])
	targPosi = (peda[0] + axlePosi[0], 0.0, peda[1] + axlePosi[2])
	#uppePosi = (0.0, uppePosi[1], uppePosi[2])
	#targPosi = (0.0, peda[0] + axlePosi[1], peda[1] + axlePosi[2])
	difx = targPosi[0] - uppePosi[0]
	dify = targPosi[2] - uppePosi[2]
	angl = math.atan2(dify, difx) + math.pi / 2.0
	#angl = math.atan2(dify, difx)
	#angl = math.atan2(dify, difx) - math.pi / 2.0
	A = Math.Dist(uppePosi, targPosi)
	if A > tota:
		A = tota
	uppeAngl, loweAngl = Math.Ik2d(arms = arms, A = A, angl = angl, uppeLeng = uppeLeng, loweLeng = loweLeng)
	#eule = mathutils.Euler((faci[1] * uppeAngl, -faci[0] * uppeAngl, 0.0), 'XYZ')
	#scen.objects[uppe].localOrientation = eule.to_matrix()
	#eule = mathutils.Euler((faci[1] * loweAngl, -faci[0] * loweAngl, 0.0), 'XYZ')
	#scen.objects[lowe].localOrientation = eule.to_matrix()
	#print(faci)
	#print(uppeAngl, loweAngl)
	Sele(uppe)
	RotaSet_((math.degrees(faci[1] * uppeAngl), math.degrees(-faci[0] * uppeAngl), 0.0))
	#RotaSet_((faci[1] * uppeAngl, -faci[0] * uppeAngl, 0.0))
	Sele(lowe)
	RotaSet_((math.degrees(faci[1] * loweAngl), math.degrees(-faci[0] * loweAngl), 0.0))
	#RotaSet_((faci[1] * loweAngl, -faci[0] * loweAngl, 0.0))

# TODO: make an interpolate function. (incremented and non-incremented interpolate)
# (rigging / skinning)
# incr = shif[1] / cuttDiff
# heig = star[2] - star[2] * incr + end_[2] * incr

"""
def CyclPath(t, speed, radius, phase, steps, left, arms, start, path = [], pathName = "cycl_jog__legs", charName = "beam", faci = (1.0, 0.0)):
	import bpy
	import math
	Math = MathLink()
	#start = 0
	# TODO
	# is this where phase goes?
	# should t be going forward or backward?
	pedal_speed = speed
	ground_height = 0.0
	y = math.sin(t * 2.0 * math.pi * pedal_speed + phase)
	x = math.cos(t * 2.0 * math.pi * pedal_speed + phase)
	# TODO:
	# fix this?
	# is this where phase goes?
	#x = math.cos(-t * 2.0 * math.pi * pedal_speed + phase)
	#y = math.sin(-t * 2.0 * math.pi * pedal_speed + phase)
	# TODO
	#if left == 1 and arms == 0 and 1 == 0:
	##if left == 1 and arms == 0:
	#	Sele("Sphere")
	#	loc = (x, y, 0.0)
	#	Loca(loc)
	#	bpy.ops.anim.keyframe_insert(type='Location', confirm_success=False)
	angle = math.atan2(y, x)
	#angle = t * 2.0 * math.pi * pedal_speed + phase
	#print("angle", math.degrees(angle))
	#angle += phase
	while angle < 0.0:
		angle += 2.0 * math.pi
	while angle >= 2.0 * math.pi:
		angle -= 2.0 * math.pi
	# TODO: this isnt correct. need to get the angle to each point
	step = int((angle / (2.0 * math.pi)) * (steps - 0))
	#print("step", step)
	# TODO: step, next_step, adjust both if necessary
	step += start
	next_step = step + 1
	if step >= steps:
		step -= steps
	if next_step >= steps:
		next_step -= steps
	#if left == 1 and arms == 0:
	#	print("step, next", step, next_step)
	# TODO: find a better way to do this
	astep = 2.0 * math.pi / steps
	# find the angle remainder
	angle_remainder = angle
	while angle_remainder >= astep:
		angle_remainder -= astep
	# for non-adjusted angle, the ratio of progress (a) to a full step (b)
	progress = angle_remainder / astep
	# TODO: bad way to do this
	#Sele("path")
	# TODO: x and z or y and z or x and y
	##start_x = bpy.context.object.data.vertices[step].co.y
	#start_x = bpy.context.object.data.vertices[step].co.x
	#start_y = bpy.context.object.data.vertices[step].co.z
	##end_x = bpy.context.object.data.vertices[next_step].co.y
	#end_x = bpy.context.object.data.vertices[next_step].co.x
	#end_y = bpy.context.object.data.vertices[next_step].co.z
	# TODO: test this
	# if faci is default, read x/z
	dimlInte = 0
	dimhInte = 2
	dimlStri = "x"
	dimhStri = "z"
	# if faci is not default, read y/z
	if faci == (0.0, 1.0) or faci == (0.0, -1.0):
		dimlInte = 1
		dimlStri = "y"
	if path != []:
		start_x = path[step][dimlInte]
		start_y = path[step][dimhInte]
		end_x = path[next_step][dimlInte]
		end_y = path[next_step][dimhInte]
	else:
		# TODO:
		Sele(charName)
		# TODO: read vari name from a single location
		variName = pathName + "." + Pad_(step)
		start_x = bpy.context.object.properties[variName + "." + dimlStri]
		start_y = bpy.context.object.properties[variName + "." + dimhStri]
		variName = pathName + "." + Pad_(next_step)
		end_x = bpy.context.object.properties[variName + "." + dimlStri]
		end_y = bpy.context.object.properties[variName + "." + dimhStri]

	# angle from origin to x,y start of this step
	theta_a = math.atan2(start_y, start_x)
	while theta_a < 0.0:
		theta_a += 2.0 * math.pi
	while theta_a >= 2.0 * math.pi:
		theta_a -= 2.0 * math.pi
	theta_b = math.atan2(end_y, end_x)
	while theta_b < 0.0:
		theta_b += 2.0 * math.pi
	while theta_b >= 2.0 * math.pi:
		theta_b -= 2.0 * math.pi
	#Sele("a")
	#bpy.context.object.rotation_euler[0] = theta_a
	#bpy.ops.anim.keyframe_insert(type='Rotation', confirm_success = False)
	#Sele("b")
	#bpy.context.object.rotation_euler[0] = theta_b
	#bpy.ops.anim.keyframe_insert(type='Rotation', confirm_success = False)
	# get the difference between the new angle and min angle
	# angle between this step and the next step
	# TODO:
	#if step != steps - 1:
	#	angle_diff = theta_b - theta_a
	#else:
	#	angle_diff = 2.0 * math.pi - theta_a
	##while angle_diff >= 2.0 * math.pi:
	##	angle_diff -= 2.0 * math.pi
	angle_diff = Math.VectAngl((start_x, start_y), (end_x, end_y))
	angle_diff = math.radians(angle_diff)
	# TODO: this worked, then it didn't work. related to applying path rotation, previously 180.
	#	this is probably correct, along with applying rotation. fix something else
	#angle_diff *= -1.0
	# TODO: lay cycle paths flat
	while angle_diff >= 2.0 * math.pi:
		angle_diff -= 2.0 * math.pi
	while angle_diff < 0.0:
		angle_diff += 2.0 * math.pi
	# angle_diff is "theta_2". a / b = t1 / t2. solve for t1
	progress *= angle_diff
	# add adjusted progress to theta a, the start of this step
	theta_a += progress

	# TODO: is this right?
	x = math.cos(theta_a)
	y = math.sin(theta_a)
	#x = math.cos(math.radians(theta_a))
	#y = math.sin(math.radians(theta_a))
	#x = radius * math.cos(theta_a)
	#y = radius * math.sin(theta_a)
	# new radius: intersection between theta a and line from start x y to end x y
	m1 = (y / x)
	b1 = 0.0
	#print(end_x, start_x)
	m2 = (end_y - start_y) / (end_x - start_x)
	b2 = (end_y) - m2 * (end_x)
	X = (b2 - b1) / (m1 - m2)
	Y = m1 * X



	##if left == 1 and arms == 0:
	#if left == 1 and arms == 0 and 1 == 0:
	#	Sele("Sphere")
	#	loc = (X, Y, 0.0)
	#	Loca(loc)
	#	bpy.ops.anim.keyframe_insert(type='Location', confirm_success=False)
	return X, Y
"""

def CyclPath(t, speed, radius, phase, steps, left, arms, start, path = [], pathName = "cycl_jog__legs", charName = "beam", faci = (1.0, 0.0)):
	import bpy
	import math
	Math = MathLink()
	#start = 0
	# TODO
	# is this where phase goes?
	# should t be going forward or backward?
	pedal_speed = speed
	ground_height = 0.0
	#y = math.sin(t * 2.0 * math.pi * pedal_speed + phase)
	#x = math.cos(t * 2.0 * math.pi * pedal_speed + phase)
	y = math.sin(t * 2.0 * math.pi * pedal_speed)
	x = math.cos(t * 2.0 * math.pi * pedal_speed)
	angle = math.atan2(y, x)
	angle += phase
	while angle < 0.0:
		angle += 2.0 * math.pi
	while angle >= 2.0 * math.pi:
		angle -= 2.0 * math.pi
	step = int((angle / (2.0 * math.pi)) * (steps))
	# TODO: does this work?
	step += start
	next_step = step + 1
	if step >= steps:
		step -= steps
	if next_step >= steps:
		next_step -= steps
	# TODO: find a better way to do this
	astep = 2.0 * math.pi / steps
	# find the angle remainder
	angle_remainder = angle
	while angle_remainder >= astep:
		angle_remainder -= astep
	# for non-adjusted angle, the ratio of progress (a) to a full step (b)
	progress = angle_remainder / astep
	
	# TODO: test this
	# if faci is default, read x/z
	dimlInte = 0
	dimhInte = 2
	dimlStri = "x"
	dimhStri = "z"
	# if faci is not default, read y/z
	if faci == (0.0, 1.0) or faci == (0.0, -1.0):
		dimlInte = 1
		dimlStri = "y"
	if path != []:
		start_x = path[step][dimlInte]
		start_y = path[step][dimhInte]
		end_x = path[next_step][dimlInte]
		end_y = path[next_step][dimhInte]
	else:
		# TODO:
		Sele(charName)
		# TODO: read vari name from a single location
		variName = pathName + "." + Pad_(step)
		start_x = bpy.context.object.properties[variName + "." + dimlStri]
		start_y = bpy.context.object.properties[variName + "." + dimhStri]
		variName = pathName + "." + Pad_(next_step)
		end_x = bpy.context.object.properties[variName + "." + dimlStri]
		end_y = bpy.context.object.properties[variName + "." + dimhStri]

	# draw a vector from start to end
	vect = Math.Vect((start_x, start_y), (end_x, end_y))
	# scale the vector by progress
	vect = Math.VectScal(vect, progress)
	# add to start
	vect = Math.VectAdd_((start_x, start_y), vect)
	return vect
#"""

####################################

# OBJECT / SCENE / VIEWPORT LOOK

def Hori(horizon_color):
	import bpy
	bpy.context.scene.world.horizon_color = horizon_color

def Visi(togg = True, hide = False):
	import bpy
	if togg == True:
		bpy.context.object.hide = not bpy.context.object.hide
		bpy.context.object.hide_render = not bpy.context.object.hide_render
	else:
		bpy.context.object.hide = hide
		bpy.context.object.hide_render = hide

def HideList(hideList):
	import bpy
	for hide in hideList:
		Sele(hide)
		bpy.context.object.hide = True
		bpy.context.object.hide_render = True
		bpy.context.object.hide_select = True

# set smooth shading on all faces
def Shad():
	import bpy
	VertSeleAll_()
	Edit()
	bpy.ops.mesh.faces_shade_smooth()
	Edit()
	VertDese()

# set the clip end in the 3d window
# TODO: is there a way to access clip_end directly
def WindClip(clip):
	import bpy
	brea = False
	a = 0
	while a < len(bpy.context.screen.areas):
		area = bpy.context.screen.areas[a]
		if area.type == 'VIEW_3D':
			b = 0
			while b < len(area.spaces):
				if area.spaces[b].type == 'VIEW_3D':
					area.spaces[0].clip_end = clip
					brea = True
					break
				b += 1
			if brea == True:
				break
		a += 1

# for all grouped materials (cycles engine), set the color of the viewport to the diffuse color of the material
def ViewColo():
	import bpy
	for mate in bpy.data.materials:
		for grou in bpy.data.node_groups:
			for node in grou.nodes:
				set_ = ShadHas_Colo(node.type)
				if set_ == True:
					mate.diffuse_color = (node.inputs[0].default_value[0], node.inputs[0].default_value[1], node.inputs[0].default_value[2])

# for all grouped materials (cycles engine), set the diffuse color of the material to the viewport color
def ViewTo__Colo():
	import bpy
	for mate in bpy.data.materials:
		for grou in bpy.data.node_groups:
			for node in grou.nodes:
				set_ = ShadHas_Colo(node.type)
				if set_ == True:
					node.inputs[0].default_value[0] = mate.diffuse_color[0]
					node.inputs[0].default_value[1] = mate.diffuse_color[1]
					node.inputs[0].default_value[2] = mate.diffuse_color[2]

# set use_shadow on a selected spot light
def SpotShad(use_shadow = False):
	import bpy
	bpy.context.object.data.use_shadow = use_shadow

####################################

# INSTANCE

def Empt(inde = 1):
	import bpy
	bpy.ops.object.empty_add(type = 'PLAIN_AXES', location = (0.0, 0.0, 0.0))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)


def Plan(inde = 1):
	import bpy
	bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Sphe(inde = 1):
	import bpy
	bpy.ops.mesh.primitive_uv_sphere_add(size=1, view_align=False, enter_editmode=False, location = (0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Cube(inde = 1):
	import bpy
	bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Cyli(inde = 1):
	import bpy
	bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Cone(inde = 1):
	import bpy
	bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def VertAdd_(inde = 1):
	Cube()
	VertSeleAll_()
	Edit()
	Merg()
	Edit()
	VertDese()
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Curv(clea = True, inde = 1):
	import bpy
	bpy.ops.curve.primitive_bezier_curve_add(location=(0.0, 0.0, 0.0))
	if clea == True:
		Edit()
		bpy.ops.curve.select_all(action = 'DESELECT')
		bpy.context.object.data.splines[0].bezier_points[1].select_control_point = True
		bpy.ops.curve.delete(type='VERT')
		Edit()
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Circ(inde = 1):
	import bpy
	bpy.ops.curve.primitive_bezier_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Text(text = "", name = "", conv = True, mate = True, inde = 1):
	import bpy
	if text != "":
		bpy.ops.object.text_add(radius=1, view_align=False, enter_editmode=False, location = (0.0, 0.0, 0.0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
		Edit()
		bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
		bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
		bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
		bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
		a = 0
		while a < len(text):
			bpy.ops.font.text_insert(text = str(text[a]))
			a += 1
		Edit()
		if conv == True:
			Conv()
		if mate == True:
			Mate(colo = (1.0, 1.0, 1.0), use_shadeless = True)
		if name != "":
			bpy.context.object.name = name
		vers = bpy.app.version
		if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
			bpy.ops.object.move_to_collection(collection_index = inde)

def Came(inde = 1):
	import bpy
	bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 10.0), rotation=(0.0, 0.0, 0.0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

def Ligh(typ_ = 'POINT', inde = 1):
	import bpy
	bpy.ops.object.lamp_add(type = typ_, view_align=False, location=(0.0, 0.0, 0.0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

# TODO: make work for different facing directions
def VectDraw(vect, orig = (0.0, 0.0, 0.0), cyliScal = (0.4, 0.05, 0.05), coneScal = (0.1, 0.1, 0.1), inde = 1):
	import bpy
	Math = MathLink()
	magn = Math.VectMagn(vect)
	curs = CursRead()
	# draw a cylinder
	Cyli()
	# move the origin to the base
	Curs((0.0, 0.0, -1.0))
	OrigCurs()
	# re-center
	Loca((0.0, 0.0, 0.0))
	# orient to +x
	Rota((0.0, 90.0, 0.0))
	ApplRota()
	# scale
	Scal((cyliScal[0] * magn, cyliScal[1] * magn, cyliScal[2] * magn))
	name = bpy.context.object.name
	# draw a cone
	Cone()
	# move the origin to the base
	Curs((0.0, 0.0, -1.0))
	OrigCurs()
	# orient to +x
	Rota((0.0, 90.0, 0.0))
	ApplRota()
	# scale
	Scal((coneScal[0] * magn, coneScal[1] * magn,coneScal[2] * magn))
	# move the cone to the top of the cylinder
	Loca((cyliScal[0] * 2.0 * magn, 0.0, 0.0))
	# join
	Join(name)
	# reset origin
	Curs((0.0, 0.0, 0.0))
	OrigCurs()
	# rotate
	Rota(Math.VectTo__Eule3d__(Math.VectNorm(vect)))
	# place
	Loca(orig)
	Name("vect")
	# restore cursor location
	Curs(curs)
	vers = bpy.app.version
	if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
		bpy.ops.object.move_to_collection(collection_index = inde)

#############################################

# READ FUNCTIONS

def LocaRead(worl = False):
	import bpy
	Math = MathLink()
	if worl == False:
		retu = tuple(bpy.context.object.location)
	else:
		"""
		pare = bpy.context.object.parent
		bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
		retu = tuple((bpy.context.object.location[0], bpy.context.object.location[1], bpy.context.object.location[2]))
		if pare != None:
			Pare(pare.name)
		"""
		# TODO: scale
		name = bpy.context.object.name
		loca = tuple(bpy.context.object.location)
		pare = bpy.context.object.parent
		while pare != None:
			Sele(pare.name)
			rota = RotaRead()
			rota = Math.VectDegr(rota)
			pareLoca = tuple(pare.location)
			vect = Math.Vect(pareLoca, loca)
			vect = Math.VectRota3d__(vect, rota)
			loca = Math.VectAdd_(vect, pareLoca)
			pare = bpy.context.object.parent
		# TODO
		retu = loca
		Sele(name)
	return retu

def ScalRead():
	import bpy
	return tuple(bpy.context.object.scale)

def RotaRead():
	import bpy
	Math = MathLink()
	retu = tuple(bpy.context.object.rotation_euler)
	return Math.VectDegr(retu)

def TranRead():
	Math = MathLink()
	return ScalRead(), Math.VectDegr(RotaRead()), LocaRead()

# return all children of the selected object
# TODO: preserve hierarchy
def Chil(lis_ = []):
	import bpy
	obje = bpy.context.object
	for chil in obje.children:
		lis_.append(chil.name)
		Sele(chil.name)
		Chil(lis_)
	return lis_

def Vert(inde):
	import bpy
	return tuple(bpy.context.object.data.vertices[inde].co)

# local
def Edge(inde):
	import bpy
	ver1 = bpy.context.object.data.edges[inde].key[0]
	ver2 = bpy.context.object.data.edges[inde].key[1]
	x = bpy.context.object.data.vertices[ver1].co.x + bpy.context.object.data.vertices[ver2].co.x
	x /= 2.0
	y = bpy.context.object.data.vertices[ver1].co.y + bpy.context.object.data.vertices[ver2].co.y
	y /= 2.0
	z = bpy.context.object.data.vertices[ver1].co.z + bpy.context.object.data.vertices[ver2].co.z
	z /= 2.0
	return (x, y, z)

def PolyVert(inde):
	import bpy
	retu = []
	poly = bpy.context.object.data.polygons[inde]
	a = 0
	while a < len(poly.vertices):
		vert = poly.vertices[a]
		retu.append(vert)
		a += 1
	return retu

def PolyEdge(inde):
	import bpy
	retu = []
	poly = bpy.context.object.data.polygons[inde]
	a = 0
	while a < len(poly.edge_keys):
		edge = poly.edge_keys[a]
		retu.append(edge)
		a += 1
	return retu

def PolyAttr(attr = ""):
	import bpy
	retu = []
	a = 0
	while a < len(bpy.context.object.data.polygons):
		valu = getattr(bpy.context.object.data.polygons[a], attr)
		retu.append(tuple(valu))
		a += 1
	return retu

#CentList = functools.partial(PolyAttr, attr = "center")
#NormList = functools.partial(PolyAttr, attr = "normal")

def CentList():
	import bpy
	retu = []
	a = 0
	while a < len(bpy.context.object.data.polygons):
		retu.append(PolyCent(a))
		a += 1
	return retu

def PolyCent(inde):
	import bpy
	return tuple(bpy.context.object.data.polygons[inde].center)

def NormList():
	import bpy
	retu = []
	a = 0
	while a < len(bpy.context.object.data.polygons):
		# TODO
		#retu.append(PolyNorm[a])
		retu.append(PolyNorm(a))
		a += 1
	return retu

def PolyNorm(inde):
	import bpy
	return tuple(bpy.context.object.data.polygons[inde].normal)

def Dist(obj1, obj2):
	import bpy
	Math = MathLink()
	cont = bpy.context.object.name
	if type(obj1) == str:
		Sele(obj1)
		obj1 = LocaRead()
	if type(obj2) == str:
		Sele(obj2)
		obj1 = LocaRead()
	Sele(cont)
	return Math.Dist(obj1, obj2)

# greatest x, y, or z location of an object
def Xyz_Most(axis = 2, reverse = True, inde = False):
	import bpy
	Pyth = PythLink()
	vert = VertList()
	if inde:
		for a in range(len(vert)):
			vert[a] = [vert[a][0], vert[a][1], vert[a][2]]
			vert[a].append(a)
	vert = Pyth.SortDime(vert, axis, reverse = reverse)
	retu = vert[0][axis]
	if inde:
		retu = vert[0]
	return retu

# greatest x, y, or z location of a polygon
def Xyz_MostPoly(axis = 2, poly = 0, reverse = True):
	import bpy
	Pyth = PythLink()
	vert = PolyVert(poly)
	vert = VertLoca(vert)
	vert = Pyth.SortDime(vert, axis, reverse = reverse)
	return vert[0][axis]

# TODO: return the highest matching z
def Z_xy(loca, tria = True):
	import bpy
	import math
	Pyth = PythLink()
	Math = MathLink()
	retu = None
	name = bpy.context.object.name
	scal, rota, loc1 = TranRead()
	tole = 0.001
	if tria == True:
		Tria()
	# find the face that contains the (x, y) position and get the vertices
	a = 0
	while a < len(bpy.context.object.data.polygons):
		# TODO: this is a downward raycast. create an outline of the object, and check if the raycast falls within the outline, then recursively subdivide
		vectList = []
		b = 0
		while b < len(bpy.context.object.data.polygons[a].vertices):
			# get the vert
			vert = bpy.context.object.data.vertices[bpy.context.object.data.polygons[a].vertices[b]]
			# get the world location of the vert
			loc2 = Math.Tran3d__((vert.co.x, vert.co.y, vert.co.z), scal, rota, loc1)
			# get the x/y vector from the sources position to the vertex positions
			vect = Math.Vect((loca[0], loca[1], 0.0), (loc2[0], loc2[1], 0.0))
			# get the angle of the vector relative to +x
			angl = math.atan2(vect[1], vect[0])
			if angl < 0.0:
				angl += 2.0 * math.pi
			# add the vector and the vectors angle to a lists
			vectList.append((angl, vect))
			b += 1
		# sort the list 
		vectList = sorted(vectList)
		# total angle between all angles in the list created above
		angl = 0.0
		# add the angles from one vector to another
		b = 0
		while b < len(vectList) - 1:
			angl += Math.VectAngl(vectList[b][1], vectList[b + 1][1])
			b += 1
		# add the final angle from the last vector to the first vector
		angl += Math.VectAngl(vectList[b][1], vectList[0][1])
		# check if the total angle is equal to a circle
		if math.fabs(360.0 - angl) <= tole:
			break
		a += 1
	if a < len(bpy.context.object.data.polygons):
		x = loca[0]
		y = loca[1]
		# find the highest point of the polygon for the origin start of a raycast to the polygon face
		z = Xyz_MostPoly(axis = 2, poly = a)
		x, y, z = Math.Tran3d__((x, y, z), scal, rota, loc1)
		poin = Math.VectAdd_(bpy.context.object.location, bpy.context.object.data.polygons[a].center)
		poin = Math.Tran3d__(poin, scal, rota, loc1)
		norm = bpy.context.object.data.polygons[a].normal
		dist = Math.DistTo__Inte((x, y, z), (0.0, 0.0, -1.0), poin, norm)
		Sele(name)
		retu = z - dist
	else:
		retu = "could not find z"
	return retu

# get the path the path marker is sitting on
# triangulates scene objects
def ObjeOver(loca):
	retu = []
	for obje in Scene().objects:
		Sele(obje.name)
		if obje.type == 'MESH':
			# TODO: where else should this check be implemented
			if obje.layers[Laye() - 1]:
				# TODO: slow
				z = Z_xy(loca)
				if type(z) == float and z <= loca[2]:
					retu = [z, obje.name]
					break
	return retu

# if two vertices are selected, the lowest index will be returned
def VertSeleRead():
	import bpy
	if bpy.context.object.mode == 'EDIT':
		Edit()
	a = 0
	while a < len(bpy.context.object.data.vertices):
		if bpy.context.object.data.vertices[a].select == True:
			break
		a += 1
	if a >= len(bpy.context.object.data.vertices):
		a = -1
	return a

# if two edges are selected, the lowest index will be returned
def EdgeSeleRead():
	import bpy
	if bpy.context.object.mode == 'EDIT':
		Edit()
	a = 0
	while a < len(bpy.context.object.data.edges):
		if bpy.context.object.data.edges[a].select == True:
			break
		a += 1
	if a >= len(bpy.context.object.data.edges):
		a = -1
	return a

# if two polygons are selected, the lowest index will be returned
def PolySeleRead():
	import bpy
	if bpy.context.object.mode == 'EDIT':
		Edit()
	a = 0
	while a < len(bpy.context.object.data.polygons):
		if bpy.context.object.data.polygons[a].select == True:
			break
		a += 1
	if a >= len(bpy.context.object.data.polygons):
		a = -1
	return a

"""
	vertList = VertListSele()
	for a in range(len(bpy.context.object.data.polygons)):
		vert = bpy.context.object.data.polygons[a].vertices
		if len(vertList) == len(vert):
			same = True
			for b in range(len(vertList)):
				exis = False
				for c in range(len(vert)):
					if vertList[b] == vert[c]:
						exis = True
						break
				if exis == False:
					same = False
					break
			if same == True:
				print(a)
				break
"""

# return an index list of selected vertices
def VertListSele(meth = 0):
	import bpy
	retu = []
	# TODO: where else can this be used
	if meth == 0:
		try:
			import numpy
			leng = len(bpy.context.object.data.vertices)
			sele = numpy.zeros(leng, dtype = bool)
			bpy.context.object.data.vertices.foreach_get('select', sele)
			rang = numpy.arange(leng, dtype = int)
			retu = rang[sele]
			retu = list(retu)
			for a in range(len(retu)):
				retu[a] = int(retu[a])
		except:
			meth = 1
	if meth == 1:
		retu = list(filter(lambda vert: vert.select, bpy.context.object.data.vertices))
		for a in range(len(retu)):
			retu[a] = retu[a].index
	if meth == 2:
		a = 0
		while a < len(bpy.context.object.data.vertices):
			if bpy.context.object.data.vertices[a].select == True:
				retu.append(a)
			a += 1
	
	return retu

# get a list of all vertices connected to INDEX (slow)
def VertConn(inde):
	import bpy
	retu = []
	if inde != -1:
		"""
		for edge in bpy.context.object.data.edges:
			if edge.key[0] == inde or edge.key[1] == inde:
				if edge.key[0] == inde:
					retu.append(edge.key[1])
				if edge.key[1] == inde:
					retu.append(edge.key[0])
		"""
		# backup selection
		sele = VertListSele()
		VertSele([inde])
		Edit()
		bpy.ops.mesh.select_more(use_face_step = False)
		Edit()
		retu = VertListSele()
		retu.remove(inde)
		# restore selection
		VertSele(sele)
	return retu

def Prin():
	import bpy
	for obje in bpy.context.scene.objects:
		sele = False
		vers = bpy.app.version
		if vers[0] >= 3 or (vers[0] == 2 and vers[1] >= 80):
			if obje.select_get() == True:
				sele = True
		else:
			if obje.select == True:
				sele = True
		if sele == True:
			print(obje.name)

def PrinVert():
	import bpy
	for a in range(len(bpy.context.object.data.vertices)):
		if bpy.context.object.data.vertices[a].select == True:
			print(a)

def PrinEdge():
	import bpy
	for a in range(len(bpy.context.object.data.edges)):
		if bpy.context.object.data.edges[a].select == True:
			print(a)

def PrinPoly():
	import bpy
	for a in range(len(bpy.context.object.data.polygons)):
		if bpy.context.object.data.polygons[a].select == True:
			print(a)

#########################################

# CONVERSIONS

# read a VERT INDEX LIST and return a vert location list
def VertLoca(vertList):
	retu = []
	for vert in vertList:
		retu.append(Vert(vert))
	return retu

# rebuild an edge list to hold locations rather than indices
def EdgeLoca(vert, edge):
	retu = []
	a = 0
	while a < len(edge):
		retu.append((vert[edge[a][0]], vert[edge[a][1]]))
		a += 1
	return retu

# pass a WORLD LOCATION and get back a vertex index for the selected object
# TODO: slow
def VertIndeBy__Loca(loca, exac = True):
	import bpy
	Math = MathLink()
	tole = 0.0001
	lis_ = []
	scal, rota, loc2 = TranRead()
	a = 0
	while a < len(bpy.context.object.data.vertices):
		# get local vertex data
		vert = bpy.context.object.data.vertices[a]
		# append world location
		lis_.append(Math.Tran3d__((vert.co.x, vert.co.y, vert.co.z), scal, rota, loc2))
		a += 1
	# get the clos EST index
	retu, dist = Math.VectClos(loca, lis_)
	# if theyre not exactly the same (and exac is True), return not found
	if exac == True:
		if dist > tole:
			retu = -1
	return retu

# read a local location and return world space
def TranAppl3d__(vect):
	Math = MathLink()
	scal, rota, loca = TranRead()
	return Math.Tran3d__(vect, scal, rota, loca)

# read geomerty for a ray obstructor and optionally convert it to world space
def ObstTran(vert, cent, norm, poly, scal, rota, loca):
	Math = MathLink()
	# convert vertices to world space
	d = 0
	while d < len(vert):
		vert[d] = Math.Tran3d__(vert[d], scal, rota, loca)
		d += 1
	d = 0
	while d < len(cent):
		# convert centers to world space
		cent[d] = Math.Tran3d__(cent[d], scal, rota, loca)
		# convert normals to world space
		norm[d] = Math.VectRota3d__(norm[d], rota)
		d += 1
	return vert, cent, norm, poly

# start: location of the vertex at index 0
def SortBy__Conn(star):
	Math = MathLink()
	name = Object().name
	# download a vertex list
	vertList = VertList()
	# download an edge list
	edgeList = EdgeList()
	# append the first vertex
	vertListNew_ = []
	vertListNew_.append(VertIndeBy__Loca(star))
	# find the vertex that star is connected to
	a = 0
	while a < len(edgeList):
		if len(vertListNew_) == len(vertList):
			break
		if edgeList[a][0] == vertListNew_[len(vertListNew_) - 1] or edgeList[a][1] == vertListNew_[len(vertListNew_) - 1]:
			exis = False
			b = 0
			while b < len(vertListNew_):
				if (edgeList[a][0] == vertListNew_[len(vertListNew_) - 1] and edgeList[a][1] == vertListNew_[b]) or (edgeList[a][1] == vertListNew_[len(vertListNew_) - 1] and edgeList[a][0] == vertListNew_[b]):
					exis = True
					break
				b += 1
			if exis == False:
				if edgeList[a][0] == vertListNew_[len(vertListNew_) - 1]:
					vertListNew_.append(edgeList[a][1])
				else:
					vertListNew_.append(edgeList[a][0])
				a = -1
		a += 1
	# build new vertex list
	uplo = []
	a = 0
	while a < len(vertListNew_):
		uplo.append(vertList[vertListNew_[a]])
		a += 1
	# build new edge list
	edgeList = Math.EdgeLine(len(uplo))
	# replace the old mesh object with a new one of the same name
	Dele()
	Uplo([uplo, edgeList, []], name = name)

#################################################

# NAMING

# set the NAME of the selected object
def Name(name):
	import bpy
	bpy.context.object.name = name

# pass an INTEGER and return a string with a width of 3 (usually)
def Pad_(numb):
	retu = ""
	if numb >= 1000:
		thou = int(numb) / 1000
	if numb < 100:
		retu += "0"
	if numb < 10:
		retu += "0"
	retu += str(numb)
	if numb >= 1000:
		retu = str(thou) + retu
	return retu

# retrieve a number from a string and return an int
def Inst(stri):
	stri = stri.split(".")
	for elem in stri:
		if elem.isnumeric():
			stri = int(elem)
			break
	if type(stri) == list:
		stri = 0
	return stri

# replace the instance in a string
def InstRepl(stri, indeStri):
	stri = stri.split(".")
	if len(stri) > 0:
		if len(stri) > 1:
			retu = ""
			a = 0
			while a < len(stri):
				if stri[a].isnumeric():
					retu += indeStri
				else:
					retu += stri[a]
				if a < len(stri) - 1:
					retu += "."
				a += 1
		else:
			retu = stri[0] + "." + indeStri
	return retu

# for all objects in a scene, split by "." and replace each instance of string FIND with string REPLACE
def FindRepl(find, repl):
	import bpy
	for obje in bpy.context.scene.objects:
		name = obje.name.split(".")
		nameNew_ = ""
		a = 0
		while a < len(name):
			if name[a] == find:
				nameNew_ += repl
			else:
				nameNew_ += name[a]
			if a < len(name) - 1:
				nameNew_ += "."
			a += 1
		obje.name = nameNew_

def ScenName(scenName = "Scene"):
	import bpy
	bpy.context.scene.name = scenName

#############################################

# SCENE

def ScenNew_():
	import bpy
	bpy.ops.scene.new()

def ScenSet_(scenName):
	import bpy
	bpy.context.screen.scene = bpy.data.scenes[scenName]

def DeleCube():
	import bpy
	Sele('Cube')
	bpy.ops.object.delete()

def DeleLamp():
	import bpy
	Sele('Lamp')
	bpy.ops.object.delete()

def DeleCame():
	import bpy
	Sele('Camera')
	bpy.ops.object.delete()

def DeleDefa(came = False):
	DeleCube()
	DeleLamp()
	if came == True:
		DeleCame()

# returns 1 for Scene().layers[0]. subtract 1 to use as an index
def Laye():
	a = 0
	while a < 20:
		if Scene().layers[a]:
			break
		a += 1
	return a + 1

#################################################

# CONTEXT

def Scene():
	import bpy
	return bpy.context.scene

def Object():
	import bpy
	return bpy.context.object

def Objects():
	import bpy
	return bpy.context.scene.objects

def Vertices():
	import bpy
	return bpy.context.object.data.vertices

def Edges():
	import bpy
	return bpy.context.object.data.edges

def Polygons():
	import bpy
	return bpy.context.object.data.polygons

#################################################

# DOWNLOAD / UPLOAD OBJECTS

def VertList():
	import bpy
	retu = []
	a = 0
	while a < len(bpy.context.object.data.vertices):
		vert = bpy.context.object.data.vertices[a]
		retu.append((vert.co.x, vert.co.y, vert.co.z))
		a += 1
	return retu

def EdgeList():
	import bpy
	retu = []
	a = 0
	while a < len(bpy.context.object.data.edges):
		edge = bpy.context.object.data.edges[a]
		retu.append((edge.key[0], edge.key[1]))
		a += 1
	return retu

# TODO: this should be called polyvertlist or something
def PolyList():
	import bpy
	retu = []
	a = 0
	while a < len(bpy.context.object.data.polygons):
		retu.append(PolyVert(a))
		a += 1
	# TODO: update
	#return tuple(retu)
	return retu

def Down():
	return [VertList(), EdgeList(), PolyList()]

# upload an object from a list
# LIST is a list of lists.
# first list is a vertex list (a list of 3d locations)
# second list a an edge list (a list of integer pairs that connect two vertices by their index)
# third is a poly list (a list of vertices that make up each poly. the vertex index list must be in a specific order for the poly to orient properly)
# only the vertex list is strictly required
# edges and faces can be added after the object is uploaded
def Uplo(lis_, orig = (0.0, 0.0, 0.0), name = "obje"):
	import bpy
	bpy.ops.object.add(location = (orig[0], orig[1], orig[2]), type = 'MESH')
	bpy.context.object.name = name
	bpy.context.object.data.from_pydata(lis_[0], lis_[1], lis_[2])
	bpy.context.object.data.validate()

# validate all mesh objects
def Vali():
	for obje in bpy.context.scene.objects:
		if obje.type == 'MESH':
			print(obje.data.validate(), obje.name)

#########################################

# APPEND

def Impo(blenFile = "", pref = "", rena = "", ligh = False, came = False, empt = True, scal = (1.0, 1.0, 1.0), posi = False, posz = False, rota = False, pivo = "", skip = True, repl = False):
	import os
	Pyth = PythLink()
	Head = HeadLink()
	blenComm = BlenCommLink()

	dire, blenName = FilePath(blenFile)

	# write options to a file
	writ = {}
	writ.update({"blenName":blenName})
	writ.update({"dire":dire})
	writ.update({"ligh":ligh})
	writ.update({"came":came})
	writ.update({"empt":empt})

	# TODO: update
	# TODO: tempscri needs to know where to find the variables
	#Pyth.LineTo__File(Pyth.DictTo__Line(writ), "list" + os.sep + "expo")
	Pyth.LineTo__File(Pyth.DictTo__Line(writ), "list" + os.sep + blenName)

	expr = ""
	expr += blenComm + " -b " + dire + blenName + ".blend"	
	expr += " --python tempScri.py"

	scri = Head()
	scri += "def main():\n"
	#scri += "\tline = Pyth.FileTo__Line(\"list" + os.sep + "expo\")\n"
	scri += "\tline = Pyth.FileTo__Line(\"list" + os.sep + blenName + "\")\n"
	scri += "\tline = Pyth.LineTo__Dict(line)\n"
	scri += "\tBlen.Expo(listName = line[\"blenName\"], ligh = line[\"ligh\"], came = line[\"came\"], empt = line[\"empt\"])\n"
	scri += "main()\n"

	fileObje = open("tempScri.py", mode = "w")
	fileObje.write(scri)
	fileObje.close()

	# execute
	os.system(expr)

	objeList = ""
	# read the list and import the objects
	objeList = ReadList(name = blenName)
	ImpoBlen(blenName = blenName, dire = dire, objeList = objeList, posi = posi, posz = posz, rota = rota, pivo = pivo, scal = scal, pref = pref, rena = rena, skip = skip, repl = repl)
	return objeList

def Expo(listName = "", ligh = False, came = False, empt = False):
	import bpy
	import os
	Pyth = PythLink()
	scen = bpy.context.scene
	writ = []
	writ.append([])
	writ.append([])
	writ.append([])
	# write a number that tells whether object is root, 1 from root, or 2 and more
	for obje in scen.objects:
		if obje.type != 'NoneType':
			hs = obje.hide_select
			if hs == False:
				writObje = True
				pare = "None"
				hier = 0
				if obje.name == "":
					writObje = False
				if obje.type == 'CAMERA' and came == False:
					writObje = False
				if obje.type == 'LAMP' and ligh == False:
					writObje = False
				if obje.type == 'EMPTY' and empt == False:
					writObje = False
				if obje.parent != None:
					pare = obje.parent.name
					if obje.parent.parent == None:
						hier = 1
					else:
						hier = 2
				if writObje == True:
					writ[hier].append([obje.name, pare, hier])
	a = 0
	while a < len(writ):
		# sort
		writ[a] = sorted(writ[a])
		writ[a] = Pyth.SortDime(writ[a], 1)
		# make writable
		b = 0
		while b < len(writ[a]):
			writ[a][b] = Pyth.ListTo__Stri(writ[a][b])
			b += 1
		a += 1
	# make writable
	writOut_ = []
	a = 0
	while a < len(writ):
		b = 0
		while b < len(writ[a]):
			writOut_.append(writ[a][b])
			b += 1
		a += 1
	Pyth.LineTo__File(writOut_, "list" + os.sep + listName)

def ReadList(name = ""):
	import os
	Pyth = PythLink()
	retu = []
	if name != "":
		object_list = Pyth.FileTo__Line("list" + os.sep + name)
		a = 0
		while a < len(object_list):
			object_list[a] = object_list[a].split(",")
			b = 0
			while b < len(object_list[a]):
				object_list[a][b] = object_list[a][b].strip()
				b += 1
			a += 1
		a = 0
		while a < len(object_list):
			retu.append({'name':object_list[a][0]})
			a += 1
	return retu

# blenName: file name without .blend
# dire: directory of the blend file
# objeList: a list a dictionaries with the key 'name' and value of the object name
# posi: True to position the object on an empty with the same name + '.impo'
# posz: True to change to z position on import (if posi is True)
# rota: rotate the object according to the rotation of the import object (z only)
# pivo: pivot the rotation around the import object (if rota is True)
# scal: scale the object
# pref: add a string to the beginning of the objects name
# rena: move the instance number after the name (char.002.head instead of char.head.002)
def ImpoBlen(blenName = "", dire = "", objeList = [], posi = False, posz = False, rota = False, pivo = "", scal = (1.0, 1.0, 1.0), pref = "", rena = "", skip = True, repl = False):
	import os
	import bpy
	import math
	bpy.ops.wm.append(directory = dire + blenName + ".blend" + os.sep + "Object", files = objeList, link = False)
	a = 0
	while a < len(objeList):
		Sele(objeList[a]["name"])
		obje = bpy.context.object
		if posi == True:
			x = bpy.data.objects[obje.name + ".impo"].location[0]
			y = bpy.data.objects[obje.name + ".impo"].location[1]
			z = 0.0
			if posz == True:
				z = bpy.data.objects[obje.name + ".impo"].location[2]
			bpy.context.object.location = (obje.location[0] + x, obje.location[1] + y, obje.location[2] + z)
		if rota == True:
			if pivo == "CURSOR":
				bpy.context.scene.cursor_location = bpy.data.objects[obje.name + ".impo"].location
			Rota(rota = (math.degrees(bpy.data.objects[obje.name + ".impo"].rotation_euler[0]), math.degrees(bpy.data.objects[obje.name + ".impo"].rotation_euler[1]), math.degrees(bpy.data.objects[obje.name + ".impo"].rotation_euler[2])), pivo = pivo)
		if scal != (1.0, 1.0, 1.0):
			Scal(scal)
			obje.location = (obje.location[0] * scal[0], obje.location[1] * scal[1], obje.location[2] * scal[2])
		if pref != "":
			obje.name = pref + "." + obje.name
		a += 1
	if rena != "":
		Rena(objeName = objeList[0]["name"], objeList = objeList, rena = rena, skip = skip, repl = repl)

# move the instance string (eg "001") after the object's name rather than the end
# (eg enemy.shoulder.001 becomes enemy.001.shoulder)
def Rena(objeName = "", objeList = [], rena = "", skip = True, repl = False):
	import bpy
	a = 0
	while a < len(objeList):
		name = objeList[a]["name"]
		if name != "":
			Sele(name)
			name = name.split(".")
			if len(name) > 0:
				if len(name) > 1:
					if rena != "":
						stri = ""
						b = 0
						while b < len(name):
							if stri != "":
								stri += "."
							if name[b] != objeName or skip == False:
								if name[b] != rena or repl == True:
									stri += name[b]
							else:
								stri += name[b] + "." + rena
							b += 1
						bpy.context.object.name = stri
				else:
					bpy.context.object.name = bpy.context.object.name + "." + rena
		a += 1

def TextAppe(name = "", filePath = ""):
	import bpy
	import os
	exte = filepath.split(".")
	if exte[len(exte) - 1] != blend:
		filePath += ".blend"
	bpy.ops.wm.append(directory = filePath + os.sep + "Texture", files = [{"name":name}], link = False, autoselect = True, active_layer = True, instance_groups = False)

####################################

# COMMAND LINE / SCRIPTING

# form a string to pass to a console
# run os.system(command) to execute the command
def Batc(blen = "", batc = True):
	blenComm = BlenCommLink()
	stri = blenComm + " "
	if batc == True:
		stri += "-b "
	stri += blen
	blen = blen.split(".")
	if len(blen) > 1:
		if blen[len(blen) - 1] != "blend":
			stri += ".blend"
	return stri

# instruct blender to render an image and save it to disk
def Rend(imag):
	retu = " -o"
	retu += " " + imag
	retu += " -f"
	retu += " 1"
	return retu

def RendVide(vide, end_):
	retu = " -o"
	retu += " " + vide
	retu += " -F AVIJPEG"
	# TODO
	#retu += " -a [1," + str(end_) + "]"
	retu += " -a"
	return retu

# TODO: see if a python expression can still be constructed in windows by adding a quote at the beginning and end
def Expr(star = True):
	stri = ""
	if star == True:
		stri = " --python-expr \""
	else:
		stri = "\""
	return stri

# receive a the filepath of a blend file, and return the folder and filename
def FilePath(filepath):
	import os
	blenName = filepath
	blenName = blenName.split(os.sep)
	dire = ""
	a = 0
	while a < len(blenName) - 1:
		dire += blenName[a] + os.sep
		a += 1
	if len(blenName) > 0:
		blenName = blenName[len(blenName) - 1]
	blenName = blenName.split(".")
	if len(blenName) > 0:
		# TODO: test
		name = ""
		for a in range(len(blenName) - 1):
			name += blenName[a]
			if a < len(blenName) - 2:
				name += "."
		blenName = name
	else:
		blenName = ""
	return dire, blenName

#############################################

# CYCLES TEXTURE RANDOMIZATION

# TODO: move to gene?

def NodeRand(node_group = 'NodeGroup', node = None, nudg = 0.0):
	import random
	keys = []
	mima = []
	if node.type == 'BRIGHTCONTRAST':
		# (bright, contrast) # not using 0 - color
		keys = [node.inputs[1].default_value, node.inputs[2].default_value]
		if nudg == 0.0:
			mima = [ [[-5.0, 5.0]], [[-5.0, 5.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'BSDF_DIFFUSE':
		# (roughness) # not using 0 - color
		keys = [node.inputs[1].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 1.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'BSDF_TRANSPARENT':
		# (color)
		keys = [node.inputs[0].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'EMISSION':
		# (color, strength)
		keys = [node.inputs[0].default_value, node.inputs[1].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]], [[0.0, 2.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'HUE_SAT':
		# (h, s, v, factor)
		keys = [node.inputs[0].default_value, node.inputs[1].default_value, node.inputs[2].default_value, node.inputs[3].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 1.0]], [[0.0, 1.0]], [[0.0, 1.0]], [[0.0, 1.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'INVERT':
		# (factor) # not using 1 - color
		keys = [node.inputs[0].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 1.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'MAPPING':
		# not using: use min/max, vector_type
		keys = [node.translation, node.rotation, node.scale]
		if nudg == 0.0:
			mima = [ [[-10.0, 10.0], [-10.0, 10.0], [-10.0, 10.0]], [[0.0, 6.283185307179586], [0.0, 6.283185307179586], [0.0, 6.283185307179586]], [[-10.0, 10.0], [-10.0, 10.0], [-10.0, 10.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'MIX_RGB':
		# (factor), color1, (color2)
		keys = [node.blend_type, node.inputs[0].default_value, node.inputs[2].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 17.0]], [[0.0, 1.0]], [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'MIX_SHADER':
		# (factor), shader1, shader2
		keys = [node.inputs[0].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 1.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'TEX_NOISE':
		# vector, (scale, detail, distortion)
		keys = [node.inputs[1].default_value, node.inputs[2].default_value, node.inputs[3].default_value]
		if nudg == 0.0:
			mima = [ [[-10.0, 10.0]], [[-10.0, 10.0]], [[-10.0, 10.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	if node.type == 'TEX_WAVE':
		# (wt, wp) vector (scale, distortion, detail, detail_scale)
		keys = [node.wave_type, node.wave_profile, node.inputs[1].default_value, node.inputs[2].default_value, node.inputs[3].default_value, node.inputs[4].default_value]
		if nudg == 0.0:
			mima = [ [[0.0, 1.0]], [[0.0, 1.0]], [[-10.0, 10.0]], [[-10.0, 10.0]], [[-10.0, 10.0]], [[-10.0, 10.0]] ]
		else:
			mima = NodeRandList(keys, nudg)
	a = 0
	while a < len(mima):
		inpu = mima[a]
		b = 0
		while b < len(inpu):
			mm = inpu[b]
			random.seed()
			text = mm[0] + (mm[1] - mm[0]) * random.random()
			if str(type(keys[a])) == '<class \'bpy_prop_array\'>' or str(type(keys[a])) == '<class \'Vector\'>' or str(type(keys[a])) == '<class \'Euler\'>':
				keys[a][b] = text
			else:
				keys[a] = text
			b += 1
		a += 1
	if len(mima) > 0:
		if node.type == 'BRIGHTCONTRAST':
			node.inputs[1].default_value = keys[0]
			node.inputs[2].default_value = keys[1]
		if node.type == 'BSDF_DIFFUSE':
			node.inputs[1].default_value = keys[0]
		if node.type == 'BSDF_TRANSPARENT':
			node.inputs[0].default_value = (keys[0][0], keys[0][1], keys[0][2], 1.0)
		if node.type == 'EMISSION':
			node.inputs[0].default_value = (keys[0][0], keys[0][1], keys[0][2], 1.0)
			node.inputs[1].default_value = keys[1]
		if node.type == 'HUE_SAT':
			node.inputs[0].default_value = keys[0]
			node.inputs[1].default_value = keys[1]
			node.inputs[2].default_value = keys[2]
			node.inputs[3].default_value = keys[3]
		if node.type == 'INVERT':
			node.inputs[0].default_value = keys[0]
		if node.type == 'MAPPING':
			node.translation = (keys[0][0], keys[0][1], keys[0][2])
			node.rotation = (keys[1][0], keys[1][1], keys[1][2])
			node.scale = (keys[2][0], keys[2][1], keys[2][2])
		if node.type == 'MIX_RGB':
			if type(keys[0]) == float:
				keys[0] = round(keys[0])
			if keys[0] == 0:
				node.blend_type = 'LINEAR_LIGHT'
			if keys[0] == 1:
				node.blend_type = 'SOFT_LIGHT'
			if keys[0] == 2:
				node.blend_type = 'COLOR'
			if keys[0] == 3:
				node.blend_type = 'VALUE'
			if keys[0] == 4:
				node.blend_type = 'SATURATION'
			if keys[0] == 5:
				node.blend_type = 'HUE'
			if keys[0] == 6:
				node.blend_type = 'BURN'
			if keys[0] == 7:
				node.blend_type = 'DODGE'
			if keys[0] == 8:
				node.blend_type = 'OVERLAY'
			if keys[0] == 9:
				node.blend_type = 'LIGHTEN'
			if keys[0] == 10:
				node.blend_type = 'DARKEN'
			if keys[0] == 11:
				node.blend_type = 'DIFFERENCE'
			if keys[0] == 12:
				node.blend_type = 'DIVIDE'
			if keys[0] == 13:
				node.blend_type = 'SCREEN'
			if keys[0] == 14:
				node.blend_type = 'SUBTRACT'
			if keys[0] == 15:
				node.blend_type = 'MULTIPLY'
			if keys[0] == 16:
				node.blend_type = 'ADD'
			if keys[0] == 17:
				node.blend_type = 'MIX'
			node.inputs[0].default_value = keys[1]
			node.inputs[2].default_value = (keys[2][0], keys[2][1], keys[2][2], 1.0)
		if node.type == 'MIX_SHADER':
			node.inputs[0].default_value = keys[0]
		if node.type == 'TEX_NOISE':
			node.inputs[1].default_value = keys[0]
			node.inputs[2].default_value = keys[1]
			node.inputs[3].default_value = keys[2]
		if node.type == 'TEX_WAVE':
			if type(keys[0]) == str:
				if keys[0] == 'RINGS':
					node.wave_type = 'RINGS'
				elif keys[0] == 'BANDS':
					node.wave_type = 'BANDS'
			if type(keys[0]) == float:
				if keys[0] < 0.5:
					node.wave_type = 'RINGS'
				else:
					node.wave_type = 'BANDS'
			if type(keys[0]) == str:
				if keys[1] == 'SAW':
					node.wave_profile = 'SAW'
				elif keys[1] == 'SIN':
					node.wave_profile = 'SIN'
			if type(keys[0]) == float:
				if keys[1] < 0.5:
					node.wave_profile = 'SAW'
				else:
					node.wave_profile = 'SIN'
			node.inputs[1].default_value = keys[2]
			node.inputs[2].default_value = keys[3]
			node.inputs[3].default_value = keys[4]
			node.inputs[4].default_value = keys[5]

def NodeRandList(keys, nudg):
	mima = []
	for a in range(len(keys)):
		lis_ = []
		if str(type(keys[a])) == '<class \'bpy_prop_array\'>' or str(type(keys[a])) == '<class \'Vector\'>' or str(type(keys[a])) == '<class \'Euler\'>':
			for b in range(len(keys[a])):
				lis_.append([keys[a][b] - nudg / 2.0, keys[a][b] + nudg / 2.0])
		else:
			if type(keys[a]) != str:
				lis_.append([keys[a] - nudg / 2.0, keys[a] + nudg / 2.0])
		mima.append(lis_)
	return mima
