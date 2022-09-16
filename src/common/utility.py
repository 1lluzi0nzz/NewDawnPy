
class Utility:
    def readPos(str):
        str = str.split(",")
        return int(str[0]), int(str[1])

    def makePos(tup):
        return str(tup[0]) + "," + str(tup[1])