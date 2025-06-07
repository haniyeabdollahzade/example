#list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#n = len(list_number)
#print(sum(list_number) // n)

def calculate(list_number):
    n = len(list_number)
    return sum(list_number) // n

numbers = input('Enter numbers: ').split(' ')
numbers = list(map(int, numbers))
print(calculate(numbers))    
