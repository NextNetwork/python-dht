from random import randint
def randomString(len):
    strlist = []
    for i in range(len):
        print strlist
        strlist.append(chr(randint(0, 255)))
    s = ''.join(strlist)
    return s

def longInt(str):
    return long(str.encode('hex'), 16)

if __name__ == '__main__':
    s = randomString(20)
