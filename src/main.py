from PropData import PropData

# argparse goes here

DEBUG = True


def printls(ll):
    for i in ll:
        print(i)


fIn = open("../examples/sample1.txt", "r")
fOutSqrrl = open("../examples/out1.gnut", "w")

debugData = ""
# print to a debug file while i'm testing
if DEBUG:
    fOutDebug = open("../examples/out1.txt", "w")

allCommands = fIn.readlines()
props = []
propsFormatted = ""


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
    for p in props:
        decoded = p.decode()
        propsFormatted += createFRProp(decoded)
        if DEBUG:
            debugData += (decoded + "\n")

    propsFormatted += "}\n" # closing brace, very important


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


handleInput()
process()
export()

fIn.close()
fOutSqrrl.close()
if DEBUG:
    fOutDebug.close()

