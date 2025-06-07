import string

def get_letters_from_string(text):
    letters = []
    for char in text:
        if char.isalpha():
            letters.append(char)
    return '-'.join(letters)

text = "123abcABC!"
print(get_letters_from_string(text))   