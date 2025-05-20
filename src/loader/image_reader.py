#dependencies
from sys import platform
import numpy as np
import cv2 as cv

#Own dependencies
#imports routes depends on the operating system
if platform == "win32":
    import src.configuration.error as error
else:
    import configuration.error as error



def returnImageArray(path_to_image):
    """
    Input : path to a pbm image
    Output : a numpy matrix containing the values for each pixel of the image passed in parameter (returns)
    """
    try:
        image = cv.imread(path_to_image, -1)  # loads image -- to be changed to be more general
        return image
    except Exception as e:
        error.printError(e)
    return