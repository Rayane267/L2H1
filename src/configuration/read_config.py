import json


def readConfig():
    '''
    this function is called upon initialization of the script
    it serves as a way for the script to know what to do, and where to do it : images location, etc
    '''
    try :
        with open("./configuration/configuration.json") as CONFIGURATION:
            config = json.load(CONFIGURATION)
            return config
    except Exception as e:
        print("Error : " , e)
