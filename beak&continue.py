
def iterate_with_conditions(nums):
    for num in nums:
        if num == 5:
            print("Found 5, continue!")
            continue
        if num == 8:
            print("Found 8, break!")
            break