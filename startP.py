import re

def startp(txt):
    p_word = []
    words = txt.split()
    for word in words:
        if re.match(r"^p", word, re.IGNORECASE):
            p_word.append(word)
    return p_word


txt = "Python is a popular programming language"
print(startp(txt))