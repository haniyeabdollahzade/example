def game(n):
    list_num = []
    for i in n:
        list_num.append(i)

    maximum = 0
    for i in list_num:
        if i > maximum: 
            maximum = i
            
    minmum = float('inf')
    for i in list_num:
        if i < minmum:
            minmum = i
    return (maximum - minmum)           

n = input('Enter a Number: ')
x = list(map(int, n))
print('Differential:',game(x))
