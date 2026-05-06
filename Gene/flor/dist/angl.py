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

# TODO: test default path
# expects a series of objects, named like "bran.000", "bran.001", ... and a branPare file which is a list of the spawing branch of each object
def BranAngl(name = "bran", branPare = "./", anglCuto = 80.0):
    if type(branPare) == list or (type(branPare) == str and os.path.exists(branPare)):
        if type(branPare) == str:
            branPare = Pyth.FileTo__Line(branPare)
            branPare = branPare[0]
            branPare = branPare.split(",")
            for a in range(len(branPare)):
                branPare[a] = int(branPare[a])
        for a in range(len(branPare)):
            if branPare[a] != -1:
                chil = name + "." + Blen.Pad_(a)
                pare = name + "." + Blen.Pad_(branPare[a])
                # get the branching vertex
                Blen.Sele(pare)
                Blen.Appl()
                vertPare = Blen.VertList()
                connPare = ConnList()
                Blen.Sele(chil)
                Blen.Appl()
                vertChil = Blen.VertList()
                connChil = ConnList()
                star = (0.0, 0.0, 0.0)
                pareStar = -1
                for b in range(len(vertPare)):
                    for c in range(len(vertChil)):
                        loc1 = vertPare[b]
                        loc2 = vertChil[c]
                        if Math.VectSame(loc1, loc2):
                            star = loc1
                            pareStar = b
                            break
                if Math.VectSame(vertChil[connChil[0]], star) == False:
                    new_ConnList = []
                    a = len(connChil) - 1
                    while a >= 0:
                        new_ConnList.append(connChil[a])
                        a -= 1
                    connChil = new_ConnList[:]
                chilVect = (0.0, 0.0, 0.0)
                pareVect = (0.0, 0.0, 0.0)
                # get child vect
                chilVect = Math.Vect(vertChil[connChil[0]], vertChil[connChil[1]])
                # get parent vect
                if pareStar < len(connPare) - 1:
                    pareVect = Math.Vect(vertPare[connPare[pareStar]], vertPare[connPare[pareStar + 1]])
                else:
                    pareVect = Math.Vect(vertPare[connPare[pareStar - 1]], vertPare[connPare[pareStar]])
                angl = Math.VectAngl(chilVect, pareVect)
                if angl > anglCuto:
                    # rotate child and all its children to within cutoff
                    chilList = ChilList(a, branPare)
                    pivo = vertChil[connChil[0]]
                    scal, rota, loca = Blen.TranRead()
                    pivo = Math.Tran3d__(pivo, scal, rota, loca)
                    rota = angl - anglCuto
                    axis = Math.VectCros3d__(chilVect, pareVect)
                    axis = Math.VectNorm(axis)
                    Rota(chilList, pivo, rota, axis, name)
    else:
        print("provide a branch parent file or branch parent list")

def Rota(chilList, pivo, rota, axis, objeName):
    import bpy
    import math
    a = 0
    while a < len(chilList):
        Blen.Sele(objeName + "." + Blen.Pad_(chilList[a]))
        scal, rot_, loca = Blen.TranRead()
        for b in range(len(bpy.context.object.data.vertices)):
            vect = bpy.context.object.data.vertices[b].co
            vect = Math.Tran3d__(vect, scal, rot_, loca)
            vect = Math.Vect(pivo, vect)
            vect = Math.Quat(vect, rota, axis)
            vect = Math.VectAdd_(pivo, vect)
            vect = Math.Tran3d__Reve(vect, scal, rot_, loca)
            bpy.context.object.data.vertices[b].co = vect
        a += 1

def ChilList(obje, branPare):
    chilList = [obje]
    a = 0
    while a < len(branPare):
        if (a in chilList) == False and (branPare[a] in chilList):
            chilList.append(a)
            a = -1
        a += 1
    return chilList

def ConnList():
    import bpy
    edgeList = Blen.EdgeList()
    name = bpy.context.object.name
    founList = []
    for a in range(len(Blen.Vertices())):
        founList.append(False)
    # get a connected line from start to end
    Blen.Sele(name)
    # find a vertex thats connected to only one other vertex
    for a in range(len(founList)):
        if founList[a] == False:
            conn = Math.VertCon2(a, edgeList, [])
            if len(conn) == 1:
                vert = a
                break
    # start the connected list
    connList = [vert]
    founList[vert] = True
    while True:
        # sort the branch vertices in a line from beginning to end
        conn = Math.VertCon2(vert, edgeList, [])
        for con_ in conn:
            if founList[con_] == False:
                connList.append(con_)
                founList[con_] = True
                vert = con_
                break
        if (False in founList) == False: break
    return connList

