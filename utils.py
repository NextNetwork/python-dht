from random import randint
from hashlib import sha1


def entropy(len):
    strlist = []
    for i in range(len):
        strlist.append(chr(randint(0, 255)))
    s = ''.join(strlist)
    return s


def randomString(len):
    h = sha1()
    h.update(entropy(len))
    return h.digest()


def longInt(str):
    return long(str.encode('hex'), 16)


def quickSort(arr, start, end):
    if start < end:
        k = arr[end]
        i = start - 1

        for j in range(start, end):
            if arr[j] < k:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]

        arr[end], arr[i+1] = arr[i+1], arr[end]
        #print arr, i, end
        quickSort(arr, 0, i)
        quickSort(arr, i+1, end)

def randomHb():
    left = 100
    for i in range(10):
        min = 6
        max = 12

        if i != 9:
            if left-(10-i-1)*6 >= 12:
                #print "123 ", i, left,left-(10-i-1)*12
                min = left-(10-i-1)*12
                if min < 6:
                    min = 6
            if left-(10-i-1)*12 <= 6:
                print "456 ", i, left, left-(10-i-1)*6
                max = left-(10-i-1)*6
                if max > 12:
                    max = 12

            num = randint(min, max)
        else:
            num = left

        left -= num
        print num



if __name__ == '__main__':
    s = randomString(20)

    arr = [7, 4, 6, 8, 1, 3, 5]

    quickSort(arr, 0, len(arr)-1)

    randomHb()

    print arr
