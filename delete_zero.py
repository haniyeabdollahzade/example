numbers = [1, 0, 4, 2, 0, 0, 6, 3, 0]
for i in numbers[:]:
    if i == 0:
        numbers.remove(i)
print(numbers)    