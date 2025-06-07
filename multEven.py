def multEvenNumber(nums):
    multNums = 1
    for num in nums:
        if num % 2 == 0:
            multNums *= num
    return multNums


numbers = [3, 2, 6, 7, 4]
print(multEvenNumber(numbers))

