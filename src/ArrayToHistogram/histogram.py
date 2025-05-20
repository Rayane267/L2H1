from math import atan, degrees, pi, sin
import matplotlib.pyplot as plt
import numpy as np
from ntpath import basename

def ObjectListToHistogram(objects, height, pathToImage):
    """
    Input: Dictionary * int
    Output: List
    takes object dictionary and returns a list containing number of angles appearing by their index
    """
    #print(objects)
    #return value
    angles = [0] * 361 #360 for degrees (361 because of 0-360 error to do)
    #get 2 objects to analyse
    object1 = objects["object 1"]
    object2 = objects["object 2"]
    angleNumber = len(object1) * len(object2)#will be used to normalise
    for c1 in object1:
        for c2 in object2:
            angle = findAngle(c1, c2, height)
            #print(angle, c1,c2)
            angle += 180 #for negative values
            try:
                angles[angle] += 1
            except:
                print(angle)
    #essai
    angles = np.array(angles)
    largestFrequency = np.amax(angles)
    showHistogram(angles, largestFrequency, pathToImage)

def findAngle(coordinate1, coordinate2, height):
    """
    Input: set*set*int
    Output: int
    get 2 coordiante and returns the angle
    """
    opp = (height - coordinate2[0]) - (height - coordinate1[0])
    #print(opp)
    adj = coordinate2[1] - coordinate1[1]
    #different case for the case where the object b is to the left
    if adj < 0:
        if opp <= 0:
            angle = -pi + atan(opp/adj)
        else:
            angle = pi + atan(opp/adj)
    elif adj > 0:
        angle = atan(opp / adj)
    # check for the division by zero
    else:
        if opp > 0:
            angle = pi/2
        else:
            angle = -pi/2
    return round(degrees(angle))

def showHistogram(angles, numAngles, pathToImage):
    """
    Input: List * int * String
    Output: dictionary showing the relational pistion
    """
    xpoints = np.linspace(-pi, pi, 361)#181 because of the 0-360 erreur to do (with radian)
    #xpoints = [x for x in range(-180,181)] #with angle
    histogram = np.array(angles)/numAngles #it normalizes
    ypoints = histogram
    reference = np.power(np.sin(xpoints), 2)
    reference2 = np.power(np.cos(xpoints), 2)

    plt.plot(xpoints, ypoints, 'b')
    plt.plot(xpoints, reference, 'r')
    plt.plot(xpoints, reference2, 'g')

    #find the intersections of sin^2 and the histogram
    idxSin = np.argwhere(np.diff(np.sign(ypoints - reference))).flatten()
    #get y values of intersection points for up and down values
    down = [reference[idxSin[x]] for x in range(len(idxSin)) if idxSin[x] < 180]
    up = [reference[idxSin[x]] for x in range(len(idxSin)) if idxSin[x] > 180]
    # find the intersections of cos^2 and the histogram
    idxCos = np.argwhere(np.diff(np.sign(ypoints - reference2))).flatten()
    # get y values of intersection points for right and left
    right = [reference2[idxCos[x]] for x in range(len(idxCos)) if idxCos[x] > 90 and idxCos[x] < 270]
    left = [reference2[idxCos[x]] for x in range(len(idxCos)) if idxCos[x] < 90 or idxCos[x] > 270]

    #show the histogram and intersections
    plt.plot(xpoints[idxCos], reference2[idxCos], 'ro')
    plt.plot(xpoints[idxSin], reference[idxSin], 'ro')

    #save figure
    plt.savefig(pathToImage + "Figure.png")

    # close the figure
    plt.clf()

    #create the return dictionary
    relativePos = dict()
    if len(down) > 0:
        relativePos["down"] = max(down)
    if len(up) > 0:
        relativePos["up"] = max(up)
    if len(right) > 0:
        relativePos["right"] = max(right)
    if len(left) > 0:
        relativePos["left"] = max(left)
    with open(pathToImage + "_HISTOGRAM.txt", mode='w',encoding='utf-8-sig') as outputFile:
        outputFile.write(str(relativePos) + "\n")


    return relativePos