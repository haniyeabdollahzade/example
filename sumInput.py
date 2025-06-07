n = input()

def sumOfNumbers(n):
    try:
        float(n)
        return True
    except:
        return False
    
num_str = list(filter(sumOfNumbers, n))
if num_str:
    numbers = map(float, num_str)
    print(sum(numbers))    