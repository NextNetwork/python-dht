from utils import *
def newBitmapForm(self, bitmap, size):
    newBitmap = Bitmap(size)

    div = bitmap.size/8

    for i in range(0, div):
        newBitmap.data[i] = bitmap.data[i]

    for i in range(div*8, size):
        if bitmap.bit(i) == 1:
            newBitmap.set(i)
    return newBitmap

def newBitmapFromString(self, str):
    bitmap = Bitmap(len(str))

    for i, c in enumerate(list(str)):
        bitmap.data[i] = c
    return bitmap

class Bitmap():
    def __init__(self, size):
        self.size = size
        self.data = ''

        self.div, self.mod = size/8, size%8

        if self.mod > 0:
            self.div += 1

        for i in range (0, self.div):
            self.data += '\0'

    #retrun the bit at index
    def bit(self, index):
        div = index / 8  # the index of the node string
        mod = index % 8
        nodeIdDivInt = int(self.data[div])
        # the high bit of nodeid & current prefixLen mod
        # when prifixlen = 0 ,then prifixlen mod = 0, highbit = 10000000 = 128 & nodeid[div]
        # the result = 1xxxxxxx then >> (7-mod) = the high bit of byte(char)
        result = ((1 << (7 - mod)) & nodeIdDivInt) >> (7 - mod)
        return result

    #sets the bit at index `index`.
    def set(self, index):
        div, mod = index / 8, index % 8

        shift = 1 << (7-mod)
        self.data[div] |= shift

    def xor(self, bitmap):
        distance = longInt(self.data) ^ longInt(bitmap.data)
        return distance

    #Compare compares the prefixLen-prefix of two bitmap
    def compare(self, bitmap, prefixLen):
        div, mod = prefixLen/8, prefixLen%8

        for i in range(0, div):
            if self.data[div] != bitmap.data[div]:
                return 0

        for i in range(div*8, prefixLen):
            mybit = self.bit(i)
            otherbit = self.bit(i)
            if mybit != otherbit:
                return 0
        return 1

    # the low bit of char
    def getBit(self, index):
        div, mod = index / 8, index % 8
        result = self.data[div] & (1 << mod)

        return result
