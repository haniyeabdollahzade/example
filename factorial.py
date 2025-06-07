def fact(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x

n = int(input("Enter a Number: "))
print(fact(n))
        