# TODO: make this a function
"""
import bpy
for a in range(len(bpy.context.scene.objects)):
    name = bpy.context.scene.objects[a].name
    name = name.split(".")
    bpy.context.scene.objects[a].name = "bran." + name[1]
"""
print()
BranAngl(branPare = [-1, 0, 0, 1, 2, 3, 0, 3, 7, 0, 1, 2, 3, 9, 10, 11, 13, 15, 1, 2, 6, 9, 10, 11, 19, 23, 0, 1, 2, 6, 10, 18, 19, 20, 21, 27, 28, 29, 30, 31, 33, 34, 40, 0, 2, 9, 10, 11, 18, 19, 20, 21, 26, 28, 30, 31, 32, 43, 44, 45, 46, 47, 48, 49, 50, 52, 55, 57, 58, 59, 64, 1, 2, 6, 9, 19, 26, 28, 31, 33, 43, 45, 48, 49, 52, 57, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 87, 89, 0, 1, 6, 20, 26, 31, 33, 43, 44, 45, 48, 50, 71, 75, 77, 79, 80, 81, 101, 103, 104, 105, 106, 107, 109, 110, 112, 116, 117, 119, 121, 122, 0, 1, 2, 9, 19, 20, 26, 28, 33, 43, 44, 50, 72, 76, 80, 101, 102, 107, 108, 109, 110, 112, 119, 133, 135, 136, 139, 142, 144, 145, 146, 147, 148, 150, 151, 153, 154, 158, 159, 160, 9, 20, 28, 43, 44, 45, 50, 72, 74, 76, 101, 104, 105, 108, 112, 133, 135, 136, 138, 139, 142, 143, 144, 145, 146, 151, 173, 175, 176, 177, 179, 180, 182, 183, 185, 186, 189, 191, 192, 194, 195, 199, 201, 206, 207, 217, 0, 26, 33, 50, 72, 101, 104, 105, 108, 133, 135, 136, 138, 139, 142, 144, 148, 173, 174, 177, 178, 179, 180, 181, 182, 184, 186, 190, 191, 192, 193, 219, 221, 222, 223, 224, 225, 226, 227, 228, 229, 231, 232, 233, 235, 236, 237, 240, 242, 244, 252, 255, 257, 258, 260, 262, 270, 273, 274, 277, 0, 9, 20, 26, 43, 45, 74, 76, 101, 104, 105, 133, 136, 138, 144, 173, 174, 176, 179, 181, 183, 219, 220, 223, 224, 226, 230, 231, 232, 236, 255, 280, 282, 283, 285, 287, 288, 289, 290, 291, 294, 295, 296, 297, 298, 299, 300, 301, 303, 304, 305, 306, 307, 309, 310, 311, 312, 319, 327, 336, 0, 9, 26, 43, 101, 104, 108, 133, 138, 139, 142, 173, 176, 183, 219, 220, 224, 226, 230, 232, 279, 280, 282, 283, 285, 287, 288, 290, 291, 299, 301, 303, 306, 327, 339, 341, 343, 344, 348, 349, 350, 351, 352, 354, 357, 358, 359, 360, 361, 362, 364, 367, 370, 373, 374, 375, 382, 394, 0, 26, 43, 74, 101, 105, 133, 136, 139, 173, 174, 176, 220, 224, 233, 279, 280, 282, 283, 287, 291, 296, 303, 339, 340, 341, 342, 343, 344, 346, 348, 350, 351, 360, 361, 362, 364, 370, 375, 382, 394, 397, 398, 399, 401, 403, 404, 405, 406, 408, 409, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 426, 427, 428, 429, 431, 435, 436, 438, 439, 440, 441, 447, 0, 43, 101, 176, 220, 280, 282, 283, 287, 339, 340, 341, 342, 348, 350, 351, 362, 375, 398, 399, 401, 403, 404, 405, 406, 408, 409, 413, 414, 415, 416, 423, 435, 473, 474, 476, 477, 478, 479, 480, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 494, 495, 496, 497, 498, 500, 501, 502, 503, 505, 506, 507, 510, 520, 522, 531, 533, 535, 0, 43, 101, 139, 173, 220, 279, 280, 282, 283, 287, 291, 339, 341, 342, 375, 397, 398, 399, 401, 404, 405, 406, 408, 409, 414, 415, 435, 472, 474, 475, 476, 477, 478, 481, 483, 484, 489, 490, 492, 505, 507, 540, 541, 542, 544, 545, 548, 549, 552, 553, 554, 555, 556, 557, 558, 559, 561, 562, 563, 564, 565, 566, 568, 569, 570, 571, 572, 573, 575, 576, 577, 580, 581, 582, 583, 586, 587, 588, 590, 591, 0, 26, 43, 101, 176, 220, 280, 282, 283, 287, 340, 341, 342, 397, 398, 399, 401, 409, 472, 473, 474, 475, 479, 483, 484, 489, 505, 507, 540, 541, 542, 544, 545, 547, 548, 549, 553, 554, 556, 557, 558, 559, 571, 583, 584, 592, 604, 624, 628, 629, 632, 633, 634, 635, 636, 638, 639, 643, 645, 646, 647, 648, 649, 650, 653, 655, 656, 657, 658, 660, 661, 662, 663, 665, 667, 669, 670, 672, 693, 0, 26, 280, 282, 283, 287, 341, 375, 398, 401, 472, 473, 476, 478, 505, 507, 540, 541, 545, 548, 549, 553, 554, 557, 558, 559, 571, 584, 624, 628, 632, 633, 634, 635, 636, 647, 650, 662, 665, 670, 700, 701, 703, 704, 706, 707, 708, 709, 711, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 727, 728, 729, 730, 731, 733, 734, 737, 739, 740, 744, 754, 762, 26, 283, 341, 342, 397, 398, 399, 472, 473, 478, 505, 540, 541, 548, 549, 553, 554, 559, 624, 628, 629, 632, 633, 635, 636, 639, 650, 670, 700, 703, 706, 708, 714, 727, 729, 773, 774, 776, 778, 779, 783, 784, 787, 788, 789, 791, 794, 795, 797, 799, 801, 802, 803, 804, 807, 811, 812, 825, 828, 282, 283, 341, 398, 399, 541, 548, 559, 569, 629, 632, 633, 635, 703, 706, 708, 717, 775, 776, 779, 783, 785, 803, 811, 832, 833, 835, 837, 843, 845, 848, 850, 851, 853, 854, 855, 283, 341, 342, 399, 505, 632, 776, 779, 785, 836, 868, 869, 870, 875, 876, 399, 541, 776, 883, 399, 887])