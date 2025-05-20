import numpy as np
import sys

sys.setrecursionlimit(20000)

def getBlankCoordinate(pbmArray):
    """
    Input: Image array * BackgroundColor(int or list)
    Output: List of coordinate of pixels that it's value is not 0
    """
    #create the return value
    PixelList = []
    #get background color
    bgColor = pbmArray[0][0]
    height = pbmArray.shape[0]
    width = pbmArray.shape[1]
    for i in range(height):
        for j in range(width):
            if not(np.array_equal(pbmArray[i][j], bgColor)):
                PixelList.append((i,j))
    return PixelList

def getEightPixel(i,j, pixelList):
    """
    Input: entier * entier (for coordinate) * pixelList (list of coordinate
    Output: List of pixels surrounding the pixel given and pixels that is in the pixel list
    """
    surroundings = [(x,y) for x in range(i-1, i+2) for y in range(j-1,j+2)]
    surroundingsInList = []
    for elem in surroundings:
        if elem in pixelList:
            surroundingsInList.append(elem)
    #remove the original element
    surroundingsInList.remove((i,j))
    return surroundingsInList

def separatefromList(pixelList):
    """
    this function seperates the values of the pixelList in different object by the fact that if the pixel is connex
    Input: list
    Output: dictionary * int
    """
    longeur = len(pixelList)
    objects = {
        "object 1": []
    }
    nbComponent = 1
    i = 0
    while(i < longeur):
        analysePixel(i,objects, nbComponent, pixelList)
        if i >len(pixelList):
            break
        i+=1
        nbComponent +=1
        objects["object " + str(nbComponent)] = []
    return objects, nbComponent


def analysePixel(i, objects, nbComponent, pixelList):
    """
    put every connexe pixel in a list as value in the object dictionary
    Input: Int, dictionnary, int, list
    Output: None
    """
    surrounding = getEightPixel(pixelList[i][0],pixelList[i][1], pixelList)
    #add to the dictionnary
    objects["object " + str(nbComponent)].append(pixelList[i])
    #remove from the pixel list
    pixelList.remove(pixelList[i])
    #do the same for the rest
    for elem in surrounding:
        if(elem) in pixelList:
            i1 = pixelList.index(elem)
            analysePixel(i1, objects, nbComponent, pixelList)