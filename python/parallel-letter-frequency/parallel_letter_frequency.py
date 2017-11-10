#Create a function that returns the total frequency of each letter in a
#list of texts and that employs parallelism.

def calculate(text_input):
    d = {}
    i = 0
    for string in text_input:
        string = string.lower()
        for char in string:
            if char.isalpha():
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
    return d
