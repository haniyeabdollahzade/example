def replacee(nums):
    num = []
    for i in nums:
        if i % 2 != 0:
            num.append(-1)
        else: 
            num.append(i)
    return num        

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(replacee(nums))        