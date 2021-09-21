class PropData:
    ''' Represents the data for a prop in Apex Legends'''
    def __init__(self, string):
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
