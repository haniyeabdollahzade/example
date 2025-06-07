def palindrom(txt):
    words = txt.split()
    palindrom = []

    for word in words:
        #clean_word = ''.join(char.lower() for char in word if char.isalpha())
        clean_word = ''
        for char in word:
            if char.isalpha():
                clean_word += char.lower()
        if clean_word == clean_word[::-1]:
            palindrom.append(clean_word)
    return palindrom                          
            


txt = "At noon the sun is above  our eye level"
print(palindrom(txt))
