def sumOfEvenNumber(n):
    sum_num = []
    for i in range(n + 1):
        if i % 2 == 0:
            sum_num.append(i)
    return sum_num

n = int(input("Enter a Number: ")  )
number = sumOfEvenNumber(n)
print(sum(number))         
