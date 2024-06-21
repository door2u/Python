
#import functools

def PythLink(Pyth = None):
	return Pyth
def MathLink(Math = None):
	return Math
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
	if dese == True:
		bpy.ops.object.select_all(action='DESELECT')
	scen.objects.active = scen.objects[name]
	scen.objects[name].select = True
	return scen.objects[name]

# select an object by NAME from another scene by NAME
def SeleOthe(objeName, scenName):
	import bpy
	scen = bpy.context.scene
	for obje in scen.objects:
		obje.select = False
	scen = bpy.data.scenes[scenName]	
	# deselect all
	for obje in scen.objects:
		obje.select = False
	# select object
	scene.objects.active = scene.objects[objeName]
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
	bpy.data.objects[chil].select = True
	bpy.ops.object.parent_set(type = 'OBJECT', xmirror = False, keep_transform = True)
	Sele(chil)

def PareClea():
	import bpy
	bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

# select the first object, then call join, and pass the NAME of the second object. joined object inherits the name of the first object
def Join(name):
	import bpy
	bpy.data.objects[name].select = True
	bpy.ops.object.join()

# duplicate the selected object
def Dupl():
	import bpy
	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})

# delete the selected object
def Dele():
	import bpy
	bpy.ops.object.delete()

#################################################

# TRANSFORMS

# scale selected object by SCAL
def Scal(scal, proportional_size = 1.0):
	import bpy
	bpy.ops.transform.resize(value=(scal[0], scal[1], scal[2]), constraint_axis=(scal[0] != 1.0, scal[1] != 1.0, scal[2] != 1.0), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size = proportional_size)

# rotate the selected object by ROTA. set loca to TRUE for a local rotation. set PIVOT to CURSOR to translate the object around the z-axis of the cursor
def Rota(rota = (0.0, 0.0, 0.0), loca = False, pivo = ""):
	import bpy
	import math
	cons = 'GLOBAL'
	if loca == True:
		cons = 'LOCAL'
	bpy.ops.transform.rotate(value = math.radians(rota[0]), axis=(1, 0, 0), constraint_axis = (True, False, False), constraint_orientation = cons)
	bpy.ops.transform.rotate(value = math.radians(rota[1]), axis=(0, 1, 0), constraint_axis = (False, True, False), constraint_orientation = cons)
	bpy.ops.transform.rotate(value = math.radians(rota[2]), axis=(0, 0, 1), constraint_axis = (False, False, True), constraint_orientation = cons)
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
def Move(vect):
	import bpy
	bpy.ops.transform.translate(value = vect, constraint_axis=(False, False, False), constraint_orientation='LOCAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

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
	bpy.context.scene.cursor_location = loca

def CursRead():
	import bpy
	return tuple(bpy.context.scene.cursor_location)

# cursor to selected
def CursTo__Sele(all_ = False):
	import bpy
	Math = MathLink()
	if all_ == False:
		x, y, z = LocaRead()
	else:
		aver = []
		for obje in bpy.context.scene.objects:
			if obje.select == True:
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
def VertSele(vert):
	import bpy
	# backup current context
	name = bpy.context.object.name
	# create a new vertex group and add the vertices in the passed list to the new group
	VertGrou("temp", vert)
	# reselect the object
	Sele(name)
	# deselect all verts
	VertDese()
	# select the group created above
	VertGrouSele("temp")
	# delete the group
	bpy.ops.object.vertex_group_remove()

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
def PolySele(inde):
	import bpy
	VertSele(PolyVert(inde))

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

def VertGrou(name, lis_, weig = 1.0):
	import bpy
	bpy.ops.object.vertex_group_add()
	bpy.context.object.vertex_groups[len(bpy.context.object.vertex_groups) - 1].name = name
	bpy.context.object.vertex_groups[name].add(lis_, weig, type='ADD')

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

def Extr():
	import bpy
	Edit()
	bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0.0, 0.0, 0.0), "constraint_axis":(False, False, False), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":39.7397, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
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
def VertDoub():
	import bpy
	VertSeleAll_()
	Edit()
	bpy.ops.mesh.remove_doubles()
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

def VertTran(tran):
	import bpy
	Edit()
	bpy.ops.transform.translate(value=(tran[0], tran[1], tran[2]), constraint_axis=(tran[0] != 0.0, tran[1] != 0.0, tran[2] != 0.0), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=39.7397, release_confirm=True)
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
		Uplo(uplo[a], name = "poly" + "." + Pad_(a))
		Tran(scal, rota, loca)
	Sele(name)
	Dele()

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
			bpy.context.object.active_material.texture_slots[len(bpy.context.object.active_material.texture_slots) - 1].texture_coords = 'ORCO'

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

