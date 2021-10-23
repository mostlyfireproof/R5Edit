import argparse
import words
from PropData import PropData

DEBUG = False

# Sets up argparse
parser = argparse.ArgumentParser(description='Creates a map from prop data')
parser.add_argument('input', metavar='input', type=str, help='R5R log output in a file')
parser.add_argument('output', metavar='output', type=str, default="map.gnut", help='The name of the map')

args = parser.parse_args()

# Opens files
fIn = open(args.input, "r")
fOutSqrrl = open(args.output, "w")

debugData = ""
# print to a debug file while i'm testing
if DEBUG:
    fOutDebug = open("../examples/dbg.txt", "w")

allCommands = fIn.readlines()
props = {}
propsFormatted = ""


def printls(ls):
    """ Just prints each element of a list """
    for i in ls:
        print(i)


def printdict(d):
    """ Just prints each element of a dictionary """
    for i in d:
        print(i)


def handleInput():
    """ Reads in lines from the R5R console and finds prop data """
    # error handling in case of failed load
    lastBootUp = 0
    for i in reversed(allCommands):
        if (i.find("NEW EDITOR DATA") > -1):
            lastBootUp = allCommands.index(i)
            break
    print("LINE: " + str(lastBootUp))

    # process every command
    for s in allCommands:
        i = s.find("[editor]")      # placing objects
        r = s.find("[delete]")      # deleting objects
        z = s.find("[zip]")         # placing ziplines
        p = s.find("[pickup]")      # placing pickups (grenades, weapons)
        if i > 0:
            # might need to make this more robust for spawn points
            # what is error handling and input checking
            try:
                pr = PropData(s[i+8:])
                props[pr.getHash()] = pr
            except:
                print("Invalid input: " + s)

        elif r > 0:
            try:
                toRemove = s[r+8:]
                del props[hash(toRemove)]
            except:
                print("Problem removing: " + s)

        elif z > 0:
            try:
                pr = PropData(s[z+5:])
                props[pr.getHash()] = pr
            except:
                print("Invalid input: " + s)



def process():
    """ Processes the stuff """
    global propsFormatted
    global debugData

    propsFormatted += words.CREATEPROPFUNCTION
    # propsFormatted += words.CREATEZIPLINEFUNCTION

    propsFormatted += words.HEADER
    for p in props.values():
        decoded = p.decode()
        propsFormatted += createEditorProp(decoded)
        if DEBUG:
            debugData += (decoded + "\n")

    propsFormatted += words.FOOTER


def export():
    """ Exports the props to a functional Apex Legends map
        (not complete yet) """
    printdict(props)
    fOutSqrrl.write(propsFormatted)
    if DEBUG:
        fOutDebug.write(debugData)

    print("--------------\nSuccess!")


def createEditorProp(propInfo: str) -> str:
    """ Creates a prop """
    return "    CreateEditorProp( " + propInfo + " )\n"


def createFRProp(propInfo: str) -> str:
    """ Creates a firing range prop """
    return "CreateFRProp( " + propInfo + " )\n"


# This is where I actually run the functions
handleInput()
process()
export()

fIn.close()
fOutSqrrl.close()
if DEBUG:
    fOutDebug.close()

