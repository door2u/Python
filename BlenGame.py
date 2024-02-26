
# cont = bge.logic.getCurrentController()
# scen = bge.logic.getCurrentScene()
# owne = cont.owner

def PythLink(Pyth = None):
	return Pyth
def BlenLink(Blen = None):
	return Blen
def MathLink(Math = None):
	return Math
def HeadLink(Head = None):
	return Head
def BlenCommLink(blenComm = None):
	return blenComm
def BlenDireLink(blenDire = None):
	return blenDire
def LogiDireLink(logiDire = None):
	return logiDire

########################################

# OPTIONS

def EngiGame():
	Blen = BlenLink()
	Blen.Scene().render.engine = 'BLENDER_GAME'

def Reso(x, y):
	Blen = BlenLink()
	Blen.Scene().render.resolution_x = x
	Blen.Scene().render.resolution_y = y
	Blen.Scene().game_settings.resolution_x = x
	Blen.Scene().game_settings.resolution_y = y

def Full():
	Blen = BlenLink()
	Blen.Scene().game_settings.show_fullscreen = True

def FramExte():
	Blen = BlenLink()
	Blen.Scene().game_settings.frame_type = "EXTEND"

def Debu():
	Blen = BlenLink()
	Blen.Scene().game_settings.show_debug_properties = True

def Glsl():
	Blen = BlenLink()
	Blen.Scene().game_settings.material_mode = 'GLSL'

def Mous():
	Blen = BlenLink()
	Blen.Scene().game_settings.show_mouse = True

########################################

# LOGIC

def LogiSensOpti():
	return {'invert':False, 'tick_skip':0, 'use_level':False, 'use_pulse_false_level':False, 'use_pulse_true_level':False, 'use_tap':False}

def LogiContOpti():
	return {'states':1, 'use_priority':False}

# TODO: iterate through all types and check if defaults are correct
def LogiSensDict(typ_ = ""):
	retu = {}
	if typ_ == "ACTUATOR":
		retu = {'type':'ACTUATOR', 'actuator':''}
	if typ_ == "COLLISION":
		retu = {'type':'COLLISION', 'material':'', 'property':'', 'use_material':False, 'use_pulse':False}
	if typ_ == "DELAY":
		retu = {'type':'DELAY', 'delay':0, 'duration':0, 'use_repeat':False}
	if typ_ == "JOYSTICK":
		# ['BUTTON', 'AXIS', 'HAT', 'AXIS_SINGLE']
		# ['RIGHTAXIS', 'UPAXIS', 'LEFTAXIS', 'DOWNAXIS']
		# ['UP', 'DOWN', 'LEFT', 'RIGHT', 'UPRIGHT', 'DOWNLEFT', 'UPLEFT', 'DOWNRIGHT']
		retu = {'type':'JOYSTICK', 'button_number':0, 'event_typ_':'BUTTON', 'joystick_index':0, 'use_all_events':False, 'axis_direction':'RIGHTAXIS', 'axis_number':1, 'axis_threshold':0, 'hat_direction':'UP', 'hat_number':1, 'single_axis_number':0}
	if typ_ == "KEYBOARD":
		# ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10']
		retu = {'type':'KEYBOARD', 'key':'None', 'use_all_keys':False, 'modifier_key_1':'NONE', 'modifier_key_2':'NONE', 'log':'', 'target':''}
	if typ_ == "MESSAGE":
		retu = {'type':'MESSAGE', 'subject':''}
	if typ_ == "MOUSE":
		# ['LEFTCLICK', 'MIDDLECLICK', 'RIGHTCLICK', 'WHEELUP', 'WHEELDOWN', 'MOVEMENT', 'MOUSEOVER', 'MOUSEOVERANY']
		retu = {'type':'MOUSE', 'material':'', 'mouse_event':'LEFTCLICK', 'property':'', 'use_material':'PROPERTY', 'use_pulse':False, 'use_x_ray':False}
	if typ_ == "NEAR":
		retu = {'type':'NEAR', 'distance':1.0, 'property':'', 'reset_distance':2.0}
	if typ_ == "PROPERTY":
		# ['PROPEQUAL', 'PROPNEQUAL', 'PROPINTERVAL', 'PROPCHANGED']
		retu = {'type':'PROPERTY', 'evaluation_type':'PROPEQUAL', 'property':'', 'value':'', 'value_max':'', 'value_min':''}
	if typ_ == "RADAR":
		# ['XAXIS', 'YAXIS', 'ZAXIS', 'NEGXAXIS', 'NEGYAXIS', 'NEGZAXIS']
		retu = {'type':'RADAR', 'angle':0.0, 'axis':'XAXIS', 'distance':0.0, 'property':''}
	if typ_ == "RANDOM":
		retu = {'type':'RANDOM', 'seed':0}
	if typ_ == "RAY":
		# ['XAXIS', 'YAXIS', 'ZAXIS', 'NEGXAXIS', 'NEGYAXIS', 'NEGZAXIS']
		# ['PROPERTY', 'MATERIAL']
		retu = {'type':'RAY', 'axis':'YAXIS', 'material':'', 'property':'', 'range':0.009999999776482582, 'ray_type':'PROPERTY', 'use_x_ray':False}
	return retu

def LogiContDict(typ_ = "PYTHON"):
	# ['SCRIPT', 'MODULE']
	retu = {'type':'PYTHON', 'mode':'SCRIPT', 'module':'', 'text':None, 'use_debug':False}
	if typ_ == "EXPRESSION":
		retu = {'type':'EXPRESSION', 'expression':''}
	elif typ_ == "LOGIC_AND":
		retu = retu = {'type':'LOGIC_AND'}
	elif typ_ == "LOGIC_NAND":
		retu = retu = {'type':'LOGIC_NAND'}
	elif typ_ == "LOGIC_NOR":
		retu = retu = {'type':'LOGIC_NOR'}
	elif typ_ == "LOGIC_OR":
		retu = retu = {'type':'LOGIC_OR'}
	elif typ_ == "LOGIC_XNOR":
		retu = retu = {'type':'LOGIC_XNOR'}
	elif typ_ == "LOGIC_XOR":
		retu = retu = {'type':'LOGIC_XOR'}
	return retu

