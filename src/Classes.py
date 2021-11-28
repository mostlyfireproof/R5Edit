class Vec3:
    """ Represents a vector with 3 values. Can be used for position or angles. """
    def __init__(self, x, y=-1, z=-1):
        if y == z == -1:  # case when constructed with a single string
            arr = x.replace('<', '').replace('>', '').replace('\n', '').split(',')
            self.x = arr[0]
            self.y = arr[1]
            self.z = arr[2]
        else:  # case when constructed with 3 values
            self.x = x
            self.y = y
            self.z = z

    def to_string(self) -> str:
        """ Converts a vector to a string """
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ">"


class PropData:
    """ Represents the data for a prop in Apex Legends"""
    def __init__(self, string: str):
        self.myHash = hash(string)

        cutoff = string.find(";")
        mdl = string[:cutoff]
        string = string[cutoff + 1:]

        cutoff = string.find(";")
        pos = string[:cutoff]
        string = string[cutoff + 1:]

        cutoff = string.find(";")
        angle = string[:cutoff]
        string = string[cutoff + 1:]

        # handles realm and maintains backwards compatibility
        realm = "-1"
        cutoff = string.find(";")
        if cutoff > -1:
            realm = string[:cutoff]

        self.model = mdl
        self.position = pos.split(",")
        self.angles = angle.split(",")
        self.realm = realm

    def decode(self) -> str:
        """ Turns the data in the class in to a string that the engine can take """
        # takes the data from the object
        output = "$\"" + self.model + "\", " + self.devector(self.position) + ", " + self.devector(self.angles)
        # adds on extra data for mantle (?) and draw distance
        output += ", true, 8000"
        output += ", " + self.realm
        return output

    def devector(self, string: list) -> str:
        """ Turns a stringified vector back in to numbers """
        output = "<" + string[0] + "," + string[1] + "," + string[2] + ">"
        return output

    def getHash(self) -> int:
        """ Just returns the hash, makes it easier to compare props """
        return self.myHash


class Zipline(PropData):
    """ Represents the data for a zipline """
    def __init__(self, start: str, end: str):
        self.myHash = hash(start + end)

        self.start = Vec3(start)
        self.end = Vec3(end)

    def decode(self) -> str:
        return self.start.to_string() + ", " + self.end.to_string()
