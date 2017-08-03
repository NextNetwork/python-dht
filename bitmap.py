def newBitmapForm(self, bitmap):

def newBitmapFromString(self, s):

class Bitmap():
    def __init__(self, size):
        self.size = size
        self.data = ''

        div, mod = size/8, size%8

        if mod > 0:
            div++

        for i in range (0, div):
            self.data += '\0'

    #retrun the bit at index
    def bit(self, index):
        div = prefixLen / 8  # the index of the node string
        mod = prefixLen % 8
        nodeIdDivInt = int(self.data[div])
        # the high bit of nodeid & current prefixLen mod
        # when prifixlen = 0 ,then prifixlen mod = 0, highbit = 1000000 = 128 & nodeid[div]
        # the result = 1xxxxxx then >> (7-mod) = the high bit of byte(char)
        result = ((1 << (7 - mod)) & nodeIdDivInt) >> (7 - mod)
        return result

    def set(self, index, bit):
