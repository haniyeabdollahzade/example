def triangle(n):
    for i in range(1, n+1):
        x = n - i  # space
        print((x * ' ') + str(i) * i)


n = int(input('Enter triangle lenght: '))
T = triangle(n)       
