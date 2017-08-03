def newBitmapForm(self, bitmap):

def newBitmapFromString(self):

class Bitmap():
    def __init__(self, size, data):
        self.size = size
        self.data = data

        div, mod = size/8, size%8
