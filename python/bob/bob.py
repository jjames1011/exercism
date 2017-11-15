import re
def hey(phrase):
    phrase = re.sub('\s+','',phrase)
    if phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase == '':
        return 'Fine. Be that way!'
    elif phrase[len(phrase)-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
