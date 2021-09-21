from PropData import PropData

# argparse goes here

def printls(list):
    for i in list:
        print(i)


fIn = open("../examples/sample1.txt", "r")
fOut = open("../examples/out1.gnut", "w")

allCommands = fIn.readlines()
propCommands = []

def handleInput():
    """ Reads in lines from the R5R console and finds prop data """
    for s in allCommands:
        i = s.find("[editor]")
        if i > 0:
            # might need to make this more robust for spawn points
            # what is error handling and input checking
            try:
                pr = PropData(s[i+8:])
                propCommands.append(pr)
            except:
                print("Invalid input: " + s)

def process():
    """ Processes the stuff """
    pass

def export():
    """ Exports the props to a functional Apex Legends map
        (not complete yet) """
    printls(propCommands)


handleInput()
export()

fIn.close()
fOut.close()