def CharLeftTo__Righ(name = "", lis_ = [[".shoulder.l", ".body"], [".hip.l", ".body"]], faci = (1.0, 0.0), exceList = [], axle = True, axleList = ["axle.arms", "axle.legs"], dele = True):
	import bpy
	if lis_ == [[".shoulder.l", ".body"], [".hip.l", ".body"]]:
		for a in range(len(lis_)):
			for b in range(len(lis_[a])):
				lis_[a][b] = name + lis_[a][b]
	if dele == True:
		deleList = [name + ".axle.arms.r", name + ".axle.legs.r", name + ".shoulder.r", name + ".elbow.r", name + ".wrist.r", name + ".hand.r", name + ".hip.r", name + ".knee.r", name + ".ankle.r", name + ".foot.r"]
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

# ANIMATION FUNCTIONS

def Fram(fram):
	import bpy
	bpy.context.scene.frame_current = fram

def Key_Rota(obje, rota, glob = True):
	import bpy
	if obje == None:
		obje = bpy.context.object.name
	Sele(obje)
	if rota != None:
		if glob == True:
			Rota(rota)
		else:
			Rota(rota, loca = True)
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

def Cycl(name = "", trac = "axle.legs.l", t = 0.0, radi = 0.2, spee = 0.1, uppe = "", lowe = "", end = "", righ = False, arms = False, armsPath = True, armsRati = 0.05, uppeLeng = 1.0, loweLeng = 1.0, faci = (1.0, 0.0), path_star = 2):
	import bpy
	import math
	import mathutils
	Math = MathLink()
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
	nameStri = name + "." + part
	if arms == False or (arms == True and armsPath == True):
		#peda = CyclPath(t = t, acti = acti, spee = spee, radi = radi, phas = phas, righ = righ, arms = arms)
		left = 1
		if righ == True:
			left = 0
		peda = cycle_path(t, spee, radi, phas, 16, left, 0, path_star)
		#print(peda)
	else:
		peda = Math.Elli(t = -t, spee = spee, radi = radi, phas = phas, rati = armsRati)
	peda = Math.VectScal(peda, radi)
	#tracPosi = scen.objects[trac].localPosition
	Sele(trac)
	tracPosi = LocaRead()
	#print(tracPosi)
	tota = uppeLeng + loweLeng
	# the distance from hip where the foot should be
	#uppePosi = scen.objects[uppe].localPosition
	Sele(uppe)
	uppePosi = LocaRead()
	#print(uppePosi)
	# TODO: convert x/y to x using faci
	uppePosi = (uppePosi[0], 0.0, uppePosi[2])
	targPosi = (peda[0] + tracPosi[0], 0.0, peda[1] + tracPosi[2])
	#uppePosi = (0.0, uppePosi[1], uppePosi[2])
	#targPosi = (0.0, peda[0] + tracPosi[1], peda[1] + tracPosi[2])
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

# TODO: this might be converting to an angle then back to x and y
def cycle_path(t, speed, radius, phase, steps, left, arms, start):
	import bpy
	import math
	Math = MathLink()
	start = 0
	# TODO
	pedal_speed = speed
	ground_height = 0.0
	#y = math.sin(t * 2.0 * math.pi * pedal_speed)
	#x = math.cos(t * 2.0 * math.pi * pedal_speed)
	# TODO: fix this
	y = math.sin(-t * 2.0 * math.pi * pedal_speed)
	x = math.cos(-t * 2.0 * math.pi * pedal_speed)
	# TODO
	if left == 1 and arms == 0 and 1 == 0:
	#if left == 1 and arms == 0:
		Sele("Sphere")
		loc = (x, y, 0.0)
		Loca(loc)
		bpy.ops.anim.keyframe_insert(type='Location', confirm_success=False)
	angle = math.atan2(y, x)
	#print("angle", math.degrees(angle))
	angle += phase
	while angle < 0.0:
		angle += 2.0 * math.pi
	while angle >= 2.0 * math.pi:
		angle -= 2.0 * math.pi
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
	Sele("path")
	# TODO: x and z or y and z or x and y
	#start_x = bpy.context.object.data.vertices[step].co.y
	start_x = bpy.context.object.data.vertices[step].co.x
	start_y = bpy.context.object.data.vertices[step].co.z
	#end_x = bpy.context.object.data.vertices[next_step].co.y
	end_x = bpy.context.object.data.vertices[next_step].co.x
	end_y = bpy.context.object.data.vertices[next_step].co.z
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
	"""
	if step != steps - 1:
		angle_diff = theta_b - theta_a
	else:
		angle_diff = 2.0 * math.pi - theta_a
	#while angle_diff >= 2.0 * math.pi:
	#	angle_diff -= 2.0 * math.pi
	"""
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
	#"""
	m1 = (y / x)
	b1 = 0.0
	#print(end_x, start_x)
	m2 = (end_y - start_y) / (end_x - start_x)
	b2 = (end_y) - m2 * (end_x)
	X = (b2 - b1) / (m1 - m2)
	Y = m1 * X
	#"""
	#X = x
	#Y = y
	#Sele("Sphere")
	#bpy.data.objects["Sphere"].location[1] = X
	#bpy.data.objects["Sphere"].location[2] = Y
	#bpy.ops.anim.keyframe_insert(type='Location', confirm_success = False)
	#if left == 1 and arms == 0:
	if left == 1 and arms == 0 and 1 == 0:
		Sele("Sphere")
		loc = (X, Y, 0.0)
		Loca(loc)
		bpy.ops.anim.keyframe_insert(type='Location', confirm_success=False)
	return X, Y