# TODO: what about options that show when something is selected (sound)
def LogiActuDict(typ_ = ""):
	retu = {}
	if typ_ == "ACTION":
		# ['BLEND', 'ADD']
		# ['PLAY', 'PINGPONG', 'FLIPPER', 'LOOPSTOP', 'LOOPEND', 'PROPERTY']
		retu = {'type':'ACTION', 'action':None, 'apply_to_children':False, 'blend_mode':'BLEND', 'frame_blend_in':0, 'frame_end':0, 'frame_property':'', 'frame_start':0, 'layer':0, 'layer_weight':0.0, 'play_mode':'PLAY', 'priority':0, 'property':'', 'use_additive':False, 'use_continue_last_frame':True, 'use_force':False, 'use_local':False}
	if typ_ == "CAMERA":
		# 'POS_X', 'POS_Y', 'NEG_X', 'NEG_Y'
		retu = {'type':'CAMERA', 'axis':'POS_X', 'damping':0.03125, 'height':0.0, 'max':0.0, 'min':0.0, 'object':None}
	if typ_ == "CONSTRAINT":
		# ['NONE', 'DIRPX', 'DIRPY', 'DIRPZ', 'DIRNX', 'DIRNY', 'DIRNZ']
		# ['NONE', 'DIRPX', 'DIRPY', 'DIRPZ']
		# ['NONE', 'LOCX', 'LOCY', 'LOCZ']
		# ['LOC', 'DIST', 'ORI', 'FH']
		retu = {'type':'CONSTRAINT', 'angle_max':0.0, 'angle_min':0.0, 'damping':0, 'damping_rotation':0, 'direction':'NONE', 'direction_axis':'NONE', 'direction_axis_pos':'NONE', 'distance':0.0, 'fh_damping':0.0, 'fh_force':0.0, 'fh_height':0.0, 'limit':'NONE', 'limit_max':0.0, 'limit_min':0.0, 'material':'', 'mode':'LOC', 'property':'', 'range':0.0, 'rotation_max':(0.0, 0.0, 0.0), 'time':0, 'use_fh_normal':False, 'use_fh_paralel_axis':False, 'use_force_distance':False, 'use_local':False, 'use_material_detect':False, 'use_normal':False, 'use_persistant':False}
	if typ_ == "EDIT_OBJECT":
		# ['RESTOREDYN', 'SUSPENDDYN', 'ENABLERIGIDBODY', 'DISABLERIGIDBODY', 'SETMASS']
		# ['ADDOBJECT', 'ENDOBJECT', 'REPLACEMESH', 'TRACKTO', 'DYNAMICS']
		# ['TRACKAXISX', 'TRACKAXISY', 'TRACKAXISZ', 'TRACKAXISNEGX', 'TRACKAXISNEGY', 'TRACKAXISNEGZ']
		# ['UPAXISX', 'UPAXISY', 'UPAXISZ']
		retu = {'type':'EDIT_OBJECT', 'angular_velocity':(0.0, 0.0, 0.0), 'dynamic_operation':'RESTOREDYN', 'linear_velocity':(0.0, 0.0, 0.0), 'mass':0.0, 'mesh':None, 'mode':'ADDOBJECT', 'object':None, 'time':0, 'track_axis':'TRACKAXISY', 'track_object':None, 'up_axis':'UPAXISZ', 'use_3d_tracking':False, 'use_local_angular_velocity':False, 'use_local_linear_velocity':False, 'use_replace_display_mesh':True, 'use_replace_physics_mesh':False}
	if typ_ == "FILTER_2D":
		# ['ENABLE', 'DISABLE', 'REMOVE', 'MOTIONBLUR', 'BLUR', 'SHARPEN', 'DILATION', 'EROSION', 'LAPLACIAN', 'SOBEL', 'PREWITT', 'GRAYSCALE', 'SEPIA', 'INVERT', 'CUSTOMFILTER']
		retu = {'type':'FILTER_2D', 'mode':'REMOVE', 'filter_pass':0, 'motion_blur_factor':0.0, 'use_motion_blur':True, 'glsl_shader':None}
	if typ_ == "GAME":
		# ['START', 'RESTART', 'QUIT', 'SAVECFG', 'LOADCFG']
		retu = {'type':'GAME', 'mode':'START', 'filename':''}
	if typ_ == "MESSAGE":
		# ['TEXT', 'PROPERTY']
		retu = {'type':'MESSAGE', 'subject':'', 'to_property':'', 'body_type':'TEXT', 'body_message':'', 'body_property':''}
	if typ_ == "MOUSE":
		# ['VISIBILITY', 'LOOK']
		# ['OBJECT_AXIS_X', 'OBJECT_AXIS_Y', 'OBJECT_AXIS_Z']
		retu = {'type':'MOUSE', 'mode':'VISIBILITY', 'visible':True, 'sensitivity_x':2.0, 'threshold_x':0.0, 'min_x':0.0, 'max_x':0.0, 'sensitivity_y':2.0, 'threshold_y':0.0, 'min_y':-1.5707963705062866, 'max_y':1.5707963705062866, 'use_axis_x':True, 'object_axis_x':'OBJECT_AXIS_Z', 'reset_x':True, 'local_x':False, 'use_axis_y':True, 'object_axis_y':'OBJECT_AXIS_X', 'reset_y':True, 'local_y':True}
	if typ_ == "MOTION":
		# ['OBJECT_NORMAL', 'OBJECT_SERVO', 'OBJECT_CHARACTER']
		retu = {'type':'MOTION', 'damping':0, 'derivative_coefficient':0.0, 'force':(0.0, 0.0, 0.0), 'force_max_x':0.0, 'force_max_y':0.0, 'force_max_z':1.0, 'force_min_x':1.0, 'force_min_y':0.0, 'force_min_z':0.0, 'integral_coefficient':0.0, 'linear_velocity':(0.0, 0.0, 0.0), 'mode':'OBJECT_NORMAL', 'offset_location':(0.0, 0.0, 0.0), 'offset_rotation':(0.0, 0.0, 0.0), 'proportional_coefficient':0.0, 'reference_object':None, 'torque':(0.0, 0.0, 0.0), 'use_add_character_location':False, 'use_character_jump':False, 'use_local_force':True, 'use_local_linear_velocity':False, 'use_local_location':True, 'use_local_rotation':True, 'use_local_torque':True, 'use_servo_limit_x':True, 'use_servo_limit_y':True, 'use_servo_limit_z':True}
	if typ_ == "PARENT":
		# ['SETPARENT', 'REMOVEPARENT']
		retu = {'type':'PARENT', 'mode':'SETPARENT', 'object':None, 'use_compound':True, 'use_ghost':True}
	if typ_ == "PROPERTY":
		# ['ASSIGN', 'ADD', 'COPY', 'TOGGLE']
		retu = {'type':'PROPERTY', 'mode':'ASSIGN', 'object':None, 'object_property':'', 'property':'', 'value':''}
	if typ_ == "RANDOM":
		# ['BOOL_CONSTANT', 'BOOL_UNIFORM', 'BOOL_BERNOUILLI', 'INT_CONSTANT', 'INT_UNIFORM', 'INT_POISSON', 'FLOAT_CONSTANT', 'FLOAT_UNIFORM', 'FLOAT_NORMAL', 'FLOAT_NEGATIVE_EXPONENTIAL']
		retu = {'type':'RANDOM', 'chance':0.10000000149011612, 'distribution':'BOOL_CONSTANT', 'float_max':0.0, 'float_min':0.10000000149011612, 'float_value':0.10000000149011612, 'half_life_time':0.10000000149011612, 'int_max':0, 'int_mean':0.10000000149011612, 'int_min':0, 'int_value':0, 'property':'', 'seed':0, 'standard_deviation':0.0, 'use_always_true':False}
	if typ_ == "SCENE":
		# ['RESTART', 'SET', 'CAMERA', 'ADDFRONT', 'ADDBACK', 'REMOVE', 'SUSPEND', 'RESUME']
		retu = {'type':'SCENE', 'camera':None, 'mode':'RESTART', 'scene':None}
	if typ_ == "SOUND":
		# ['PLAYSTOP', 'PLAYEND', 'LOOPSTOP', 'LOOPEND', 'LOOPBIDIRECTIONAL', 'LOOPBIDIRECTIONALSTOP']
		retu = {'type':'SOUND', 'name':'Sound', 'mode':'PLAYSTOP', 'volume':1.0, 'pitch':0.0, 'cone_inner_angle_3d':6.2831854820251465, 'cone_outer_angle_3d':6.2831854820251465, 'cone_outer_gain_3d':0.0, 'distance_3d_max':3.4028234663852886e+38, 'distance_3d_reference':1.0, 'gain_3d_min':0.0, 'gain_3d_max':1.0, 'rolloff_factor_3d':1.0, 'use_sound_3d':False}
	if typ_ == "STATE":
		# ['SET', 'ADD', 'REMOVE', 'CHANGE']
		retu = {'type':'STATE', 'operation':'SET', 'states':[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}
	if typ_ == "STEERING":
		# ['SEEK', 'FLEE', 'PATHFOLLOWING']
		retu = {'type':'STEERING', 'acceleration':3.0, 'distance':1.0, 'facing':True, 'facing_axis':'X', 'lock_z_velocity':True, 'mode':'SEEK', 'navmesh':None, 'normal_up':False, 'self_terminated':False, 'show_visualization':False, 'turn_speed':120.0, 'update_period':0, 'velocity':3.0}
	if typ_ == "VISIBILITY":
		retu = {'type':'VISIBILITY', 'apply_to_children':False, 'use_occlusion':False, 'use_visible':True}
	return retu

# TODO: some things can still converted to an input list, like mouse event, key, and others
def Logi(sensOpti = {}, sensDict = {}, sensName = "", contOpti = {}, contDict = {}, contName = "", actuOpti = {}, actuDict = {}, actuName = ""):
	import os
	import bpy
	Blen = BlenLink()
	if type(sensDict) == dict:
		if sensDict == {}:
			sensType = "ALWAYS"
		else:
			sensType = sensDict["type"]
	else:
		sensType = sensDict
	if type(contDict) == dict:
		if contDict == {}:
			contType = "PYTHON"
			contDict = LogiContDict()
		else:
			contType = contDict["type"]
	else:
		contType = contDict
	if type(actuDict) == dict:
		if actuDict != {}:
			actuType = actuDict["type"]
		else:
			actuType = ""
	else:
		actuType = actuDict
	# add sensor / controller / actuator
	if sensType != "" and sensType != "linkCont" and sensType != "linkSens":
		#print(Blen.Object().name)
		bpy.ops.logic.sensor_add(type = sensType, object = Blen.Object().name)
		Sensors()[len(Sensors()) - 1].show_expanded = False
		if sensDict != {}:
			# sens values
			sensDictDefa = LogiSensDict(typ_ = sensType)
			for key_ in sensDictDefa:
				if key_ != 'type' and sensDict[key_] != sensDictDefa[key_]:
					setattr(Sensors()[len(Sensors()) - 1], key_, sensDict[key_])
		if sensName != "" and sensType != "linkCont":
			Sensors()[len(Sensors()) - 1].name = sensName			
	if contType != "" and contType != "linkSens" and contType != "linkCont" and contType != "linkActu" and sensType != "linkCont":
		bpy.ops.logic.controller_add(type = contType, object = Blen.Object().name)
		Controllers()[len(Controllers()) - 1].show_expanded = False
		if contDict != {}:
			# cont values
			contDictDefa = LogiContDict(contType)
			for key_ in contDictDefa:
				if key_ != 'type' and contDict[key_] != contDictDefa[key_]:
					if contType == "PYTHON" and key_ == 'text':
						name = contDict[key_].split(os.sep)
						name = name[len(name) - 1]
						done = False
						for text in bpy.data.texts:
							if text.name == name:
								done = True
						if done == False:
							bpy.ops.text.open(filepath = contDict[key_])
						Controllers()[len(Controllers()) - 1].text = bpy.data.texts[name]
					else:
						setattr(Controllers()[len(Controllers()) - 1], key_, contDict[key_])
							
		if contName != "" and contType != "linkSens" and contType != "linkActu":
			Controllers()[len(Controllers()) - 1].name = contName
	if actuType != "" and actuType != "linkCont":
		bpy.ops.logic.actuator_add(type = actuType, object = Blen.Object().name)
		Actuators()[len(Actuators()) - 1].show_expanded = False
		if actuDict != {}:
			# actu values
			actuDictDefa = LogiActuDict(actuType)
			for key_ in actuDictDefa:
				if key_ != 'type' and actuDict[key_] != actuDictDefa[key_]:
					if actuType == "SCENE" and key_ == "scene":
						Actuators()[len(Actuators()) - 1].scene = bpy.data.scenes[actuDict[key_]]
					elif actuType == "SOUND" and key_ == "name":
						name = actuDict[key_].split(os.sep)
						name = name[len(name) - 1]
						done = False
						for soun in bpy.data.sounds:
							if soun.name == name:
								done = True
						if done == False:
							bpy.ops.sound.open(filepath = actuDict[key_])
						Actuators()[len(Actuators()) - 1].sound = bpy.data.sounds[name]
					else:
						#print(actuDict[key_])
						setattr(Actuators()[len(Actuators()) - 1], key_, actuDict[key_])
		if actuName != "" and actuType != "linkCont":
			Actuators()[len(Actuators()) - 1].name = actuName
	sensLink = len(Controllers()) - 1
	actuLink = len(Controllers()) - 1
	if sensType == "linkCont":
		if sensName != "":
			sensLink = sensName
	# link
	if sensType == "linkCont":
		Controllers()[sensLink].link(Sensors()[len(Sensors()) - 1])
	contLink = len(Sensors()) - 1
	if contType == "linkSens":
		if contName != "":
			contLink = contName
	if contType == "linkSens" or sensType == "linkSens" or (sensType != "" and contType != ""):
		Controllers()[len(Controllers()) - 1].link(Sensors()[contLink])
	contLink = len(Actuators()) - 1
	if contType == "linkActu":
		if contName != "":
			contLink = contName
	if contType == "linkActu" or (contType != "" and actuType != ""):
		Actuators()[contLink].link(Controllers()[len(Controllers()) - 1])
	if actuType == "linkCont":
		if actuName != "":
			actuLink = actuName
	if actuType == "linkCont":
		Actuators()[len(Actuators()) - 1].link(Controllers()[actuLink])
	# sens options
	if sensOpti != {}:
		sensOptiDefa = LogiSensOpti()
		for key_ in sensOptiDefa:
			if sensOpti[key_] != sensOptiDefa[key_]:
				setattr(Sensors()[len(Sensors()) - 1], key_, sensOpti[key_])
	# cont options
	if contOpti != {}:
		contOptiDefa = LogiContOpti()
		for key_ in contOptiDefa:
			if contOpti[key_] != contOptiDefa[key_]:
				setattr(Controllers()[len(Controllers()) - 1], key_, contOpti[key_])

def Sensors():
	Blen = BlenLink()
	return Blen.Object().game.sensors

def Controllers():
	Blen = BlenLink()
	return Blen.Object().game.controllers

def Actuators():
	Blen = BlenLink()
	return Blen.Object().game.actuators

def Properties():
	Blen = BlenLink()
	return Blen.Object().game.properties

########################################

# PROPERTIES

def Prop(propName = "prop", propType = 'FLOAT', propValu = None):
	import bpy
	bpy.ops.object.game_property_new(name = propName, type = propType)
	if propValu != None:
		Properties()[len(Properties()) - 1].value = propValu

def PropSet_(propName = "prop", propValu = None):
	Properties()[propName].value = propValu

def PropFromDict(dict, pref = "", capi = True, excl = True):
	for key_ in dict:
		if excl == True and pref != key_:
			if capi == True and pref != "":
				stri = ""
				stri += key_[0].capitalize()
				a = 1
				while a < len(key_):
					stri += key_[a]
					a += 1
			PropFromKey_Valu(pref + stri, dict[key_])

def PropFromKey_Valu(key_, valu):
	propType = "FLOAT"
	if type(valu) == int:
		propType = "INT"
	if type(valu) == bool:
		propType = "BOOL"
	if type(valu) == str:
		propType = "STRING"
	Prop(propName = key_, propType = propType, propValu = valu)

########################################

# SCENE

# add a prefix to all objects in a scene
# ! object names must be unique across all scenes
def Pref(pref):
	Blen = BlenLink()
	for obje in Blen.Scene().objects:
		obje.name = pref + "." + obje.name

# add an empty object that holds general information, like active characters
def ScenObje(charList = [], scenObje = "scen_obje", keyb = True, joys = True, joysInde = 0, joysAxis = 1, joysThre = 8191, lookX___Sens = 1.0, lookY___Sens = 1.0, mousCentX___ = True, mousCentY___ = True):
	Blen = BlenLink()
	Blen.Empt()
	Blen.Name(scenObje)
	a = 0
	while a < len(charList):
		char = charList[a]
		Prop(propName = "char." + Blen.Pad_(a + 0), propType = 'BOOL', propValu = True)
		Prop(propName = "charName." + Blen.Pad_(a + 0), propType = 'STRING', propValu = char)
		a += 1
	Prop(propName = "charCoun", propType = 'INT', propValu = len(charList))
	Inpu(keyb = keyb, joys = joys, joysInde = joysInde, joysAxis = joysAxis, joysThre = joysThre, lookX___Sens = lookX___Sens, lookY___Sens = lookY___Sens, mousCentX___ = mousCentX___, mousCentY___ = mousCentY___)

########################################

# INPUT

def Inpu(keyb = True, joys = True, joysInde = 0, joysAxis = 1, joysThre = 8191, lookX___Sens = 2.0, lookY___Sens = 1.0, mousCentX___ = True, mousCentY___ = True):
	Pyth = PythLink()
	logiDire = LogiDireLink()
	Prop(propName = "inpuDire", propType = "FLOAT")
	Prop(propName = "inpuMagn", propType = "FLOAT")
	Prop(propName = "keyb", propType = "BOOL", propValu = keyb)
	Prop(propName = "joys", propType = "BOOL", propValu = joys)
	if joys == True:
		# joystick dead zone (2 ** 13 - 1 by default)
		Prop(propName = "joysThre", propType = "INT", propValu = joysThre)
	sens = "KEYBOARD"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	# TODO: alphabetize
	sensDict["key"] = "W"
	contDict["text"] = logiDire + "inpu.py"
	Logi(sensName = sensDict["key"], sensOpti = sensOpti, sensDict = sensDict, contDict = contDict)
	sensDict["key"] = "A"
	Logi(sensName = sensDict["key"], sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["key"] = "S"
	Logi(sensName = sensDict["key"], sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["key"] = "D"
	Logi(sensName = sensDict["key"], sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensOpti["use_pulse_true_level"] = False
	sensOpti["use_tap"] = True
	sensDict["key"] = "W"
	Logi(sensName = sensDict["key"] + "_T", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["key"] = "A"
	Logi(sensName = sensDict["key"] + "_T", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["key"] = "S"
	Logi(sensName = sensDict["key"] + "_T", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["key"] = "D"
	Logi(sensName = sensDict["key"] + "_T", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["key"] = "LEFT_SHIFT"
	Logi(sensName = sensDict["key"], sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	Prop(propName = "leftShif", propType = "FLOAT")
	Prop(propName = "inpuRighPrev", propType = "FLOAT")
	Prop(propName = "inpuUp__Prev", propType = "FLOAT")
	sens = "JOYSTICK"
	sensDict = LogiSensDict(typ_ = sens)
	sensOpti["use_tap"] = False
	sensDict["joystick_index"] = joysInde
	sensDict["event_type"] = "AXIS_SINGLE"
	sensDict["axis_threshold"] = joysThre
	sensDict["single_axis_number"] = 1
	Logi(sensName = "RIGHTAXIS", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["single_axis_number"] = 2
	Logi(sensName = "UPAXIS", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensOpti["use_pulse_true_level"] = False
	sensDict["event_type"] = "AXIS_SINGLE"
	sensDict["single_axis_number"] = 3
	Logi(sensName = "joysAxisRigh", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["single_axis_number"] = 6
	Logi(sensName = "joysAxisUp__", sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	Prop(propName = "joysAxisRigh", propType = "INT")
	Prop(propName = "joysAxisUp__", propType = "INT")
	Prop(propName = "axisRigh", propType = "FLOAT")
	Prop(propName = "axisUp__", propType = "FLOAT")
	Prop(propName = "axisRighPrev", propType = 'FLOAT')
	Prop(propName = "axisUp__Prev", propType = 'FLOAT')
	Prop(propName = "lookX___Sens", propType = 'FLOAT', propValu = lookX___Sens)
	Prop(propName = "lookY___Sens", propType = 'FLOAT', propValu = lookY___Sens)
	Prop(propName = "mousCentX___", propType = "BOOL", propValu = mousCentX___)
	Prop(propName = "mousCentY___", propType = "BOOL", propValu = mousCentY___)
	sens = "MOUSE"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	sensDict["mouse_event"] = 'MOVEMENT'
	Logi(sensName = 'look', sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")

# TODO: name
# add a "clil" property to an object that gets set to true when the left mouse button is held and false otherwise
def Clil():
	sens = "MOUSE"
	cont = "LOGIC_AND"
	actu = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	actuDict = LogiActuDict(typ_ = actu)
	sensOpti["use_tap"] = True
	sensDict["event"] = 'LEFTCLICK'
	actuDict["property"] = "clil"
	actuDict["value"] = "True"
	Logi(sensDict = sensDict, sensOpti = sensOpti, sensName = "clil", actuDict = actuDict)
	sensOpti["invert"] = True
	actuDict["value"] = "True"
	Logi(sensDict = sensDict, sensOpti = sensOpti, sensName = "clilInve", actuDict = actuDict)
	Prop(propName = "clil", propType = 'BOOL')

# add a "clir" property to an object that gets set to true when the right mouse button is held and false otherwise
def Clir():
	sens = "MOUSE"
	cont = "LOGIC_AND"
	actu = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	actuDict = LogiActuDict(typ_ = actu)
	sensOpti["use_tap"] = True
	sensDict["event"] = 'RIGHTCLICK'
	actuDict["property"] = "clir"
	actuDict["value"] = "True"
	Logi(sensDict = sensDict, sensOpti = sensOpti, sensName = "clir", actuDict = actuDict)
	sensOpti["invert"] = True
	actuDict["value"] = "True"
	Logi(sensDict = sensDict, sensOpti = sensOpti, sensName = "clirInve", actuDict = actuDict)
	Prop(propName = "clil", propType = 'BOOL')

def MousOver():
	Prop(propName = "over", propType = 'BOOL')
	sens = "MOUSE"
	cont = "LOGIC_AND"
	actu = "PROPERTY"
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict(typ_ = cont)
	actuDict = LogiActuDict(typ_ = actu)
	sensDict["mouse_event"] = "MOUSEOVER"
	actuDict["property"] = "over"
	actuDict["value"] = "True"
	Logi(sensDict = sensDict, contDict = contDict, actuDict = actuDict)
	sensOpti = LogiSensOpti()
	sensOpti["invert"] = True
	actuDict["value"] = "False"
	Logi(sensDict = sensDict, sensOpti = sensOpti, contDict = contDict, actuDict = actuDict)

# make an object clickable with mouse over
def MousClic():
	MousOver()
	Prop(propName = "clic", propType = 'BOOL')
	# disable clic when left click is released
	sens = "MOUSE"
	cont = "LOGIC_AND"
	actu = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict(typ_ = cont)
	actuDict = LogiActuDict(typ_ = actu)
	sensOpti["use_tap"] = True
	sensOpti["invert"] = True
	sensDict["mouse_event"] = "LEFTCLICK"
	actuDict["property"] = "clic"
	actuDict["value"] = "False"
	Logi(sensDict = sensDict, sensOpti = sensOpti, contDict = contDict, actuDict = actuDict)
	# enable click when left click is clicked and over is True
	sensOpti["invert"] = False
	actuDict["value"] = "True"
	Logi(sensDict = sensDict, sensOpti = sensOpti, contDict = contDict, actuDict = actuDict)
	# also require over to be True
	sens = "PROPERTY"
	sensDict = LogiSensDict(typ_ = sens)
	sensDict["property"] = "over"
	sensDict["value"] = "True"
	Logi(sensDict = sensDict, contDict = "linkActu")

########################################

# CHARACTERS

# specify surfaces that characters can move on
def PathInit(pathList = []):
	Blen = BlenLink()
	for path in pathList:
		Blen.Sele(path[0])
		numb = path[0]
		numb = numb.split(".")
		numb = numb[len(numb) - 1]
		Prop(propName = "path", propType = 'BOOL')
		Prop(propName = "numb", propType = 'INT', propValu = int(numb))
		Prop(propName = "stai", propType = 'BOOL', propValu = path[1])

# add empties that cast rays down and check if theyre on a path
# TODO
def PathChec(empt = 1.0, heig = 1.8, forw = (1.0, 0.0), coun = 16):
	#import bpy
	import math
	Blen = BlenLink()
	logiDire = LogiDireLink()
	name = Blen.Object().name
	angl = math.atan2(forw[1], forw[0])
	sensOpti = LogiSensOpti()
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	contDict["text"] = logiDire + "path.py"
	a = 0
	while a < coun:
		Blen.Empt()
		Blen.Name(name + "." + "path" + "." + Blen.Pad_(a))
		Blen.Pare(name)
		Blen.Move((math.cos(angl) * empt, math.sin(angl) * empt, heig))
		if a == 0:
			Prop(propName = "numb", propType = 'INT')
		Prop(propName = "pathChec", propType = "BOOL", propValu = True)
		Prop(propName = "owne", propType = "STRING", propValu = name)
		Logi(sensOpti = sensOpti, contDict = contDict)
		angl += 2.0 * math.pi / coun
		a += 1

def Char(loca = (0.0, 0.0, 0.0), dire = "", empt = 1.0, cyclArms = True, acti = []):
	Blen = BlenLink()
	Math = MathLink()
	logiDire = LogiDireLink()
	# should the move automatically orient the character to the destination. gets disabled by Cont() by default.
	Prop(propName = "orie", propType = 'BOOL', propValu = True)
	name = Blen.Object().name
	Blen.Sele(name + "." + "head")
	headLoca = Blen.LocaRead()
	heig = Blen.Xyz_Most(axis = 2)
	heig += headLoca[2]
	#print("heig", heig)
	Blen.Sele(name)
	Prop(propName = "heig", propType = 'FLOAT', propValu = heig)
	# get the "x-most" part of the head. assumes character is facing +x. used for first-person camera placement
	Blen.Sele(name + "." + "head")
	fronMost = Blen.Xyz_Most(axis = 0)
	Blen.Sele(name)
	Prop(propName = "fronMost", propType = 'FLOAT', propValu = fronMost)
	Blen.Sele(name + "." + "body")
	bodyLoca = Blen.LocaRead(worl = True)
	Blen.Sele(name)
	Prop(propName = "bodyHeig", propType = 'FLOAT', propValu = bodyLoca[2])
	Blen.Sele(name)
	GrouCast(heig = heig)
	Blen.Sele(name)
	# movement animation
	Cycl(acti = acti, dire = dire)
	Prop(propName = "move", propType = 'BOOL')
	Prop(propName = "z___", propType = 'FLOAT')
	sens = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	sensDict["property"] = "move"
	sensDict["value"] = "True"
	contDict["text"] = logiDire + "move.py"
	Logi(sensName = "move", sensOpti = sensOpti, sensDict = sensDict, contDict = contDict)
	PathChec(empt = empt, heig = heig)
	Blen.Sele(name)
	Blen.Loca(loca)

def GrouCast(heig = 1.8, scenName = ""):
	Blen = BlenLink()
	logiDire = LogiDireLink()
	obje = Blen.Object()
	char = obje.name
	loca = obje.location
	emptName = char + "." + "grou_cast"
	# add two empties, one above, one below. cast from upper to lower and look for "path" var. set character height to intersection point.
	Blen.Empt()
	Blen.Object().name = emptName + ".d"
	Blen.Pare(pare = char)
	Blen.Object().location = loca
	Blen.Object().location[2] -= heig
	Blen.Pare(pare = char)
	Blen.Empt()
	Blen.Object().name = emptName
	Blen.Pare(pare = char)
	Blen.Object().location = loca
	Blen.Object().location[2] += heig
	Blen.Pare(pare = char)
	sensOpti = LogiSensOpti()
	contOpti = LogiContOpti()
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	contOpti["use_priority"] = True
	contDict["text"] = logiDire + "grou_cast.py"
	Logi(sensOpti = sensOpti, contOpti = contOpti, contDict = contDict)
	Prop(propName = "owne", propType = 'STRING', propValu = char)
	# TODO: is this being used
	Prop(propName = "grou", propType = 'BOOL', propValu = True)
	Prop(propName = "grouHeig", propType = 'FLOAT')

# cyclSpee: speed of arm / leg rotation
# radi: diplacement from an axle
# cyclArms: should the arms be animated
def Cycl(acti = [], dire = ""):
	import os
	Blen = BlenLink()
	Math = MathLink()
	logiDire = LogiDireLink()
	name = Blen.Object().name
	sensOpti = LogiSensOpti()
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	Blen.Sele(name + ".knee.l")
	loc1 = Blen.LocaRead(worl = True)
	Blen.Sele(name + ".hip.l")
	loc2 = Blen.LocaRead(worl = True)
	LegsUppe = Math.Dist(loc1, loc2)
	Blen.Sele(name + ".foot.l")
	loc1 = Blen.LocaRead(worl = True)
	Blen.Sele(name + ".knee.l")
	loc2 = Blen.LocaRead(worl = True)
	LegsLowe = Math.Dist(loc1, loc2)
	Blen.Sele(name + ".elbow.l")
	loc1 = Blen.LocaRead(worl = True)
	Blen.Sele(name + ".shoulder.l")
	loc2 = Blen.LocaRead(worl = True)
	ArmsUppe = Math.Dist(loc1, loc2)
	Blen.Sele(name + ".hand.l")
	loc1 = Blen.LocaRead(worl = True)
	Blen.Sele(name + ".elbow.l")
	loc2 = Blen.LocaRead(worl = True)
	ArmsLowe = Math.Dist(loc1, loc2)
	Blen.Sele(name)
	Prop(propName = "legsUppe", propType = 'FLOAT', propValu = LegsUppe)
	Prop(propName = "legsLowe", propType = 'FLOAT', propValu = LegsLowe)
	Prop(propName = "armsUppe", propType = 'FLOAT', propValu = ArmsUppe)
	Prop(propName = "armsLowe", propType = 'FLOAT', propValu = ArmsLowe)
	# up / down bob when moving
	actiSet = False
	for act_ in acti:
		if actiSet == False:
			actiSet = True
			Prop(propName = "acti", propType = "STRING", propValu = act_["acti"])
		# load animation path from a blend file in the character folder (a path for the characters legs to follow)
		CyclPath(dire = dire + name + os.sep, name = act_["acti"])
		Blen.Sele(name)
		contDict["text"] = logiDire + "cycl.py"
		Logi(sensOpti = sensOpti, contDict = contDict)
		Prop(propName = "cyclTime", propType = "TIMER")
		PropFromDict(act_, pref = act_["acti"])
		Prop(propName = act_["acti"], propType = "INT")

# TODO: default path
def CyclPath(dire = "", name = "", armsPath = True):
	import os
	Blen = BlenLink()
	Pyth = PythLink()
	Head = HeadLink()
	part = ["legs"]
	if armsPath == True:
		part.append("arms")
	for par_ in part:
		#################################
		expr = BlenCommLink() + " " + "-b" + " " + dire + "cycl_" + name + "_" + par_ + ".blend" + " " + "--python-expr \""
		expr += Head()
		expr += "def main():\n"
		expr += "\tBlenGame.CyclWrit()\n"
		expr += "main()\n"
		expr += "\""
		#################################
		os.system(expr)
		line = Pyth.FileTo__Line("list" + os.sep + "cycl")
		line = Pyth.StriListTo__Tupl(line)
		CyclRead(poin = line, name = name, part = par_.capitalize())

def CyclWrit():
	import os
	import bpy
	Blen = BlenLink()
	Pyth = PythLink()
	path = "path"
	Blen.Sele(path)
	if Blen.Object().type == 'CURVE':
		Blen.Dupl()
		Blen.Conv()
	poinList = []
	for poin in Vertices():
		poinList.append(str(tuple(bpy.data.objects[path].location + poin.co)))
	Pyth.LineTo__File(poinList, "list" + os.sep + "cycl")

def CyclRead(poin = [], name = "", part = "legs"):
	import math
	Pyth = PythLink()
	dist = 0.0
	a = 0
	while a < len(poin):
		dime = ["X", "Y"]
		for dim_ in dime:
			# [name]_[legs/arms]_x_00, [name]_[legs/arms]_y_00
			stri = name + part + dim_
			stri += Pyth.Pad_(a, 2)
			# add the var
			poi = 0.0
			if dim_ == "X":
				poi = poin[a][0]
			if dim_ == "Y":
				poi = poin[a][2]
			Prop(propName = stri, propType = 'FLOAT', propValu = poi)
		# add the distance between this point and the next point
		if a < len(poin) - 1:
			dist += math.hypot(poin[a + 1][1] - poin[a][1], poin[a + 1][2] - poin[a][2])
		else:
			# last point and first point
			dist += math.hypot(poin[0][1] - poin[a][1], poin[0][2] - poin[a][2])
		a += 1

def ActiDict(name = "jog1"):
	retu = {}
	if name == "jog1":
		retu.update({"acti":"jog"})
		retu.update({"spee":0.15})
		retu.update({"cyclSpee":10.0})
		retu.update({"cyclArms":True})
		retu.update({"armsPath":True})
		retu.update({"armsRadi":1.0})
		retu.update({"armsRati":0.2})
		retu.update({"legsRadi":3.6})
		retu.update({"osci":0.04})
		retu.update({"tilt":0.15})
		retu.update({"rotaSpee":0.1})
	# TODO
	if name == "spr1":
		pass
	return retu

# TODO: faci
def AxleSet_(name = "", armsLeft = (0.0, 0.0, 0.0), armsRigh = (0.0, 0.0, 0.0), legsLeft = (0.0, 0.0, 0.0), legsRigh = (0.0, 0.0, 0.0)):
	Blen = BlenLink()
	Blen.Sele(name + ".axle.arms.l")
	Blen.Loca((armsLeft[0], Blen.Object().location[1], armsLeft[1]))
	Blen.Sele(name + ".axle.arms.r")
	Blen.Loca((armsRigh[0], Blen.Object().location[1], armsRigh[1]))
	Blen.Sele(name + ".axle.legs.l")
	Blen.Loca((legsLeft[0], Blen.Object().location[1], legsLeft[1]))
	Blen.Sele(name + ".axle.legs.r")
	Blen.Loca((legsRigh[0], Blen.Object().location[1], legsRigh[1]))

def Blin():
	logiDire = logiDireLink()
	Prop(propName = "blin", propType = 'FLOAT')
	Prop(propName = "blinTrig", propType = 'INT')
	Prop(propName = "blinTime", propType = 'FLOAT')
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict()
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	contDict["text"] = logiDire + 'blin.py'
	Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict)

########################################

# CONTROL

# simple motion. wasd to a script that checks path empties
def MotiSimp(spee = 0.2):
	logiDire = LogiDireLink()
	sens = "KEYBOARD"
	actu = "MOTION"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	actuDict = LogiActuDict(typ_ = actu)
	sensOpti["use_pulse_true_level"] = True
	sensDict["key"] = 'W'
	contDict["text"] = logiDire + "moti_simp.py"
	actuDict["offset_location"] = (spee, 0.0, 0.0)
	Logi(sensOpti = sensOpti, sensDict = sensDict, sensName = sensDict["key"], contDict = contDict, actuDict = actuDict, actuName = sensDict["key"])
	sensDict["key"] = 'A'
	actuDict["offset_location"] = (0.0, spee, 0.0)
	Logi(sensOpti = sensOpti, sensDict = sensDict, sensName = sensDict["key"], contDict = 'linkCont', actuDict = actuDict, actuName = sensDict["key"])
	sensDict["key"] = 'S'
	actuDict["offset_location"] = (-spee, 0.0, 0.0)
	Logi(sensOpti = sensOpti, sensDict = sensDict, sensName = sensDict["key"], contDict = 'linkCont', actuDict = actuDict, actuName = sensDict["key"])
	sensDict["key"] = 'D'
	actuDict["offset_location"] = (0.0, -spee, 0.0)
	Logi(sensOpti = sensOpti, sensDict = sensDict, sensName = sensDict["key"], contDict = 'linkCont', actuDict = actuDict, actuName = sensDict["key"])
	Prop(propName = "dire", propType = 'INT')

# TODO
# note: character is not controllable until "cont" property is set to True. CharCame() does this, but without CharCame(), cont will need to be set to True elsewhere.
def Cont(faci = (1.0, 0.0), tracHeig = 4.0, grav = -9.8, veloInit = 1.5, coun = 16):
	import math
	Blen = BlenLink()
	Math = MathLink()
	logiDire = LogiDireLink()
	# dont automatically orient. orientation is set by keyboard and mouse of controlled character
	PropSet_(propName = "orie", propValu = False)
	name = Blen.Object().name
	sens = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	sensDict["property"] = "cont"
	sensDict["value"] = "True"
	contDict["text"] = logiDire + "cont.py"
	Logi(sensName = "cont", sensOpti = sensOpti, sensDict = sensDict, contDict = contDict)
	Prop(propName = "cont", propType = 'BOOL')
	Blen.Empt()
	Blen.Object().name = name + ".look"
	Blen.Loca(name)
	LookX___()
	Blen.Pare(name)
	Blen.ApplRota()
	Blen.Sele(name)
	# parent track near, far, and position to control
	name1 = name + "." + "trac" + "." + "firs"
	name2 = name + "." + "trac" + "." + "near"
	name3 = name + "." + "trac" + "." + "posi"
	# angle from camera to height
	cth = 30.0
	# -3 in y, get z from cth
	pos_yz = -2.0
	name4 = name + "." + "trac" + "." + "dist"
	far_yz = -8.0
	ratio = 0.9
	yoff1 = 0.2
	heig = Properties()["heig"].value
	ratio *= heig
	fronMost = Properties()["fronMost"].value + yoff1
	Blen.Sele(name)
	loca = Blen.Object().location
	vect = Math.VectScal(faci, fronMost)
	vect = (vect[0], vect[1], heig)
	Blen.Empt()
	Blen.Loca(Math.VectAdd_(vect, loca))
	Blen.Name(name1)
	Blen.Pare(name + "." + "look")
	Blen.ApplRota()
	Blen.Empt()
	vect = (-vect[0], -vect[1], vect[2])
	Blen.Loca(Math.VectAdd_(vect, loca))
	Blen.Name(name2)
	Blen.Pare(name + "." + "look")
	Blen.ApplRota()
	Blen.Empt()
	z = pos_yz * math.sin(cth)
	vect = Math.VectScal(faci, pos_yz)
	vect = (vect[0], vect[1], z)
	Blen.Loca(Math.VectAdd_(vect, loca))
	Blen.Name(name3)
	Blen.Pare(name + "." + "look")
	Blen.ApplRota()
	Blen.Empt()
	z = far_yz * math.sin(cth)
	vect = Math.VectScal(faci, far_yz)
	vect = (vect[0], vect[1], tracHeig)
	Blen.Loca(Math.VectAdd_(vect, loca))
	Blen.Name(name4)
	Blen.Pare(name + "." + "look")
	Blen.ApplRota()
	a = 0
	while a < coun:
		Blen.Sele(name + "." + "path" + "." + Blen.Pad_(a))
		Blen.Pare(name + "." + "look")
		Blen.ApplRota()
		a += 1
	Blen.Sele(name)
	loca = Blen.LocaRead()
	Blen.Sele(name + ".look")
	Blen.Loca(loca)
	Blen.Sele(name)

########################################

# CAMERA

# TODO
def CharCame(cameName = "Camera", tab = False, faci = (1.0, 0.0), scroSens = 10, lookY___Limi = True, lookY___LimiInve = False, lookY___Uppe = 1.710422666954443, lookY___Lowe = 1.2915436464758039, charList = []):
	import math
	Blen = BlenLink()
	logiDire = LogiDireLink()
	PropSet_(propName = "cont", propValu = True)
	char = Blen.Object().name
	Blen.Sele(cameName)
	# 1 / number of divisions between near track and distant track
	# TODO: make a parameter
	Prop(propName = "scroSens", propType = "FLOAT", propValu = 0.1)
	# TODO: find a good value for this. make a parameter
	Prop(propName = "cameSpee", propType = "FLOAT", propValu = 0.7)
	Prop(propName = "cameDestX___", propType = "FLOAT")
	Prop(propName = "cameDestY___", propType = "FLOAT")
	Prop(propName = "cameDestZ___", propType = "FLOAT")
	Prop(propName = "cameMaxi", propType = "INT", propValu = int(1.0 / 0.1))
	Prop(propName = "cameCurr", propType = "INT", propValu = int(0.3 / 0.1))
	Prop(propName = "cameZoom", propType = "BOOL", propValu = True)
	Prop(propName = "char", propType = "INT", propValu = -1)
	a = 0
	while a < len(charList):
		if charList[a] == char:
			break
		a += 1
	if a < len(charList):
		PropSet_(propName = "char", propValu = a)
	sensOpti = LogiSensOpti()
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	contDict["text"] = logiDire + "came.py"
	Logi(sensOpti = sensOpti, contDict = contDict)
	if tab == True:
		sens = "KEYBOARD"
		sensOpti = LogiSensOpti()
		sensDict = LogiSensDict(typ_ = sens)
		sensOpti["use_tap"] = True
		sensDict["key"] = 'TAB'
		Logi(sensName = sensDict["key"], sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	Prop(propName = "tab_", propType = "BOOL", propValu = tab)
	sens = "MOUSE"
	sensOpti = LogiSensOpti()
	sensOpti["use_tap"] = True
	sensDict = LogiSensDict(typ_ = sens)
	sensDict["mouse_event"] = "WHEELUP"
	Logi(sensName = sensDict["mouse_event"], sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	sensDict["mouse_event"] = "WHEELDOWN"
	Logi(sensName = sensDict["mouse_event"], sensOpti = sensOpti, sensDict = sensDict, contDict = "linkSens")
	Prop(propName = "firs", propType = 'BOOL')
	Prop(propName = "firsTemp", propType = 'BOOL')
	shor = char.split(".")
	shor = shor[len(shor) - 1]
	Prop(propName = "view", propType = 'STRING', propValu = shor)
	Prop(propName = "near", propType = 'BOOL')
	Prop(propName = "zoom", propType = 'BOOL', propValu = True)
	LookY___()
	rotz = math.atan2(faci[1], faci[0])
	rotz -= math.pi / 2.0
	Blen.RotaSet_((80.0, 0.0, math.degrees(rotz)))
	Blen.Pare(char + "." + "look")
	Blen.Loca(loca = char + "." + "trac" + "." + "posi", worl = True)
	Blen.Sele(char + ".look")
	PropSet_(propName = "lookX___", propValu = True)
	Blen.Sele(char)

# similar to LookX___() below, but uses blenders built-in actuator
def LookX___Blen():
	sens = "MOUSE"
	cont = "LOGIC_AND"
	actu = "MOUSE"
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict(typ_ = cont)
	actuDict = LogiActuDict(typ_ = actu)
	sensDict["mouse_event"] = "MOVEMENT"
	actuDict["mode"] = "LOOK"
	actuDict["use_y_axis"] = False
	Logi(sensDict = sensDict, contDict = contDict, actuDict = actuDict)

def LookX___(lookX___Cut_ = 0.2):
	logiDire = LogiDireLink()
	Prop(propName = "lookX___", propType = 'BOOL')
	# set to true when the script is activated, in case something else needs to be updated
	Prop(propName = "lookX___Acti", propType = 'BOOL')
	Prop(propName = "lookX___Angl", propType = 'FLOAT')
	Prop(propName = "lookX___Cut_", propType = 'FLOAT', propValu = lookX___Cut_)
	sens = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	sensDict["property"] = "lookX___"
	sensDict["value"] = "True"
	contDict["text"] = logiDire + 'look_x.py'
	Logi(sensName = 'lookX___', sensOpti = sensOpti, sensDict = sensDict, contDict = contDict)

# similar to LookY___() below, but uses blenders built-in actuator. the lower version drifts if the game window is bigger than the screen
def LookY___Blen():
	sens = "MOUSE"
	cont = "LOGIC_AND"
	actu = "MOUSE"
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict(typ_ = cont)
	actuDict = LogiActuDict(typ_ = actu)
	sensDict["mouse_event"] = "MOVEMENT"
	actuDict["mode"] = "LOOK"
	actuDict["use_x_axis"] = False
	Logi(sensDict = sensDict, contDict = contDict, actuDict = actuDict)

def LookY___(lookY___Cut_ = 0.2, lookY___Limi = True, lookY___LimiInve = False, lookY___LimiUppe = 1.710422666954443, lookY___LimiLowe = 1.2915436464758039):
	logiDire = LogiDireLink()
	Prop(propName = "lookY___", propType = 'BOOL', propValu = True)
	Prop(propName = "lookY___Acti", propType = 'BOOL')
	Prop(propName = "lookY___Cut_", propType = 'FLOAT', propValu = lookY___Cut_)
	Prop(propName = "lookY___Limi", propType = 'BOOL', propValu = lookY___Limi)
	Prop(propName = "lookY___LimiUppe", propType = 'FLOAT', propValu = lookY___LimiUppe)
	Prop(propName = "lookY___LimiLowe", propType = 'FLOAT', propValu = lookY___LimiLowe)
	# TODO: whats causing this
	Prop(propName = "lookY___LimiInve", propType = 'BOOL', propValu = lookY___LimiInve)
	sens = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	sensDict["property"] = "lookY___"
	sensDict["value"] = "True"
	contDict["text"] = logiDire + 'look_y.py'
	Logi(sensName = 'lookY___', sensOpti = sensOpti, sensDict = sensDict, contDict = contDict)

########################################

# 2D PATH FINDING

# these functions can take a long time to finish, but they can be run once after a scene is constructed and prior to the game assembly script

# build python functions that return the pre-computed shortest path between any two points
def PathFind(obst = True, prefList = [], mark = True, obstName = "", markName = "mark", area = 0, radi = 0.7071067811865476, pathMesh = True, vertList = [], obstList = [], meshName = "path_mesh", tria = True, bump = 0.5, back = False, sort = False, pathPrin = True):
	Math = MathLink()
	if obst == True:
		obstList = Obst(prefList = prefList)
	if mark == True:
		Mark(markName = markName, area = area, radi = radi)
	if pathMesh == True:
		if vertList == []:
			vertList = PathList(markName = markName, area = area)
		PathMesh(vertList = vertList, obstList = obstList, meshName = meshName, area = area, tria = tria, bump = bump, back = back, sort = sort)
	if pathPrin == True:
		Blen.Sele(meshName)
		PathPrinAll_(area = area)

# get a list of obstacles from the scene according a list of prefixes
# eg, prefList = ["wall", "door_frame", "desk", "obst"] will match "wall.000", "005.wall.back", "desk.010", etc.
def Obst(prefList = []):
	retu = []
	for obje in Blen.Scene().objects:
		name = obje.name
		name = name.split(".")
		a = 0
		while a < len(name):
			b = 0
			while b < len(prefList):
				if name[a] == prefList[b]:
					retu.append(obje.name)
	return retu

# place 4 markers around (in x and y) all objects of a given prefix
# radi: how far past (in one dimension) the obstacle should the marker be placed (ai characters will move directly toward markers, so if radi is too close to 0.0 they might intersect with the obstacle)
def Mark(obstList = [], markName = "mark", area = 0, radi = 0.7071067811865476):
	Blen = BlenLink()
	a = 0
	while a < len(obstList):
		Blen.Sele(obstList[a])
		obje = Blen.Object()
		loca = Blen.LocaGeomRead()
		x1 = loca[0] - obje.dimensions[0] / 2.0 - radi
		x2 = loca[0] + obje.dimensions[0] / 2.0 + radi
		y1 = loca[1] - obje.dimensions[1] / 2.0 - radi
		y2 = loca[1] + obje.dimensions[1] / 2.0 + radi
		z = loca[2] + obje.dimensions[2] / 2.0
		locx = [x1, x2]
		locy = [y1, y2]
		for x in locx:
			for y in locy:
				z, pathObje = ObjeOver((x, y, z))
				Blen.Empt()
				Blen.Name(markName + "." + Blen.Pad_(area) + "." + Blen.Pad_(a))
				Blen.Loca((x, y, z))
		a += 1

# select the markers created with Mark() (or created manually) and append each location to a vertex list
def PathList(markName = "mark", area = 0):
	Blen = BlenLink()
	retu = []
	a = 0
	while a < len(Blen.Scene().objects):
		obje = Blen.Scene().objects[a]
		name = obje.name.split(".")
		comp = ""
		b = 0
		while b < len(name) - 1:
			comp += name[b]
			if b < len(name) - 2:
				comp += "."
			b += 1
		if comp == markName:
			Blen.Sele(obje.name)
			inst = Blen.Inst(obje.name)
			# append the instance and the vertex location so that the list can be sorted by instance
			# the list is sorted by instance so that paths between vertices represent paths between markers
			retu.append([inst, Blen.LocaRead()])
		a += 1
	retu = sorted(retu)
	# remove the instance entry
	a = 0
	while a < len(retu):
		retu[a] = retu[a][1]
		a += 1
	return retu

# connect the vertices in vertList with an edge if they are not obstructed by an obstacle in obstList
# bump: move vertices up in z by bump. sometimes a cast will succeed where it shouldnt if a marker is on the same plane as the terrain and the bottom of the obstacle. bump moves it up so that a raycast will hit the side of an obstacle. if the obstacle is shorter than bump, the ray will miss where it might have been intended as a hit.
def PathMesh(vertList = [], obstList = [], meshName = "path_mesh", area = 0, tria = True, bump = 0.5, back = False, sort = False):
	Blen = BlenLink()
	obst = []
	a = 0
	while a < len(obstList):
		Blen.Sele(obstList[a])
		if tria == True:
			Blen.Tria()
		# TODO: check if this still works when an obstacle is a child
		vert = Blen.VertList()
		cent = Blen.CentList()
		norm = Blen.NormList()
		poly = Blen.PolyList()
		scal, rota, loca = Blen.TranRead()
		obst.append(ObstTran(vert, cent, norm, poly, scal, rota, loca))
		a += 1
	# for all vertices, if line of sight exists to another vertex, connect the vertices by an edge
	edgeList = []
	a = 0
	while a < len(vertList):
		b = a + 1
		while b < len(vertList):
			boun = False
			# for all obstacles
			c = 0
			while c < len(obst):
				vert = obst[c][0]
				cent = obst[c][1]
				norm = obst[c][2]
				poly = obst[c][3]
				orig = (vertList[a][0], vertList[a][1], vertList[a][2] + bump)
				dest = (vertList[b][0], vertList[b][1], vertList[b][2] + bump)
				# True - the ray hit the obstacle. False - ray missed obstacle and a line of sight exists to the object
				boun = Ray_(orig = orig, dest = dest, vertList = vert, normList = norm, centList = cent, polyList = poly, back = back, sort = sort)
				if boun == True:
					break
				c += 1
			if boun == False:
				edgeList.append((a, b))
			b += 1
		a += 1
	# upload the mesh connecting markers that have lines of sight to each other
	Blen.Uplo([vertList, edgeList, []], name = meshName + "." + Blen.Pad_(area))

# create a script for each point / node in the path mesh that returns the next node in the path to a destination node
def PathPrinAll_(area = 0):
	Blen = BlenLink()
	meshName = Blen.Object().name
	a = 0
	while a < len(Vertices()):
		PathPrin(blen = "", meshName = "path_find", area = area, node = a, size = len(Vertices()))
		a += 1

def PathPrin(meshName = "path_mesh", area = 0, node = 0):
	import bpy
	Pyth = PythLink()
	Blen = BlenLink()
	Math = MathLink()
	meshName += "." + Blen.Pad_(area)
	a = node
	prinList = []
	prinList.append('import bge')
	prinList.append('cont = bge.logic.getCurrentController()')
	prinList.append('owne = cont.owner')
	prinList.append("def PathFind" + Blen.Pad_(a) + "_" + "(b):")
	prinList.append("\tnext = -1")
	Blen.Sele(meshName)
	size = len(Vertices())
	vertLoca = (Vertices()[a].co.x, Vertices()[a].co.y, Vertices()[a].co.z)
	vertLoca = TranAppl3d__(vertLoca)
	b = 0
	while b < size:
		if a != b:
			Blen.Sele(meshName)
			Blen.Dupl()
			path = Blen.Object().name
			Blen.PathShor(a, b)
			Blen.Edit()
			bpy.ops.mesh.select_all(action = 'INVERT')
			bpy.ops.mesh.delete()
			Blen.Edit()
			leng = len(Vertices())
			if leng > 1:
				# sort the vertex list based on how the edges connect them
				SortBy__Conn(vertLoca)
				# TODO: whats causing sort by connected to truncate paths. possibly unconnected paths
				leng = len(Vertices())
				if leng > 1:
					if b == 0 or (a == 0 and b == 1):
						prinList.append("\tif b == " + str(b) + ":")
					else:
						prinList.append("\telif b == " + str(b) + ":")
					# !!! the next vertex
					vert = Vertices()[1]
					# location of vertex on new path mesh
					loca = (vert.co.x, vert.co.y, vert.co.z)
					loca = TranAppl3d__(loca)
					# select original mesh object
					Blen.Sele(meshName)
					inde = Blen.VertIndeBy__Loca(loca)
					prinList.append("\t\tnext = " + str(inde))
			# delete the path object
			Blen.Sele(path)
			Blen.Dele()
		b += 1
	prinList.append("\towne[\"pathFind_" + Blen.Pad_(a) + "\"] = next")
	prinList.append("a = owne[\"pathFind\"]")
	prinList.append("if a == " + str(a) + ":")
	prinList.append("\tb = owne[\"pathFind_b\"]")
	prinList.append("\towne[\"pathFind\"] = -1")
	prinList.append("\towne[\"pathFind_b\"] = -1")
	prinList.append("\tPathFind" + Blen.Pad_(a) + "_" + "(b)")
	Pyth.LineTo__File(prinList, "scri" + os.sep + "path" + os.sep + "path_find_" + Blen.Pad_(a) + ".py")

def PathPrinBatc(blenFilePath = "", meshName = "path_mesh", area = 0, size = 0):
	import os
	blenComm = BlenCommLink()
	Head = HeadLink()
	dire, blenFilePath = FilePath(blenFilePath)
	a = 0
	while a < size:
		#################################
		expr = blenComm + " -b " + dire + blenFilePath + ".blend"
		expr += " --python-expr "
		expr += "\""
		expr += Head()
		expr += "def main():\n"
		expr += "\tline = BlenGame.PathPrin(meshName = \\\"" + meshName + "\\\", area = " + str(area) + ", node = " + str(a) + ")\n"
		expr += "main()\n"
		expr += "\""
		#################################
		os.system(expr)
		a += 1

# load the properties and logic needed for a game object to use the path finding scripts created in the above functions
def PathLoad(size):
	for a in range(size):
		Prop(propName = "path_find_" + blender.pad(a), propType = 'INT', propValu = -1)
		sens = "PROPERTY"
		sensDict = LogiSensDict(typ_ = sens)
		contDict = LogiContDict()
		sensDict["property"] = "path_find"
		sensDict["value"] = str(a)
		contDict["text"] = "scri" + os.sep + "path" + os.sep + "path_find_" + Blen.Pad_(a) + ".py"
		Logi(sensDict = sensDict, contDict = contDict)

########################################

# GAME ANIMATION

# poseList = []
# poseList.append(["sit", 0.5, 'ratio', 0.25, 'FLOAT'])
# poseList.append(["stand", 0.5])
# Blen.Sele(charName)
# BlenGame.Pose(poseList)
def Pose(poseList):
	Blen = BlenLink()
	Prop(propName = "poseNumb", propType = 'INT', propValu = -1)
	Prop(propName = "poseCoun", propType = 'INT', propValu = len(poseList))
	exis = False
	for prop in Properties():
		if prop.name == "time":
			exis = True
	if exis == False:
		Prop(propName = "time", propType = 'FLOAT')
	exis = False
	for prop in Properties():
		if prop.name == "timer":
			exis = True
	if exis == False:
		Prop(propName = "timer", propType = 'TIMER')
	# load logic
	sens = "PROPERTY"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict(typ_ = sens)
	contDict = LogiContDict()
	sensOpti["use_pulse_true_level"] = True
	sensDict["evaluation_type"] = "PROPGREATERTHAN"
	sensDict["property"] = "poseNumb"
	sensDict["value"] = "-1"
	contDict["text"] = logiDire + "pose.py"
	Logi(sensDict = sensDict, contDict = contDict)
	# load pose-specific properties
	a = 0
	for pose in poseList:
		poseStri = "pose" + "." + Blen.Pad_(a)
		pose_name = pose[0]
		Prop(propName = poseStri + ".time", propType = 'FLOAT', propValu = pose[1])
		Prop(propName = poseStri + ".name", propType = 'STRING', propValu = pose_name)
		Prop(propName = poseStri, propType = 'BOOL')
		time = pose[1]
		b = 2
		if len(pose) > 2:
			while b < len(pose):
				inpuNumb = int((b - 2) / 3)
				inpuStri = poseStri + "." + "inputs" + "." + Blen.Pad_(inpuNumb)
				propType = pose[b + 2]
				Prop(propName = inpuStri, propType = propType, propValu = pose[b + 1])
				Prop(propName = inpuStri + "." + "name", propType = 'STRING', propValu = pose[b])
				Prop(propName = inpuStri + "." + "type", propType = 'STRING', propValu = pose[b + 2])
				b += 3
		Prop(propName = poseStri + "." + "noi", propType = 'INT', propValu = inpuNumb + 1)
		a += 1

########################################

# GUI

# create lines of text in separate scenes to be triggered by a game actuator
# ! this has to be called directly after the scene script, or another script that triggers dialog scenes to load
# TODO: only works for up to two game lines
def Dial(scenName = "", dire = "", resx = 1360, resy = 768):
	import bpy
	Blen = BlenLink()
	# make a scene for each dialog line, and let the scene script trigger them as scene overlays
	dial = []
	time = []
	coun = 0
	# read dialog from files
	fileList = os.listdir(dire)
	fileList = sorted(fileList)
	for a in range(len(fileList)):
		fil_ = fileList[a]
		fil_ = fil_.split(".")
		if len(fil_) > 0:
			if fil_[0] == "dial":
				line = Pyth.FileTo__Line(fileList[a])
				# dialog lines
				if len(fil_) == 2:
					# add a blank entry so that the last dialog gets hidden
					line.append("")
					line.append("")
					dial.append(line)
					coun += 1
				# dialog timing
				elif len(fil_) == 3:
					time.append(line)
	Blen.Sele("scen_obje")
	Prop(propName = "dialTrig", propType = 'INT', propValu = -1)
	Prop(propName = "dialTimer", propType = 'TIMER')
	Prop(propName = "dialTime", propType = 'FLOAT')
	Prop(propName = "dialSets", propType = 'INT', propValu = coun)
	Prop(propName = "dialInde", propType = 'INT')
	# make a (game) character list
	charList = []
	charCoun = 0
	a = 0
	while a < len(dial):
		dia_ = dial[a]
		b = 0
		while b < len(dia_):
			line = dia_[b]
			if len(line) > 0:
				last = line[len(line) - 1]
				# > is a continuation character, it tells this function where to enter a new line on the game screen.
				# > and ., ?, and ! are indications that a dialog string is being read, as opposed to a line of text identifying a (game) character
				if last != "." and last != "?" and last != "!" and last != ">":
					gameChar = line
					exis = False
					c = 0
					while c < len(charList):
						if gameChar == charList[c]:
							exis = True
						c += 1
					if exis == False:
						charList.append(gameChar)
					Prop(propName = "dialChar." + Blen.Pad_(charCoun), propType = 'STRING', propValu = gameChar)
					charCoun += 1
			else:
				if len(dia_[b - 1]) == 0:
					Prop(propName = "dialChar." + Blen.Pad_(charCoun), propType = 'STRING', propValu = "None")
					charCoun += 1
			b += 1
		a += 1
	# types
	# 0 - other
	# 1 - unsplit line
	# 2 - start of a split line
	# 3 - end of a split line
	dialType = []
	a = 0
	dialTrac = 0
	while a < len(dial):
		dia_Typ_ = []
		# start integer. where in the dialog sequence does each dialog set begin in the list of all dialog lines
		Prop(propName = "dialStar." + Blen.Pad_(a), propType = 'INT', propValu = dialTrac)
		b = 0
		while b < len(dial[a]):
			founType = False
			# if the line of text is not blank
			if len(dial[a][b]) > 0:
				last = dial[a][b][len(dial[a][b]) - 1]
				if last == ">":
					# remove >
					dial[a][b] = dial[a][b][0:len(dial[a][b]) - 1]
					dia_Typ_.append(2)
					founType = True
					dialTrac += 1
				if last == "." or last == "?" or last == "!":
					# if the previous line was split
					if dia_Typ_[len(dia_Typ_) - 1] == 2:
						dia_Typ_.append(3)
						founType = True
					else:
						dia_Typ_.append(1)
						founType = True
						dialTrac += 1
			else:
				linePrev = dial[a][b - 1]
				# if the previous line is also blank
				if len(linePrev) == 0:
					dialTrac += 1
					dia_Typ_.append(1)
					founType = True
				else:
					last = linePrev[len(linePrev) - 1]
					if last != "." and last != "?" and last != "!":
						dialTrac += 1
						dia_Typ_.append(1)
						founType = True
			if founType == False:
				dia_Typ_.append(0)
			b += 1
		dialType.append(dia_Typ_)
		a += 1
	Prop(propName = "dialCoun", propType = 'INT', propValu = dialTrac)
	# load each characters image into a dialog scene
	a = 0
	while a < len(charList):
		# make a new scene
		Blen.ScenNew_()
		charScen = scenName + "." + charList[a]
		Blen.scene_rename(charScen)
		Blen.Came()
		Blen.Object().data.type = 'ORTHO'
		Blen.Object().data.ortho_scale = resx / 100.0
		Blen.Loca((resx / 200.0, -1.0 * resy / 200.0, 20.0))
		Blen.Object().name = charScen + ".came"
		Blen.Scene().camera = bpy.data.objects[charScen + ".came"]
		# portrait
		Blen.Plan()
		Blen.Name(charScen + "." + charList[a])
		# position / size
		# TODO: pass placement options
		edge = 50.0
		dimx = Blen.Object().dimensions[0]
		dimy = Blen.Object().dimensions[1]
		Blen.Loca((edge / 100.0 + dimx / 2.0, -1.0 * resy / 100.0 + (edge / 100.0) + dimy / 2.0, 0.0))
		Blen.Mate(name = charList[a], use_shadeless = True)
		Blen.MateText(charList[a])
		Blen.Imag(dire + charList[a] + ".png")
		Blen.Text(text = charList[a], conv = True)
		Blen.Scal((0.4, 0.4, 0.4))
		Blen.OrigGeom()
		Blen.Mate(use_shadeless = True)
		Blen.Loca((edge / 100.0 + dimx / 2.0, -1.0 * resy / 100.0 + edge / 200.0, 0.0))
		Blen.ScenSet_(scenName)
		Blen.Sele("scen_obje")
		actu = "SCENE"
		actuDict = LogiActuDict(typ_ = actu)
		actuDict["scene"] = scenName + "." + charList[a]
		# on
		actuDict["mode"] = "ADDFRONT"
		Logi(contDict = "linkActu", actuName = scenName + "." + charList[a] + ".1", actuDict = actuDict)
		# off
		actuDict["mode"] = "REMOVE"
		Logi(contDict = "linkActu", actuName = scenName + "." + charList[a] + ".0", actuDict = actuDict)
		a += 1
	# load dialog into separate scene
	dialCoun = 0
	a = 0
	while a < len(dial):
		dia_ = dial[a]
		b = 0
		while b < len(dia_):
			if dialType[a][b] != 0:
				if dialType[a][b] != 3:
					Blen.ScenNew_()
					dialScen = scenName + "." + "dial." + Blen.Pad_(dialCoun)
					Blen.ScenName(dialScen)
					Blen.Came()
					Blen.Object().data.type = 'ORTHO'
					Blen.Object().data.ortho_scale = resx / 100.0
					Blen.Loca((resx / 200.0, -1.0 * resy / 200.0, 20.0))
					Blen.Object().name = dialScen + ".came"
					Blen.Scene().camera = bpy.data.objects[dialScen + ".came"]
				Blen.Text(text = dia_[b], conv = True)
				Blen.Name(dialScen + "." + "text." + Blen.Pad_(dialCoun))
				Blen.Scal((0.4, 0.4, 0.4))
				if dialType[a][b] == 1:
					Blen.Loca((2.8, -6.18, 0.0))
					dialCoun += 1
				if dialType[a][b] == 2:
					Blen.Loca((2.8, -6.0, 0.0))
					dialCoun += 1
				if dialType[a][b] == 3:
					Blen.Loca((2.8, -6.6, 0.0))
			b += 1
		a += 1
	# loads times onto the scene object
	# switch back to main scene
	Blen.ScenSet_(scenName)
	Blen.Sele("scen_obje")
	timeCoun = 0
	a = 0
	while a < len(time):
		tim_ = time[a]
		b = 0
		while b < len(tim_):
			Prop(propName = "dialTime." + Blen.Pad_(timeCoun), propType = 'FLOAT', propValu = float(tim_[b]))
			actu = "SCENE"
			actuDict = LogiActuDict(typ_ = actu)
			actuDict["scene"] = scenName + ".dial." + Blen.Pad_(timeCoun)
			actuDict["mode"] = "ADDFRONT"
			Logi(contDict = "linkActu", actuName = scenName + ".dial." + Blen.Pad_(timeCoun) + ".1", actuDict = actuDict)
			actuDict["mode"] = "REMOVE"
			Logi(contDict = "linkActu", actuName = scenName + ".dial." + Blen.Pad_(timeCoun) + ".0", actuDict = actuDict)
			timeCoun += 1
			b += 1
		a += 1

########################################

# RAYCASTING

# TODO: recursively subdivide raycast regions and eliminate larger regions at one time, and track which polygons correspond to certain regions

# obstacles receiving casts need to be triangulated.
# seems to work ok but it hasnt been tested for all cases
# also slow, needs to be ran with a raycast engine.
# if you want to make a decent fps and dont need it to be perfect you can draw a circle around heads and rectangles around bodies / limbs.

# prepare a blender game for raycasting logic by exporting obstacle geometry
# stat: is the corresponding object in the obstacle list stationary or static. if it is, convert to world space ahead of time. let stat be an empty list to default to True
# room: which room should the owner be in to check against the provided obstacles. defaults to -1 for any, but thats much slower. if an object is not stationary, room is overwritten to -1
# boun: check intersection with a bounding box before checking geometry. this will likely speed up the ray_ script since its only looking for one collision and likely doesnt collide with the majority of others
# bounOnly: set the corresponding entry to True to count a hit if a ray passes through a bounding box and ignore geometry. defaults to False if the boun list is empty.
# an obstacle list can be created with the Obst() function
def Ray_Expo(obstList = [], stat = [], room = [], boun = [], bounOnly = [], tria = True):
	import os
	Pyth = PythLink()
	Blen = BlenLink()
	Pyth.LineTo__File([], "list" + os.sep + "ray_")
	a = 0
	while a < len(obstList):
		obst = obstList[a]
		Blen.Sele(obst)
		name = Blen.Object().name
		if a < len(stat):
			sta_ = stat[a]
		else:
			sta_ = True
		if a < len(boun):
			bou_ = boun[a]
		else:
			bou_ = True
		if a < len(bounOnly):
			bounOnl_ = bounOnly[a]
		else:
			bounOnl_ = False
		if a < len(room) and sta_ == True:
			roo_ = room[a]
		else:
			roo_ = -1
		if bou_ == True:
			# positive x bounding box
			bbxp = Blen.Xyz_Most(axis = 0)
			# negative x bounding box
			bbxn = Blen.Xyz_Most(axis = 0, reverse = False)
			bbyp = Blen.Xyz_Most(axis = 1)
			bbyn = Blen.Xyz_Most(axis = 1, reverse = False)
			bbzp = Blen.Xyz_Most(axis = 2)
			bbzn = Blen.Xyz_Most(axis = 2, reverse = False)
			if sta_ == True:
				scal, rota, loca = Blen.TranRead()
				bbxp = Math.Tran3d__(bbxp, scal, rota, loca)
				bbxn = Math.Tran3d__(bbxn, scal, rota, loca)
				bbyp = Math.Tran3d__(bbyp, scal, rota, loca)
				bbyn = Math.Tran3d__(bbyn, scal, rota, loca)
				bbzp = Math.Tran3d__(bbzp, scal, rota, loca)
				bbzn = Math.Tran3d__(bbzn, scal, rota, loca)
			verb, cenb, norb, edge, polb = BounTo__Geom(bbxp, bbxn, bbyp, bbyn, bbzp, bbzn)
		if bounOnl_ == False:
			if tria == True:
				Blen.Tria()
			vert = Blen.VertList()
			cent = Blen.CentList()
			norm = Blen.NormList()
			poly = Blen.PolyList()
			if sta_ == True:
				scal, rota, loca = Blen.TranRead()
				vert, cent, norm, poly = ObstTran(vert, cent, norm, poly, scal, rota, loca)
		else:
			vert = []
			cent = []
			norm = []
			poly = []
		verb = Pyth.TuplListTo__Stri(verb)
		cenb = Pyth.TuplListTo__Stri(cenb)
		norb = Pyth.TuplListTo__Stri(norb)
		polb = Pyth.TuplListTo__Stri(polb)
		vert = Pyth.TuplListTo__Stri(vert)
		cent = Pyth.TuplListTo__Stri(cent)
		norm = Pyth.TuplListTo__Stri(norm)
		poly = Pyth.TuplListTo__Stri(poly)
		Pyth.LineTo__File([name, str(sta_), str(roo_), str(boun), str(bounOnl_), verb, cenb, norb, polb, vert, cent, norm, poly], "list" + os.sep + "ray_", mode = "a")
		a += 1

# load raycasting logic into a blender game
# ! before calling this, add a sensor that triggers the raycast, and name it "ray_" so that "ray_.py" can check the sensor. avoid using an always sensor if possible, that might slow the game, or use blenders faster built-in ray sensor, or increase skip
def Ray_(pref = "obst"):
	import os
	Pyth = PythLink()
	logiDire = LogiDireLink()
	fil_ = "list" + os.sep + "ray_"
	line = Pyth.FileTo__Line(fil_)
	Prop(propName = "targ", propType = 'STRING')
	# True if the ray hit the target
	Prop(propName = "ray_", propType = 'BOOL')
	inst = 0
	a = 0
	while a < len(line):
		if a < len(line):
			name = line[a]
		a += 1
		if a < len(line):
			stat = line[a]
		a += 1
		if a < len(line):
			room = line[a]
		a += 1
		if a < len(line):
			boun = line[a]
		a += 1
		if a < len(line):
			bounOnly = line[a]
		a += 1
		if a < len(line):
			verb = line[a]
		a += 1
		if a < len(line):
			cenb = line[a]
		a += 1
		if a < len(line):
			norb = line[a]
		a += 1
		if a < len(line):
			polb = line[a]
		a += 1
		if a < len(line):
			vert = line[a]
		a += 1
		if a < len(line):
			cent = line[a]
		a += 1
		if a < len(line):
			norm = line[a]
		a += 1
		if a < len(line):
			poly = line[a]
		a += 1
		stat = Pyth.StriTo__Bool(stat)
		room = int(room)
		boun = Pyth.StriTo__Bool(boun)
		bounOnly = Pyth.StriTo__Bool(bounOnly)
		verb = StriListTo__Tupl(verb)
		cenb = StriListTo__Tupl(cenb)
		norb = StriListTo__Tupl(norb)
		polb = StriListTo__Tupl(polb, cast = "i")
		vert = StriListTo__Tupl(vert)
		cent = StriListTo__Tupl(cent)
		norm = StriListTo__Tupl(norm)
		poly = StriListTo__Tupl(poly, cast = "i")
		instStri = Blen.Pad_(inst)
		inst += 1

		# blender game vars
		Prop(propName = pref + "." + instStri + "." + "name", propType = 'STRING', propValu = name)
		Prop(propName = pref + "." + instStri + "." + "stat", propType = 'BOOL', propValu = stat)
		Prop(propName = pref + "." + instStri + "." + "room", propType = 'INT', propValu = room)
		Prop(propName = pref + "." + instStri + "." + "boun", propType = 'BOOL', propValu = boun)
		Prop(propName = pref + "." + instStri + "." + "bounOnly", propType = 'BOOL', propValu = bounOnly)

		Prop(propName = pref + "." + instStri + "." + "verbCoun", propType = 'INT', propValu = len(verb))
		while b in range(len(verb)):
			Prop(propName = pref + "." + instStri + "." + "verb" + "." + Blen.Pad_(b) + "." + "x", propType = 'FLOAT', propValu = verb[b][0])
			Prop(propName = pref + "." + instStri + "." + "verb" + "." + Blen.Pad_(b) + "." + "y", propType = 'FLOAT', propValu = verb[b][1])
			Prop(propName = pref + "." + instStri + "." + "verb" + "." + Blen.Pad_(b) + "." + "z", propType = 'FLOAT', propValu = verb[b][2])
		Prop(propName = pref + "." + instStri + "." + "polbCoun", propType = 'INT', propValu = len(cenb))
		while b in range(len(cenb)):
			Prop(propName = pref + "." + instStri + "." + "cenb" + "." + Blen.Pad_(b) + "." + "x", propType = 'FLOAT', propValu = cenb[b][0])
			Prop(propName = pref + "." + instStri + "." + "cenb" + "." + Blen.Pad_(b) + "." + "y", propType = 'FLOAT', propValu = cenb[b][1])
			Prop(propName = pref + "." + instStri + "." + "cenb" + "." + Blen.Pad_(b) + "." + "z", propType = 'FLOAT', propValu = cenb[b][2])
		while b in range(len(norb)):
			Prop(propName = pref + "." + instStri + "." + "norb" + "." + Blen.Pad_(b) + "." + "x", propType = 'FLOAT', propValu = norb[b][0])
			Prop(propName = pref + "." + instStri + "." + "norb" + "." + Blen.Pad_(b) + "." + "y", propType = 'FLOAT', propValu = norb[b][1])
			Prop(propName = pref + "." + instStri + "." + "norb" + "." + Blen.Pad_(b) + "." + "z", propType = 'FLOAT', propValu = norb[b][2])
		while b in range(len(polb)):
			instPoly = Blen.Pad_(b)
			Prop(propName = pref + "." + instStri + "." + "polbVertCoun" + "." + instPoly, propType = 'INT', propValu = len(polb[b]))
			for c in range(len(polb[b])):
				Prop(propName = pref + "." + instStri + "." + "polbVert" + "." + instPoly + "." + Blen.Pad_(c), propType = 'INT', propValu = polb[b][c])

		Prop(propName = pref + "." + instStri + "." + "vertCoun", propType = 'INT', propValu = len(vert))
		while b in range(len(vert)):
			Prop(propName = pref + "." + instStri + "." + "vert" + "." + Blen.Pad_(b) + "." + "x", propType = 'FLOAT', propValu = vert[b][0])
			Prop(propName = pref + "." + instStri + "." + "vert" + "." + Blen.Pad_(b) + "." + "y", propType = 'FLOAT', propValu = vert[b][1])
			Prop(propName = pref + "." + instStri + "." + "vert" + "." + Blen.Pad_(b) + "." + "z", propType = 'FLOAT', propValu = vert[b][2])
		Prop(propName = pref + "." + instStri + "." + "polyCoun", propType = 'INT', propValu = len(cent))
		while b in range(len(cent)):
			Prop(propName = pref + "." + instStri + "." + "cent" + "." + Blen.Pad_(b) + "." + "x", propType = 'FLOAT', propValu = cent[b][0])
			Prop(propName = pref + "." + instStri + "." + "cent" + "." + Blen.Pad_(b) + "." + "y", propType = 'FLOAT', propValu = cent[b][1])
			Prop(propName = pref + "." + instStri + "." + "cent" + "." + Blen.Pad_(b) + "." + "z", propType = 'FLOAT', propValu = cent[b][2])
		while b in range(len(norm)):
			Prop(propName = pref + "." + instStri + "." + "norm" + "." + Blen.Pad_(b) + "." + "x", propType = 'FLOAT', propValu = norm[b][0])
			Prop(propName = pref + "." + instStri + "." + "norm" + "." + Blen.Pad_(b) + "." + "y", propType = 'FLOAT', propValu = norm[b][1])
			Prop(propName = pref + "." + instStri + "." + "norm" + "." + Blen.Pad_(b) + "." + "z", propType = 'FLOAT', propValu = norm[b][2])
		while b in range(len(poly)):
			instPoly = Blen.Pad_(b)
			Prop(propName = pref + "." + instStri + "." + "polyVertCoun" + "." + instPoly, propType = 'INT', propValu = len(poly[b]))
			for c in range(len(poly[b])):
				Prop(propName = pref + "." + instStri + "." + "polyVert" + "." + instPoly + "." + Blen.Pad_(c), propType = 'INT', propValu = poly[b][c])

	Prop(propName = "obstCoun", propType = 'INT', propValu = inst)

	# logic
	contDict = LogiContDict()
	contDict["text"] = logiDire + "ray_.py"
	Logi(contDict = contDict)

########################################

# SOUND

# audiList: list of audio file names
# loopList: which files are to be looped
# bar_List: how many bars is each file
def Audi(audiList = [], loopList = [], bar_List = [], bpm_ = 120, dire = ""):
	Blen = BlenLink()
	logiDire = LogiDireLink()
	Prop(propName = "audiCoun", propType = 'INT', propValu = len(audiList))
	Prop(propName = "audiTime", propType = 'FLOAT')
	Prop(propName = "audi", propType = 'INT')
	actu = "SOUND"
	sensOpti = LogiSensOpti()
	sensDict = LogiSensDict()
	contDict = LogiContDict()
	actuDict = LogiActuDict(typ_ = actu)
	sensOpti["use_pulse_true_level"] = True
	contDict["text"] = logiDire() + "audi.py"
	actuDict["mode"] = "PLAYEND"
	link = False
	a = 0
	while a < len(audiList):
		Prop(propName = "audiName." + Blen.Pad_(a), propType = 'STRING', propValu = audiList[a])
		Prop(propName = "audiTime." + Blen.Pad_(a), propType = 'FLOAT', propValu = bar_List[a] * 4.0 * 60.0 / bpm_)
		loop = False
		if loopList != []:
			if len(loopList) >= a - 1:
				loop = loopList[a]
		actuDict["name"] = dire + audiList[a]
		if link == False:
			Logi(sensOpti = sensOpti, sensDict = sensDict, contDict = contDict, actuDict = actuDict, actuName = audiList[a])
			link = True
		else:
			Logi(contDict = 'linkActu', actuDict = actuDict, actuName = audiList[a])
		# TODO: rename this var and write a better explanation
		Prop(propName = "audiLoop." + Blen.Pad_(a), propType = 'BOOL')
		Prop(propName = "audiLooped." + Blen.Pad_(a), propType = 'BOOL')
		if loop == True:
			PropSet_(propName = "audiLooped." + Blen.Pad_(a), propValu = True)
			Logi(contDict = 'linkActu', actuDict = actuDict, actuName = audiList[a] + ".loop")
		a += 1

