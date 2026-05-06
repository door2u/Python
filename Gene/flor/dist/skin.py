
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

# example usage:
# import bpy
# rename all branches (should be separate objects. if not, use BranSepa() first.)
# for a in range(len(bpy.context.scene.objects)):
#   name = bpy.context.scene.objects[a].name
#   name = name.split(".")
#   bpy.context.scene.objects[a].name = "bran." + name[1]
# skin branches
# for a in range(894):
#   BranSkin(name = "bran." + Blen.Pad_(a))
# then join, shade smooth, add materials, etc
def BranSkin(name = "bran.000", twis = 0):
    import bpy
    # TODO: pass a different name to Uplo() if a conflict exists
    objeName = name.split(".")
    if len(objeName) > 0: objeName = objeName[0]
    if objeName == "obje":
        print("branches can't be named 'obje', because it will conflict with the 'Uplo()' function, which names uploads 'obje'.")
    else:
        ringCoun = 8
        Blen.Sele(name)
        Blen.Appl()
        founList = []
        for a in range(len(Blen.Vertices())):
            founList.append(False)
        uploCoun = 0
        adde = False
        while (False in founList):
            # get a connected line from start to end
            Blen.Sele(name)
            for a in range(len(founList)):
                if founList[a] == False:
                    conn = Blen.VertConn(a)
                    if len(conn) == 1:
                        vert = a
                        break
            connList = [vert]
            founList[vert] = True
            begi = False
            while True:
                # sort the branch vertices in a line from beginning to end
                conn = Blen.VertConn(vert)
                appe = False
                for con_ in conn:
                    if founList[con_] == False:
                        if len(conn) == 1:
                            # TODO: will the first one always be first
                            if begi == False:
                                begi = True
                                for a in range(len(connList)):
                                    if connList[a] == vert:
                                        connList.pop(a)
                                        break
                                connList.insert(0, vert)
                        connList.append(con_)
                        founList[con_] = True
                        vert = con_
                        appe = True
                        break
                if appe == False:
                    if adde:
                        if len(connList) > 0:
                            reve = True
                            star = bpy.context.object.data.vertices[connList[0]].co
                            for a in range(len(bpy.context.object.data.vertices)):
                                vert = bpy.context.object.data.vertices[a]
                                if a != connList[0]:
                                    if Math.VectSame(star, vert.co):
                                        reve = False
                                        break
                            if reve:
                                new_ConnList = []
                                a = len(connList) - 1
                                while a >= 0:
                                    new_ConnList.append(connList[a])
                                    a -= 1
                                connList = new_ConnList
                    vertList = []
                    edgeList = []
                    # get the angle
                    a = 0
                    while a < len(connList):
                        # add each new ring to its own list
                        vertList.append([])
                        # "this" vertex
                        vec1 = bpy.context.object.data.vertices[connList[a]].co
                        if a < len(connList) - 1:
                            # "next" vertex
                            vec2 = bpy.context.object.data.vertices[connList[a + 1]].co
                            vece = bpy.context.object.data.vertices[connList[len(connList) - 1]].co
                            vece = Math.Vect(vec1, vece)
                            base = Math.VectMagn(vece) / 20.0
                            anglVect = (0.0, 1.0, 0.0)
                            if a == 0:
                                vect = Math.Vect(vec1, vec2)
                            else:
                                # get a vector from previous to next
                                vecp = bpy.context.object.data.vertices[connList[a - 1]].co
                                vect = Math.Vect(vecp, vec2)
                            eule = Math.VectTo__Eule3d__(vect)
                            anglVect = Math.VectRota3d__(anglVect, eule)
                            anglVect = Math.VectNorm(anglVect)
                            anglVect = Math.VectScal(anglVect, base)
                            b = 0
                            while b < ringCoun:
                                anglVect = Math.Quat(anglVect, 360.0 / ringCoun, Math.VectNorm(vect))
                                vertList[a].append(Math.VectAdd_(anglVect, vec1))
                                b += 1
                        # add the center vertex to the end of the ring list
                        vertList[a].append(vec1)
                        a += 1
                    # TODO: organize vert / edge lists for ring select
    		# connect edges between rings
                    if twis == 0:
                        # align edges between rings to prevent twisting
                        for a in range(1, len(vertList) - 1):
                            smal = 0.0
                            smalInde = -1
                            for b in range(len(vertList[a - 1]) - 1):
                                vec1 = Math.Vect(vertList[a - 1][len(vertList[a - 1]) - 1], vertList[a - 1][b])
                                vec1 = Math.VectAdd_(vec1, vertList[a][len(vertList[a]) - 1])
                                vec1 = Math.VectAngl(vec1, vertList[a][0])
                                if smalInde == -1 or vec1 < smal:
                                    smal = vec1
                                    smalInde = b
                            for b in range(len(vertList[a - 1]) - 1):
                                inde = smalInde + b
                                if inde >= len(vertList[a - 1]) - 1:
                                    inde -= len(vertList[a - 1]) - 1
                                edgeList.append(((a - 1) * ringCoun + inde, a * ringCoun + b))
                    elif twis == 1:
                        # dont correct twisting
                        coun = 0
                        for a in range(len(vertList) - 1):
                            for b in range(len(vertList[a])):
                                edgeList.append((coun, coun + ringCoun))
                                coun += 1
                    elif twis == 2:
                        # use random twisting
                        for a in range(1, len(vertList) - 1):
                            import random
                            random.seed()
                            smalInde = random.randint(0, len(vertList[a - 1]) - 2)
                            for b in range(len(vertList[a - 1]) - 1):
                                inde = smalInde + b
                                if inde >= len(vertList[a - 1]) - 1:
                                    inde -= len(vertList[a - 1]) - 1
                                edgeList.append(((a - 1) * ringCoun + inde, a * ringCoun + b))
    		# remove center vertices from lists, expect for the last one
                    for a in range(len(vertList) - 1):
                        vertList[a].pop()
    		# connect edge rings
                    coun = 0
                    for a in range(len(vertList) - 1):
                        coua = coun
                        for b in range(len(vertList[a])):
                            if b < len(vertList[a]) - 1:
                                edgeList.append((coun, coun + 1))
                            else:
                                edgeList.append((coun, coua))
                            coun += 1
                    # branch cap
                    for a in range(len(vertList[len(vertList) - 2])):
                        edgeList.append((coun - ringCoun + a, coun))
    		# flatten vertices to a single list
                    vertUplo = []
                    for a in range(len(vertList)):
                        for b in range(len(vertList[a])):
                            vertUplo.append(vertList[a][b])
    		# upload
                    Blen.Uplo([vertUplo, edgeList, []])
                    uploCoun += 1
    		# add faces
                    # TODO: make a poly list
                    Blen.Edit()
                    bpy.ops.mesh.edge_face_add()
                    Blen.Edit()
                    break
        for a in range(1, uploCoun):
            Blen.Sele("obje." + Blen.Pad_(a))
            Blen.Join("obje")
            Blen.Name("obje")
        # TODO
        Blen.Name(objeName)
        Blen.Sele(name)
        Blen.Dele()
