def numberPalindrom(nums):
    for num in nums:
        clean_num = str(num)
        if clean_num == clean_num[::-1]:
            print(clean_num, end=' ')


numbers = [22, 123, 303, 151, 415]
print(numberPalindrom(numbers))