#######################

####################################

# OBJECT / SCENE / VIEWPORT LOOK

def Hori(colo):
	import bpy
	bpy.context.scene.world.horizon_color = colo

def Visi(togg = True, hide = False):
	import bpy
	if togg == True:
		bpy.context.object.hide = not bpy.context.object.hide
		bpy.context.object.hide_render = not bpy.context.object.hide_render
	else:
		bpy.context.object.hide = hide
		bpy.context.object.hide_render = hide

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

def Empt():
	import bpy
	bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1, view_align=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def Plan():
	import bpy
	bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def Sphe():
	import bpy
	bpy.ops.mesh.primitive_uv_sphere_add(size=1, view_align=False, enter_editmode=False, location = (0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def Cube():
	import bpy
	bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def Cyli():
	import bpy
	bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def Cone():
	import bpy
	bpy.ops.mesh.primitive_cone_add(radius1=1, radius2=0, depth=2, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def VertAdd_():
	Cube()
	VertSeleAll_()
	Edit()
	Merg()
	Edit()
	VertDese()

def Curv(clea = True):
	import bpy
	bpy.ops.curve.primitive_bezier_curve_add(location=(0.0, 0.0, 0.0))
	if clea == True:
		Edit()
		bpy.ops.curve.select_all(action = 'DESELECT')
		bpy.context.object.data.splines[0].bezier_points[1].select_control_point = True
		bpy.ops.curve.delete(type='VERT')
		Edit()

def Circ():
	import bpy
	bpy.ops.curve.primitive_bezier_circle_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def Text(text = "", name = "", conv = True, mate = True):
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

def Came():
	import bpy
	bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 10.0), rotation=(0.0, 0.0, 0.0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

def Ligh(typ_ = 'POINT'):
	import bpy
	bpy.ops.object.lamp_add(type = typ_, view_align=False, location=(0.0, 0.0, 0.0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

# TODO: make work for different facing directions
def VectDraw(vect, orig = (0.0, 0.0, 0.0), cyliScal = (0.4, 0.05, 0.05), coneScal = (0.1, 0.1, 0.1)):
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

#############################################

# READ FUNCTIONS

def LocaRead(worl = False):
	import bpy
	if worl == False:
		retu = tuple(bpy.context.object.location)
	else:
		pare = bpy.context.object.parent
		bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
		retu = tuple((bpy.context.object.location[0], bpy.context.object.location[1], bpy.context.object.location[2]))
		if pare != None:
			Pare(pare.name)
	return retu

def ScalRead():
	import bpy
	return tuple(bpy.context.object.scale)

def RotaRead():
	import bpy
	return tuple(bpy.context.object.rotation_euler)

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
def Xyz_Most(axis = 2, reverse = True):
	import bpy
	Pyth = PythLink()
	vert = VertList()
	vert = Pyth.SortDime(vert, axis, reverse = reverse)
	return vert[0][axis]

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

# return an index list of selected vertices
def VertListSele():
	import bpy
	retu = []
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
		for edge in bpy.context.object.data.edges:
			if edge.key[0] == inde or edge.key[1] == inde:
				if edge.key[0] == inde:
					retu.append(edge.key[1])
				if edge.key[1] == inde:
					retu.append(edge.key[0])
	return retu

def Prin():
	import bpy
	for obje in bpy.context.scene.objects:
		if obje.select == True:
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
def VertIndeBy__Loca(loca):
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
	# if theyre not exactly the same, return not found
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

def PolyList():
	import bpy
	retu = []
	a = 0
	while a < len(bpy.context.object.data.polygons):
		retu.append(PolyVert(a))
		a += 1
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

def Impo(blenFile = "", pref = "", rena = "", ligh = False, came = False, scal = (1.0, 1.0, 1.0), posi = False, posz = False, rota = False, pivo = "", skip = True, repl = False):
	import os
	Pyth = PythLink()
	Head = HeadLink()
	blenComm = BlenCommLink()

	dire, blenName = FilePath(blenFile)

	# write the blend to read from a file
	writ = {}
	writ.update({"blenName":blenName})
	writ.update({"dire":dire})
	writ.update({"ligh":ligh})
	writ.update({"came":came})
	Pyth.LineTo__File(Pyth.DictTo__Line(writ), "list" + os.sep + "expo")

	expr = ""
	expr += blenComm + " -b " + dire + blenName + ".blend"	
	expr += " --python tempScri.py"

	scri = Head()
	scri += "def main():\n"
	scri += "\tline = Pyth.FileTo__Line(\"list" + os.sep + "expo\")\n"
	scri += "\tline = Pyth.LineTo__Dict(line)\n"
	scri += "\tBlen.Expo(listName = line[\"blenName\"], ligh = line[\"ligh\"], came = line[\"came\"])\n"
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

def Expo(listName = "", ligh = False, came = False):
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
		blenName = blenName[0]
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
