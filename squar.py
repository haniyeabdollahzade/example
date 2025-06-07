def square(n):
    print(n * '* ')    
    
    for k in range(n-2):
        print('* ' + (n-2) * '  ' + '* ')      
    print(n * '* ')


n = int(input('Enter square side lenght: '))
if n < 2:
    print('invalid')  

sq = square(n)