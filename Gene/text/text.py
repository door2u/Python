import importlib.util
import os

spec = importlib.util.spec_from_file_location("Modu", os.path.expanduser("~") + os.sep + "Documents" + os.sep + "prog" + os.sep + "Pyth" + os.sep + "Modu" + os.sep + "Modu.py")
Modu = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Modu)

Pyth = Modu.Pyth
Math = Modu.Math
Blen = Modu.Blen
BlenGame = Modu.BlenGame
Gene = Modu.Gene

def NodeListOld_(nodeGrou = 'NodeGroup'):
	import bpy
	retu = []
	for a in range(len(bpy.data.node_groups[nodeGrou].nodes)):
		retu.append(bpy.data.node_groups[nodeGrou].nodes[a].name)
	return retu

def NodeNew_(nodeListOld_, nodeGrou = 'NodeGroup'):
	import bpy
	retu = None
	for a in range(len(bpy.data.node_groups[nodeGrou].nodes)):
		name = bpy.data.node_groups[nodeGrou].nodes[a].name
		if (name in nodeListOld_) == False:
			retu = bpy.data.node_groups[nodeGrou].nodes[a]
			break
	return retu

def ShadIs__(typ_):
	return typ_ == "ShaderNodeAmbientOcclusion" or typ_ == "ShaderNodeBsdfAnisotropic" or typ_ == "ShaderNodeBsdfDiffuse" or typ_ == "ShaderNodeEmission" or typ_ == "ShaderNodeBsdfGlass" or typ_ == "ShaderNodeBsdfGlossy" or typ_ == "ShaderNodeBsdfHair" or typ_ == "ShaderNodeBsdfRefraction" or typ_ == "ShaderNodeSubsurfaceScattering" or typ_ == "ShaderNodeBsdfToon" or typ_ == "ShaderNodeBsdfTranslucent" or typ_ == "ShaderNodeBsdfTransparent" or typ_ == "ShaderNodeBsdfVelvet" or typ_ == "ShaderNodeVolumeAbsorption" or typ_ == "ShaderNodeVolumeScatter"

