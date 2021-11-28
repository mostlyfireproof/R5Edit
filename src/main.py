import argparse
from Classes import PropData
from Classes import Zipline

# Sets up argparse
parser = argparse.ArgumentParser(description='Creates a map from prop data')
parser.add_argument('input', metavar='input', type=str, help='R5R log output in a file')
parser.add_argument('output', metavar='output', type=str, default="map.gnut", help='The name of the map')

args = parser.parse_args()

# Opens files
fIn = open(args.input, "r")
fOutSqrrl = open(args.output, "w")

allCommands = fIn.readlines()
props = {}
propsFormatted = ""

HEADER = '''void function SpawnEditorProps()
{
    // Written by mostly fireproof. Let me know if there are any issues!
    printl("---- NEW EDITOR DATA ----")
'''

FOOTER = '''
}
'''

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
        if i.find("NEW EDITOR DATA") > -1:
            lastBootUp = allCommands.index(i)
            break
    print("LINE: " + str(lastBootUp))

    current_zip = ""

    # process every command
    for s in allCommands[lastBootUp:]:
        i = s.find("[editor]")      # placing objects
        r = s.find("[delete]")      # deleting objects
        z = s.find("[zipline]")         # placing ziplines
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
                if s[z + 10] == "1":
                    current_zip = s[z+12:]
                else:
                    zip = Zipline(current_zip, s[z+12:])
                    props[zip.getHash()] = zip
            except:
                print("Invalid input: " + s)



def process():
    """ Processes the stuff """
    global propsFormatted

    propsFormatted += HEADER
    for p in props.values():
        decoded = p.decode()
        if isinstance(p, Zipline):
            propsFormatted += createZip(decoded)
        else:
            propsFormatted += createEditorProp(decoded)

    propsFormatted += FOOTER


def export():
    """ Exports the props to a function that can be placed in an Apex Legends map """
    printdict(props)
    fOutSqrrl.write(propsFormatted)

    print("--------------\nSuccess!")


def createEditorProp(propInfo: str) -> str:
    """ Creates a prop """
    return "    CreateEditorProp( " + propInfo + " )\n"


def createZip(zipInfo: str) -> str:
    """ Creates a zipline """
    return "    CreateEditorZipline( " + zipInfo + " )\n"


# This is where I actually run the functions
handleInput()
process()
export()

fIn.close()
fOutSqrrl.close()
