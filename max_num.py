def max_num(list_num):
    maximum = 0
    for i in list_num:
        if i > maximum:
            maximum = i
    return maximum        
        

numbers = input('Enter numbers: ').split(' ')
numbers = list(map(int, numbers))
print(max_num(numbers))
