def deletezero(numbers):
    numbers = str(numbers)
    numbers = numbers.replace('0', '')
    return numbers.strip()


numbers = 100025
print(deletezero(numbers))