import re
from collections import Counter

def word_count(phrase):
    phrase = phrase.lower().replace('_',' ')
    regex = re.compile(r'(\w+(\'\w)?)')
    words = [x[0] for x in regex.findall(phrase)]
    return Counter(words)
