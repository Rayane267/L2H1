from hashlib import sha1
from sys import platform
import hashlib as hl
from os import path

#from sympy import N

if platform == "win32":
    import src.configuration.read_config as rc
    import src.configuration.error as error
    import src.loader.image_reader as ir
    import src.separator.sepColorImage as sepC
    import src.separator.seperatorPBM as sepPBM
    import src.ArrayToHistogram.histogram as histogram
    import src.HullOnly.HullOnly as hull
    import src.Barycentre.barycentre as br
else:
    import configuration.read_config as rc
    import configuration.error as error
    import loader.image_reader as ir
    import separator.sepColorImage as sepC
    import separator.seperatorPBM as sepPBM
    import ArrayToHistogram.histogram as histogram
    import HullOnly.HullOnly as hull
    import Barycentre.barycentre as br


def printMenu():
    print("____________________")
    print("|=====| Menu |=====|")
    print("____________________")
    print("Type help to access this menu.")
    print("Methods : ")
    print(" 1 -> Angles histogram : press 1")
    print(" 2 -> Hull angles histogramm : press 2 (Only for PBM)")
    print(" 3 -> Barycentre method : press 3")
    print(" 4 -> Compare all methods : press 4")
    print(" quit -> Angles histogram : type q or quit")


def imageList():
    try:
        numberI = int(input("Enter the number of images to analyse : \n"))
        if type(numberI) != int or numberI < 1:
            print("Please enter a valid number (>0)")
            return None
        L = []
        for i in range(numberI):
            p = input("Path to image : \n")
            #if the path exists add the path in the list
            if path.exists(p):
                L.append(p)
            else:
                print("Path is not valid")
                return None
        return L
    except Exception as e:
        error.printError(e)

def histogramInit(imagesList,path_save):
    #try:
        for elem in imagesList:
            image = ir.returnImageArray(elem)
            name = hl.sha1(elem.encode('utf-8')).hexdigest() + "_Whole_"
            colors = sepC.findColors((image))  # get color list
            if elem[-4:] == ".pbm" or len(colors) == 2: #stupid bit to avoid regex
                pixelList = sepPBM.getBlankCoordinate(image)
                objectList, nbComponents = sepPBM.separatefromList(pixelList)
                histogram.ObjectListToHistogram(objectList,image.shape[0],path_save + name)
            elif len(colors) < 2:
                print("There are no objects in the image")
            else:
                coordinates = sepC.seperateFromColors(image,colors[1],colors[2])
                histogram.ObjectListToHistogram(coordinates,image.shape[0],path_save + name)
    #except Exception as e:
       # error.printError(e)


def hullHistogramInit(imagesList,path_save):
    try:
        for elem in imagesList:
            image = ir.returnImageArray(elem)
            pixelList = hull.hullExtractor(image)
            objectList, nbComponents = sepPBM.separatefromList(pixelList)
            name = hl.sha1(elem.encode('utf-8')).hexdigest() + "_Hull_"
            histogram.ObjectListToHistogram(objectList,image.shape[0],path_save + name)
    except Exception as e:
        error.printError(e)

def barycentreInit(imagesList,path_save):
    try:
        for elem in imagesList:
            image = ir.returnImageArray(elem)
            pixelList = sepPBM.getBlankCoordinate(image)
            objectList, nbComponents = sepPBM.separatefromList(pixelList)
            barycentreList = br.barycentreMethod(objectList)
            br.barycentreRelation(barycentreList,image.shape[0],path_save)
    except Exception as e:
        error.printError(e)

def compareInit(imagesList,path_save):
    barycentreInit(imagesList,path_save)
    hullHistogramInit(imagesList,path_save)
    histogramInit(imagesList,path_save)


def menuError():
    print("Wrong input !")

def menuInit(choice,path_save):
    stop = False
    if choice == "1":
        imagesList = imageList()
        #checks if the path is valid
        if imagesList != None:
            histogramInit(imagesList,path_save)
    elif choice == "2":
        imagesList = imageList()
        if imagesList != None:
            hullHistogramInit(imagesList,path_save)
    elif choice == "3":
        imagesList = imageList()
        if imagesList != None:
            barycentreInit(imagesList,path_save)
    elif choice == "4":
        imagesList = imageList()
        if imagesList != None:
            compareInit(imagesList,path_save)
    elif choice.lower() in ["quit","q"]:
        stop = not(stop)
    elif choice.lower() in ["h","help"]:
        print("See the instruction in the documentation !")
    else:
        menuError()
    return stop

def menu():
    stop = False
    config = rc.readConfig()
    while not(stop):
        printMenu()
        choice = input("Enter your choice : ")
        stop = menuInit(choice,config["path_to_save"])