def main():

	import bpy
	import math
	import random

	# TODO:

	# sort textures best to worst. then randomly select starting at the positive side of a bell curve

	# normal output
	# normal map

	# text_nudg

	# profiles. store and record source
	# record source image
	# different types of nudges:
	# NodeRand
	# disconnect a number of nodes and randomly relink
	# delete a number of nodes and create new ones

	print()

	global nudg

	# TODO: call if in blender interface
	#bpy.context.area.type = 'NODE_EDITOR'

	typeList = TypeList()

	# adjust node settings for inputs that are unlinked
	nodeRand = False
	# TODO
	# unlink some connections and relink
	#linkRe__ = False
	# delete some nodes and remake them
	nodeRe__ = False

	if nudg != 1.0:
		#while nodeRand == False and linkRe__ == False and nodeRe__ == False:
		while nodeRand == False and nodeRe__ == False:
			random.seed()
			rand = random.randint(0, 1)
			if rand == 1: nodeRand = True
			#random.seed()
			#rand = random.randint(0, 1)
			#if rand == 1: linkRe__ = True
			random.seed()
			rand = random.randint(0, 1)
			if rand == 1: nodeRe__ = True

	pi = math.pi
	miniNodeCoun = 1
	maxiNodeCoun = 80
	
	# pick a number of nodes
	random.seed()
	nodeCoun = random.randint(miniNodeCoun, maxiNodeCoun)

	# TODO
	#nodeRe__ = True
	if nodeRe__:
		# TODO?
		exclList = ['Material Output', 'Group Output']
		nodeRe__Coun = 0
		cuto = 0.3
		a = 0
		leng = len(bpy.data.node_groups['NodeGroup'].nodes)
		while a < leng:
			if (bpy.data.node_groups['NodeGroup'].nodes[a].name in exclList) == False:
				random.seed()
				rand = random.random()
				if rand <= cuto:
					bpy.data.node_groups['NodeGroup'].nodes.remove(bpy.data.node_groups['NodeGroup'].nodes[a])
					nodeRe__Coun += 1
					a -= 1
					leng -= 1
			a += 1

	ShadHas_ = False
	if nodeRe__ or nudg == 1.0:
		for a in range(nodeCoun):
			# TODO: add all nodes
			# pick a random node
			random.seed()
			node = random.randint(0, len(typeList) - 1)
			# TODO: increase the probability of certain nodes
			typ_ = typeList[node]
			bpy.data.node_groups['NodeGroup'].nodes.new(typ_)
			if ShadIs__(typ_): ShadHas_ = True

	if nudg == 1.0 and ShadHas_ == False:
		# TODO: pick any shader
		bpy.data.node_groups['NodeGroup'].nodes.new("ShaderNodeBsdfDiffuse")

	if nudg == 1.0:
		# randomly connect outputs to inputs
		exclNameList = ['Group Input', 'Group Output']
		# TODO
		exclTypeList = ['MIX_SHADER', 'SHADER', 'ShaderNodeMixShader', 'ADD_SHADER', 'ShaderNodeAddShader']
		for a in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
			if (bpy.data.node_groups['NodeGroup'].nodes[a].name in exclNameList) == False:
				for b in range(len(bpy.data.node_groups['NodeGroup'].nodes[a].outputs)):
					connInpuList = []
					if bpy.data.node_groups['NodeGroup'].nodes[a].outputs[b].is_linked == False and (bpy.data.node_groups['NodeGroup'].nodes[a].outputs[b].type in exclTypeList) == False:
						for c in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
							if a != c and (bpy.data.node_groups['NodeGroup'].nodes[c].name in exclNameList) == False:
								for d in range(len(bpy.data.node_groups['NodeGroup'].nodes[c].inputs)):
									if bpy.data.node_groups['NodeGroup'].nodes[c].inputs[d].is_linked == False and (bpy.data.node_groups['NodeGroup'].nodes[c].inputs[d].type in exclTypeList) == False:
										connInpuList.append([c, d])
					if len(connInpuList) > 0:
						pick = len(connInpuList) - 1
						random.seed()
						pick = random.randint(0, pick)
						bpy.data.node_groups['NodeGroup'].links.new(bpy.data.node_groups['NodeGroup'].nodes[connInpuList[pick][0]].inputs[connInpuList[pick][1]], bpy.data.node_groups['NodeGroup'].nodes[a].outputs[b])

	# connect shaders
	outpList = []
	for a in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
		for b in range(len(bpy.data.node_groups['NodeGroup'].nodes[a].outputs)):
			if bpy.data.node_groups['NodeGroup'].nodes[a].type != 'MIX_SHADER' and bpy.data.node_groups['NodeGroup'].nodes[a].type != 'ADD_SHADER' and bpy.data.node_groups['NodeGroup'].nodes[a].name != 'Group Input' and bpy.data.node_groups['NodeGroup'].nodes[a].outputs[b].type == 'SHADER':
				outpList.append([bpy.data.node_groups['NodeGroup'].nodes[a].name, b])
	leng = len(outpList)
	prevLeng = leng
	while leng > 1:
		outpListNew_ = []
		a = 0
		while a < len(outpList):
			nodeListOld_ = NodeListOld_()
			random.seed()
			rand = random.random()
			if rand < 0.5:
				bpy.data.node_groups['NodeGroup'].nodes.new('ShaderNodeMixShader')
			else:
				bpy.data.node_groups['NodeGroup'].nodes.new('ShaderNodeAddShader')
			nod_ = NodeNew_(nodeListOld_)
			random.seed()
			if rand < 0.5:
				# TODO: bell distribution
				nod_.inputs[0].default_value = random.random()
			if rand < 0.5: shif = 1
			else: shif = 0
			if a < leng - 1:
				bpy.data.node_groups['NodeGroup'].links.new(nod_.inputs[shif], bpy.data.node_groups['NodeGroup'].nodes[outpList[a][0]].outputs[outpList[a][1]])
				a += 1
				bpy.data.node_groups['NodeGroup'].links.new(nod_.inputs[shif + 1], bpy.data.node_groups['NodeGroup'].nodes[outpList[a][0]].outputs[outpList[a][1]])
				a += 1
			else:
				if a < leng:
					bpy.data.node_groups['NodeGroup'].links.new(nod_.inputs[shif], bpy.data.node_groups['NodeGroup'].nodes[outpList[a][0]].outputs[outpList[a][1]])
					if rand < 0.5: nod_.inputs[0].default_value = 0.0
				a += 1
		outpList = []
		for a in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
			if bpy.data.node_groups['NodeGroup'].nodes[a].name != 'Group Input' and bpy.data.node_groups['NodeGroup'].nodes[a].type == 'MIX_SHADER' and bpy.data.node_groups['NodeGroup'].nodes[a].outputs[0].is_linked == False:
				outpList.append([bpy.data.node_groups['NodeGroup'].nodes[a].name, 0])
		leng = len(outpList)
	if len(outpList) > 0:
		bpy.data.node_groups['NodeGroup'].links.new(bpy.data.node_groups['NodeGroup'].nodes['Material Output'].inputs[0], bpy.data.node_groups['NodeGroup'].nodes[outpList[0][0]].outputs[outpList[0][1]])

	# TODO: only disconnect links that dont break path to output
	"""
	# randomly disconnect outputs / inputs
	if linkRe__:
		unliList = []
		exclNameList = ['Group Input', 'Group Output', 'Material Output']
		# TODO: what else
		# TODO: 'ShaderNodeAddShader'?
		exclTypeList = ['MIX_SHADER', 'SHADER', 'ShaderNodeMixShader', 'ADD_SHADER', 'ShaderNodeAddShader', 'OUTPUT_MATERIAL']
		for a in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
			if (bpy.data.node_groups['NodeGroup'].nodes[a].name in exclNameList) == False and (bpy.data.node_groups['NodeGroup'].nodes[a].type in exclTypeList) == False:
				for b in range(len(bpy.data.node_groups['NodeGroup'].nodes[a].inputs)):
					cuto = 0.3
					random.seed()
					rand = random.random()
					if rand <= cuto:
						unliList.append([a, b])
		nodeList = unliList[:]
		a = len(nodeList) - 1
		while a > 0:
			if nodeList[a][0] == nodeList[a - 1][0]:
				nodeList.pop(a)
			a -= 1
		for a in range(len(nodeList)):
			# TODO: slow
			exclInpuList = []
			for b in range(len(unliList)):
				if unliList[b][0] == a:
					exclInpuList.append(unliList[b][1])
			nod_ = bpy.data.node_groups['NodeGroup'].nodes[nodeList[a][0]]
			typ_ = nod_.type
			#print("t", typ_)
			# TODO?
			#typ_ = typ_.strip()
			#print("t", typ_)
			inpuList = []
			outpList = []
			# TODO: multiple links
			for b in range(len(nod_.inputs)):
				if len(nod_.inputs[b].links) > 0 and (b in exclInpuList) == False: inpuList.append([nod_.inputs[b].links[0].from_socket, b])
			# TODO: is an output list needed?
			for b in range(len(nod_.outputs)):
				if len(nod_.outputs[b].links) > 0: outpList.append([nod_.outputs[b].links[0].to_socket, b])
			nodeList[a] = [a, a, typ_, inpuList, outpList, ""]
		for a in range(len(nodeList)):
			nodeListOld_ = NodeListOld_()
			typ_ = TypeTo__Type(nodeList[a][2])
			#print("typ_", typ_, nodeList[a][2])
			bpy.data.node_groups['NodeGroup'].nodes.new(typ_)
			nod_ = NodeNew_(nodeListOld_)
			for b in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
				if nod_ == bpy.data.node_groups['NodeGroup'].nodes[b]:
					nodeList[a][1] = b
					break
		for a in range(len(nodeList)):
			inpuList = nodeList[a][3]
			for b in range(len(inpuList)):
				sock = inpuList[b][0]
				# old node index
				nod_ = sock.node
				for c in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
					if nod_ == bpy.data.node_groups['NodeGroup'].nodes[c]:
						nodeInde = c
						break
				# output index
				for c in range(len(bpy.data.node_groups['NodeGroup'].nodes[nodeInde].outputs)):
					if sock == bpy.data.node_groups['NodeGroup'].nodes[nodeInde].outputs[c]:
						inde = c
						break
				# new node index
				for c in range(len(nodeList)):
					if nodeList[c][0] == nodeInde:
						nodeInde = nodeList[c][1]
						break
				bpy.data.node_groups['NodeGroup'].links.new(nod_.inputs[inpuList[b][1]], bpy.data.node_groups['NodeGroup'].nodes[nodeInde].outputs[inde])
		# TODO: output list?
		#for a in range(len(bpy.data.node_groups['NodeGroup'].nodes)): bpy.data.node_groups['NodeGroup'].nodes[a].select = False
		a = len(nodeList) - 1
		while a >= 0:
			# TODO: test
			#bpy.data.node_groups['NodeGroup'].nodes[nodeList[a][0]].select = True
			#bpy.ops.node.delete()
			bpy.data.node_groups['NodeGroup'].nodes.remove(bpy.data.node_groups['NodeGroup'].nodes[nodeList[a][0]])
			a -= 1
	"""

	if nudg == 1.0:
		# randomize all inputs that are unconnected
		for a in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
			nod_ = bpy.data.node_groups['NodeGroup'].nodes[a]
			lis_ = list(range(len(nod_.inputs)))
			# TODO: finish this list
			attrList = ["axis", "blend_type", "color", "component", "convert_from", "convert_to", "distribution", "falloff", "gradient_type", "ground_albedo", "invert", "musgrave_type", "offset", "offset_frequency", "operation", "rotation", "scale", "sky_type", "squash", "squash_frequency", "sun_direction", "translation", "turbidity", "turbulence_depth", "use_clamp", "use_min", "min", "use_max", "max", "vector_type", "wave_profile", "wave_type"]
			for attr in attrList:
				if hasattr(nod_, attr): lis_.append(attr)
			for b in lis_:
				# TODO: can attributes be linked?
				if type(b) == str or (type(b) == int and nod_.inputs[b].is_linked == False):
					try:
						Blen.NodeRand(node = nod_, inpu = b)
					except:
						Pyth.LineTo__File(["True"], "text/erro")

	if nodeRand:
		# randomize unconnected inputs if rand <= cuto
		for a in range(len(bpy.data.node_groups['NodeGroup'].nodes)):
			nod_ = bpy.data.node_groups['NodeGroup'].nodes[a]
			lis_ = list(range(len(nod_.inputs)))
			# TODO: finish this list
			attrList = ["axis", "blend_type", "color", "component", "convert_from", "convert_to", "distribution", "falloff", "gradient_type", "ground_albedo", "invert", "musgrave_type", "offset", "offset_frequency", "operation", "rotation", "scale", "sky_type", "squash", "squash_frequency", "sun_direction", "translation", "turbidity", "turbulence_depth", "use_clamp", "use_min", "min", "use_max", "max", "vector_type", "wave_profile", "wave_type"]
			for attr in attrList:
				if hasattr(nod_, attr): lis_.append(attr)
			for b in lis_:
				# TODO: can attributes be linked?
				if type(b) == str or (type(b) == int and nod_.inputs[b].is_linked == False):
					try:
						cuto = 0.3
						# TODO: count inputs and pick an exact percentage of them
						random.seed()
						rand = random.random()
						if rand <= cuto:
							Blen.NodeRand(node = nod_, inpu = b, nudg = nudg)
					except:
						Pyth.LineTo__File(["True"], "text/erro")

