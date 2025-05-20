def printDebug(JSON_file):
    '''
    this function prints the content of the configuration file.
    it is called if debug mode is on - or if asked in the menu
    '''
    for element in JSON_file:
        print(element + ":"  + str(JSON_file[element]) + "\n")