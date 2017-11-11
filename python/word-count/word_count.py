def word_count(phrase):
    words = {}
    ranWord = ''

    for char in phrase:
        if char != ' ':
            ranWord = ranWord + char

        else:
            if ranWord not in words:
                words[ranWord] = 1
                ranWord = ''
            else:
                words[ranWord] += 1
                ranWord = ''
        print(ranWord)








    return words






#print(word_count('hello hello hi hey whats whats 1 1 1 2 3 3'))
