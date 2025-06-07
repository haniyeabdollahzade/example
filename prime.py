def is_prime(n):
    if n > 1 and n != 2:
        for i in range(2, n):
            if n % 2 == 0:
                return False
        return True
    else:
        return False    

def show_primes(start, end):
    for i in range(start, end+1):
        if is_prime(i):
            print(i, end=' ')
      

show_primes(2, 37)
