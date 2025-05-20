import numpy as np

def seperateFromColors(imageArray, color1, color2):
    """
    Input: numpyArray * list * list (or int * int) depending on format
    Output: dictionary of objects coordinate
    Returns 2 object's coordinate depending on their colors
    """
    height = imageArray.shape[0]
    width = imageArray.shape[1]
    objects = {
        "object 1": [],
        "object 2": []
    }
    for i in range(height):
        for j in range(width):
            #see in wich object the pixel is
            if color1 == list(imageArray[i][j]):
                objects["object 1"].append((i, j))
            elif color2 == list(imageArray[i][j]):
                objects["object 2"].append((i,j))
    return objects

def findColors(imageArray):
    """
    Input: numpyArray
    Output: List
    Gets an image array and finds objects. I suppose that the first pixel is the background.
    I consider that the 2nd element in the list is the first object
    """
    # get background color
    bgColor = imageArray[0][0]
    analysedColors = list()
    # if the background color is an integer (for pbm format)
    if (type(bgColor) == np.uint8):
        analysedColors.append(bgColor)
        imageList = imageArray
        for row in imageList:
            for elem in row:
                if not (elem in analysedColors):
                    analysedColors.append(elem)
    # if it is a list (png jpg etc).
    else:
        analysedColors.append(list(bgColor))
        # print(type(analysedColors))
        imageList = list(imageArray)
        for row in imageList:
            for elem in list(row):
                if not (list(elem) in analysedColors):
                    analysedColors.append(list(elem))
    return analysedColors