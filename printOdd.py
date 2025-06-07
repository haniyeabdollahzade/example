def printOddNumber(n):
    odd_num = []
    for i in range(n+1):
        if i % 2 != 0:
            odd_num.append(i)
    return odd_num

n = int(input('Enter a Number: '))
print(sum(printOddNumber(n)))        
