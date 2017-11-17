from collections import OrderedDict
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def decode(string):
    print(string)
    newStr = ''
    count = 0
    i = 0
    for char in string:
        if char.isalpha():
            newStr += char
        elif RepresentsInt(char) and string[i+1].isalpha():
            count = int(char)-1
            newStr += string[i+1] * count
        elif RepresentsInt(char) and RepresentsInt(string[i+1]):
            count = int(char + string[i+1])-1
            newStr += string[i+2] * count
        i += 1
    return newStr


def encode(string):
    d = OrderedDict.fromkeys(string,0)
    print(d)
    compressedString = ''
    for char in string:
        d[char] += 1
    for key, value in d.items():
        if value > 1:
            compressedString += str(value) + key
        else:
            compressedString += key
    return compressedString

print(encode('  hsqq qww  '))
#print(encode('Helloooo'))

print(decode('12He2l4ohe'))
