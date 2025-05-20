from sys import platform
import numpy as np
import hashlib as hl

if platform == "win32":
    from src.ArrayToHistogram.histogram import findAngle
else:
    from ArrayToHistogram.histogram import findAngle

def barycentreMethod(objectDict):
    """
    input : a numpy matrix containing the values for each pixel of the image passed in parameter
    """
    barycentreDict = dict()
    for key, pixelList in objectDict.items():
        i = 0
        j = 0
        for pixel in pixelList:
            i += pixel[0]
            j += pixel[1]
        barycentreDict[key] = (i/len(pixelList),j/len(pixelList))
    return barycentreDict


def barycentreSave(relations,path_save):
        name = hl.sha1(str(relations).encode('utf-8')).hexdigest()
        with open(path_save + name +"_BARYCENTRE.txt", mode='w',encoding='utf-8-sig') as outputFile:
            for key, relation in relations.items():
               outputFile.write(key + relation)

def barycentreRelation(barycentreList,n,path_save):
    relations = dict()
    outputRelations = dict()
    for object1, barycentre in barycentreList.items():
        for object2, barycentre2 in barycentreList.items():
            if object1 != object2:
                angle = findAngle(barycentre,barycentre2,n)
                relations[object1 + " " + object2] = angle
    for key, angle in relations.items():
        angle = angle%360
        outputRelations[key] = " Angle :" + str(angle) + " Relation : "
        if angle >= 315 and angle < 45:
            outputRelations[key] += " Right "
        elif angle >= 45 and angle < 135:
            outputRelations[key] += " Up "
        elif angle >= 135  and angle < 225:
            outputRelations[key] += " Left " 
        elif angle >= 225 and angle < 315:
            outputRelations[key] += " Down "
        outputRelations[key] += "\n"
    barycentreSave(outputRelations, path_save)


