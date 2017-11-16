from collections import OrderedDict
def decode(string):
    uncompressed_Str = ''



def encode(string):
    d = OrderedDict.fromkeys(string,0)
    compressedString = ''

    for char in string:
        d[char] += 1

    for key, value in d.items():
        if value > 1:
            compressedString += str(value) + key
        else:
            compressedString += key
    return compressedString

print(encode('hellloooo'))
