def freqDigit(numbers):
    res = ''
    for number in numbers:
        number = str(number)
        if len(number) != len(set(number)):
            res += number + ' '
    return res.strip()        

numbers = [2371, 4546, 742, 311]
print(freqDigit(numbers))

            