class PropData:
    ''' Represents the data for a prop in Apex Legends'''
    def __init__(self, string:str):
        cutoff = string.find(";")
        mdl = string[:cutoff]
        string = string[cutoff + 1:]

        cutoff = string.find(";")
        pos = string[:cutoff]
        string = string[cutoff + 1:]

        cutoff = string.find(";")
        angle = string[:cutoff]
        string = string[cutoff + 1:]

        self.model = mdl
        self.position = pos.split(",")
        self.angles = angle.split(",")

    def decode(self) -> str:
        """ Turns the data in the class in to a string that the engine can take """
        # takes the data from the object
        output = "$\"" + self.model + "\", " + self.devector(self.position) + ", " + self.devector(self.angles)
        # adds on extra data for mantle (?) and draw distance
        output += ", true, 8000"
        return output

    def devector(self, string: list) -> str:
        """ Turns a stringified vector back in to numbers """
        output = "<" + string[0] + "," + string[1] + "," + string[2] + ">"
        return output
