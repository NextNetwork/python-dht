from utils import *


def newBitmapForm(bitmap, size):
    newBitmap = Bitmap(size)

    if size > bitmap.size:
        size = bitmap.size

    div = bitmap.size/8

    strList = list(newBitmap.data)
    for i in range(0, div):
        strList[i] = bitmap.data[i]

    newBitmap.data = ''.join(strList)

    for i in range(div*8, size):
        if bitmap.bit(i) == 1:
            newBitmap.set(i)
    return newBitmap


def newBitmapFromString(str):
    bitmap = Bitmap(len(str))

    '''
    for i, c in enumerate(list(str)):
        bitmap.data[i] = c
    '''
    bitmap.data = str
    return bitmap

class Bitmap():
    def __init__(self, size):
        self.size = size
        self.data = ''

        self.div, self.mod = size/8, size % 8

        if self.mod > 0:
            self.div += 1

        for i in range(0, self.div):
            self.data += '\0'

    # retrun the bit at index
    def bit(self, index):
        div = index / 8  # the index of the node string
        mod = index % 8
        #print self.data[div]
        nodeIdDivInt = ord(self.data[div])
        # the high bit of nodeid & current prefixLen mod
        # when prifixlen = 0 ,then prifixlen mod = 0, highbit = 10000000 = 128 & nodeid[div]
        # the result = 1xxxxxxx then >> (7-mod) = the high bit of byte(char)
        result = ((1 << (7 - mod)) & nodeIdDivInt) >> (7 - mod)
        return result

    # sets the bit at index `index`.
    def set(self, index):
        div, mod = index / 8, index % 8

        shift = 1 << (7-mod)
        strList = list(self.data)
        strList[div] = chr(ord(strList[div]) | shift)
        self.data = ''.join(strList)

    def xor(self, bitmap):
        distance = longInt(self.data) ^ longInt(bitmap.data)
        return distance

    # Compare compares the prefixLen-prefix of two bitmap
    def compare(self, bitmap, prefixLen):
        div, mod = prefixLen/8, prefixLen % 8

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
