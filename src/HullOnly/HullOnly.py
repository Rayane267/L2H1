#dependencies
from sys import platform
import numpy as np



def hullExtractor(image):
    """
    This function conserves only the hull of the objects given in parameter
    This is done by looking at every pixel's neighbours
    It outputs a list of every point composing the hull

    Input : numpy array
    Output : list

    """
    pixelList = []
    height = image.shape[0]
    width = image.shape[1]
    for i in range(height):
        for j in range(width):
            if image[i][j] == 255:
                if image[i+1][j+1] == 0 or image[i+1][j] == 0 or image[i+1][j-1] == 0 or image[i-1,j+1] == 0 or image[i-1][j] == 0 or image[i-1][j-1] == 0 or image[i][j-1] == 0 or image[i][j+1] == 0:
                    pixelList.append((i,j))
    return pixelList