# TODO: RGB CURVES
# TODO: Vector curves
def TypeList():
	typeList = []
	# input
	#typeList.append("ShaderNodeAttribute")
	#typeList.append("ShaderNodeCameraData")
	typeList.append("ShaderNodeFresnel")
	typeList.append("ShaderNodeNewGeometry")
	#typeList.append("NodeGroupInput")
	#typeList.append("ShaderNodeHairInfo")
	#typeList.append("ShaderNodeLayerWeight")
	#typeList.append("ShaderNodeLightPath")
	#typeList.append("ShaderNodeObjectInfo")
	#typeList.append("ShaderNodeParticleInfo")
	typeList.append("ShaderNodeRGB")
	typeList.append("ShaderNodeTangent")
	typeList.append("ShaderNodeTexCoord")
	#typeList.append("ShaderNodeUVMap")
	typeList.append("ShaderNodeValue")
	typeList.append("ShaderNodeWireframe")
	# output
	#typeList.append("NodeGroupOutput")
	#typeList.append("ShaderNodeOutputLamp")
	#typeList.append("ShaderNodeOutputMaterial")
	# shader
	#typeList.append("ShaderNodeAddShader")
	typeList.append("ShaderNodeAmbientOcclusion")
	typeList.append("ShaderNodeBsdfAnisotropic")
	typeList.append("ShaderNodeBsdfDiffuse")
	typeList.append("ShaderNodeEmission")
	typeList.append("ShaderNodeBsdfGlass")
	typeList.append("ShaderNodeBsdfGlossy")
	typeList.append("ShaderNodeBsdfHair")
	typeList.append("ShaderNodeHoldout")
	typeList.append("ShaderNodeBsdfRefraction")
	typeList.append("ShaderNodeSubsurfaceScattering")
	typeList.append("ShaderNodeBsdfToon")
	typeList.append("ShaderNodeBsdfTranslucent")
	typeList.append("ShaderNodeBsdfTransparent")
	typeList.append("ShaderNodeBsdfVelvet")
	typeList.append("ShaderNodeVolumeAbsorption")
	typeList.append("ShaderNodeVolumeScatter")
	# texture
	typeList.append("ShaderNodeTexBrick")
	typeList.append("ShaderNodeTexChecker")
	#typeList.append("ShaderNodeTexEnvironment")
	typeList.append("ShaderNodeTexGradient")
	#typeList.append("ShaderNodeTexImage")
	typeList.append("ShaderNodeTexMagic")
	typeList.append("ShaderNodeTexMusgrave")
	typeList.append("ShaderNodeTexNoise")
	#typeList.append("ShaderNodeTexPointDensity")
	typeList.append("ShaderNodeTexSky")
	typeList.append("ShaderNodeTexVoronoi")
	typeList.append("ShaderNodeTexWave")
	# color
	typeList.append("ShaderNodeBrightContrast")
	typeList.append("ShaderNodeGamma")
	typeList.append("ShaderNodeHueSaturation")
	typeList.append("ShaderNodeInvert")
	typeList.append("ShaderNodeLightFalloff")
	typeList.append("ShaderNodeMixRGB")
	# TODO
	#typeList.append("ShaderNodeRGBCurve")
	# vector
	typeList.append("ShaderNodeBump")
	typeList.append("ShaderNodeMapping")
	typeList.append("ShaderNodeNormal")
	# TODO: takes a uvmap as input
	#typeList.append("ShaderNodeNormalMap")
	# TODO
	#typeList.append("ShaderNodeVectorCurve")
	typeList.append("ShaderNodeVectorTransform")
	# converter
	typeList.append("ShaderNodeBlackbody")
	# TODO: color ramp
	#typeList.append("ShaderNodeValToRGB")
	#typeList.append("ShaderNodeCombineHSV")
	#typeList.append("ShaderNodeCombineRGB")
	#typeList.append("ShaderNodeCombineXYZ")
	typeList.append("ShaderNodeMath")
	typeList.append("ShaderNodeRGBToBW")
	#typeList.append("ShaderNodeSeparateHSV")
	#typeList.append("ShaderNodeSeparateRGB")
	#typeList.append("ShaderNodeSeparateXYZ")
	typeList.append("ShaderNodeVectorMath")
	typeList.append("ShaderNodeWavelength")
	# script
	# group
	# layout
	return typeList

