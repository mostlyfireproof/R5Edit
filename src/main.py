import argparse
from PropData import PropData

DEBUG = True

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
props = []
propsFormatted = ""


def printls(ls):
    """ Just prints each element of a list """
    for i in ls:
        print(i)


def handleInput():
    """ Reads in lines from the R5R console and finds prop data """
    for s in allCommands:
        i = s.find("[editor]")
        if i > 0:
            # might need to make this more robust for spawn points
            # what is error handling and input checking
            try:
                pr = PropData(s[i+8:])
                props.append(pr)
            except:
                print("Invalid input: " + s)


def process():
    """ Processes the stuff """
    global propsFormatted
    global debugData

    propsFormatted += "void function SpawnEditorProps()\n{\n" # Respawn braces are pain peko
    propsFormatted += "// Written by mostly fireproof. Let me know if there are any issues!\n"
    for p in props:
        decoded = p.decode()
        propsFormatted += createFRProp(decoded)
        if DEBUG:
            debugData += (decoded + "\n")

    propsFormatted += "}\n"  # closing brace, very important


def export():
    """ Exports the props to a functional Apex Legends map
        (not complete yet) """
    printls(props)
    fOutSqrrl.write(propsFormatted)
    if DEBUG:
        fOutDebug.write(debugData)


def createFRProp(propInfo: str) -> str:
    """ Creates a firing range prop """
    return "CreateFRProp (" + propInfo + " )\n"


# This is where I actually run the functions
handleInput()
process()
export()

fIn.close()
fOutSqrrl.close()
if DEBUG:
    fOutDebug.close()