def TypeTo__Type(typ_):
	retu = ""
	if typ_ == "ShaderNodeFresnel": retu = "FRESNEL"
	if typ_ == "ShaderNodeNewGeometry": retu = "NEW_GEOMETRY"
	if typ_ == "ShaderNodeRGB": retu = "RGB"
	if typ_ == "ShaderNodeTangent": retu = "TANGENT"
	if typ_ == "ShaderNodeTexCoord": retu = "TEX_COORD"
	if typ_ == "ShaderNodeValue": retu = "VALUE"
	if typ_ == "ShaderNodeWireframe": retu = "WIREFRAME"
	if typ_ == "ShaderNodeAmbientOcclusion": retu = "AMBIENT_OCCLUSION"
	if typ_ == "ShaderNodeBsdfAnisotropic": retu = "BSDF_ANISOTROPIC"
	if typ_ == "ShaderNodeBsdfDiffuse": retu = "BSDF_DIFFUSE"
	if typ_ == "ShaderNodeEmission": retu = "EMISSION"
	if typ_ == "ShaderNodeBsdfGlass": retu = "BSDF_GLASS"
	if typ_ == "ShaderNodeBsdfGlossy": retu = "BSDF_GLOSSY"
	if typ_ == "ShaderNodeBsdfHair": retu = "BSDF_HAIR"
	if typ_ == "ShaderNodeHoldout": retu = "HOLDOUT"
	if typ_ == "ShaderNodeBsdfRefraction": retu = "BSDF_REFRACTION"
	if typ_ == "ShaderNodeSubsurfaceScattering": retu = "SUBSURFACE_SCATTERING"
	if typ_ == "ShaderNodeBsdfToon": retu = "BSDF_TOON"
	if typ_ == "ShaderNodeBsdfTranslucent": retu = "BSDF_TRANSLUCENT"
	if typ_ == "ShaderNodeBsdfTransparent": retu = "BSDF_TRANSPARENT"
	if typ_ == "ShaderNodeBsdfVelvet": retu = "BSDF_VELVET"
	if typ_ == "ShaderNodeVolumeAbsorption": retu = "VOLUME_ABSORPTION"
	if typ_ == "ShaderNodeVolumeScatter": retu = "VOLUME_SCATTER"
	if typ_ == "ShaderNodeTexBrick": retu = "TEX_BRICK"
	if typ_ == "ShaderNodeTexChecker": retu = "TEX_CHECKER"
	if typ_ == "ShaderNodeTexGradient": retu = "TEX_GRADIENT"
	if typ_ == "ShaderNodeTexMagic": retu = "TEX_MAGIC"
	if typ_ == "ShaderNodeTexMusgrave": retu = "TEX_MUSGRAVE"
	if typ_ == "ShaderNodeTexNoise": retu = "TEX_NOISE"
	if typ_ == "ShaderNodeTexSky": retu = "TEX_SKY"
	if typ_ == "ShaderNodeTexVoronoi": retu = "TEX_VORONOI"
	if typ_ == "ShaderNodeTexWave": retu = "TEX_WAVE"
	if typ_ == "ShaderNodeBrightContrast": retu = "BRIGHTCONTRAST"
	if typ_ == "ShaderNodeGamma": retu = "GAMMA"
	if typ_ == "ShaderNodeHueSaturation": retu = "HUE_SAT"
	if typ_ == "ShaderNodeInvert": retu = "INVERT"
	if typ_ == "ShaderNodeLightFalloff": retu = "LIGHT_FALLOFF"
	if typ_ == "ShaderNodeMixRGB": retu = "MIX_RGB"
	if typ_ == "ShaderNodeBump": retu = "BUMP"
	if typ_ == "ShaderNodeMapping": retu = "MAPPING"
	if typ_ == "ShaderNodeNormal": retu = "NORMAL"
	if typ_ == "ShaderNodeVectorTransform": retu = "VECT_TRANSFORM"
	if typ_ == "ShaderNodeBlackbody": retu = "BLACKBODY"
	if typ_ == "ShaderNodeMath": retu = "MATH"
	if typ_ == "ShaderNodeRGBToBW": retu = "RGBTOBW"
	if typ_ == "ShaderNodeVectorMath": retu = "VECT_MATH"
	if typ_ == "ShaderNodeWavelength": retu = "WAVELENGTH"
	if typ_ == "FRESNEL": retu = "ShaderNodeFresnel"
	if typ_ == "NEW_GEOMETRY": retu = "ShaderNodeNewGeometry"
	if typ_ == "RGB": retu = "ShaderNodeRGB"
	if typ_ == "TANGENT": retu = "ShaderNodeTangent"
	if typ_ == "TEX_COORD": retu = "ShaderNodeTexCoord"
	if typ_ == "VALUE": retu = "ShaderNodeValue"
	if typ_ == "WIREFRAME": retu = "ShaderNodeWireframe"
	if typ_ == "AMBIENT_OCCLUSION": retu = "ShaderNodeAmbientOcclusion"
	if typ_ == "BSDF_ANISOTROPIC": retu = "ShaderNodeBsdfAnisotropic"
	if typ_ == "BSDF_DIFFUSE": retu = "ShaderNodeBsdfDiffuse"
	if typ_ == "EMISSION": retu = "ShaderNodeEmission"
	if typ_ == "BSDF_GLASS": retu = "ShaderNodeBsdfGlass"
	if typ_ == "BSDF_GLOSSY": retu = "ShaderNodeBsdfGlossy"
	if typ_ == "BSDF_HAIR": retu = "ShaderNodeBsdfHair"
	if typ_ == "HOLDOUT": retu = "ShaderNodeHoldout"
	if typ_ == "BSDF_REFRACTION": retu = "ShaderNodeBsdfRefraction"
	if typ_ == "SUBSURFACE_SCATTERING": retu = "ShaderNodeSubsurfaceScattering"
	if typ_ == "BSDF_TOON": retu = "ShaderNodeBsdfToon"
	if typ_ == "BSDF_TRANSLUCENT": retu = "ShaderNodeBsdfTranslucent"
	if typ_ == "BSDF_TRANSPARENT": retu = "ShaderNodeBsdfTransparent"
	if typ_ == "BSDF_VELVET": retu = "ShaderNodeBsdfVelvet"
	if typ_ == "VOLUME_ABSORPTION": retu = "ShaderNodeVolumeAbsorption"
	if typ_ == "VOLUME_SCATTER": retu = "ShaderNodeVolumeScatter"
	if typ_ == "TEX_BRICK": retu = "ShaderNodeTexBrick"
	if typ_ == "TEX_CHECKER": retu = "ShaderNodeTexChecker"
	if typ_ == "TEX_GRADIENT": retu = "ShaderNodeTexGradient"
	if typ_ == "TEX_MAGIC": retu = "ShaderNodeTexMagic"
	if typ_ == "TEX_MUSGRAVE": retu = "ShaderNodeTexMusgrave"
	if typ_ == "TEX_NOISE": retu = "ShaderNodeTexNoise"
	if typ_ == "TEX_SKY": retu = "ShaderNodeTexSky"
	if typ_ == "TEX_VORONOI": retu = "ShaderNodeTexVoronoi"
	if typ_ == "TEX_WAVE": retu = "ShaderNodeTexWave"
	if typ_ == "BRIGHTCONTRAST": retu = "ShaderNodeBrightContrast"
	if typ_ == "GAMMA": retu = "ShaderNodeGamma"
	if typ_ == "HUE_SAT": retu = "ShaderNodeHueSaturation"
	if typ_ == "INVERT": retu = "ShaderNodeInvert"
	if typ_ == "LIGHT_FALLOFF": retu = "ShaderNodeLightFalloff"
	if typ_ == "MIX_RGB": retu = "ShaderNodeMixRGB"
	if typ_ == "BUMP": retu = "ShaderNodeBump"
	if typ_ == "MAPPING": retu = "ShaderNodeMapping"
	if typ_ == "NORMAL": retu = "ShaderNodeNormal"
	if typ_ == "VECT_TRANSFORM": retu = "ShaderNodeVectorTransform"
	if typ_ == "BLACKBODY": retu = "ShaderNodeBlackbody"
	if typ_ == "MATH": retu = "ShaderNodeMath"
	if typ_ == "RGBTOBW": retu = "ShaderNodeRGBToBW"
	if typ_ == "VECT_MATH": retu = "ShaderNodeVectorMath"
	if typ_ == "WAVELENGTH": retu = "ShaderNodeWavelength"
	return retu

main()

