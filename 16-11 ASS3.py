def find_missing_numbers(nums):
    n = len(nums)
    missing_numbers = []
    for i in range(1, n+1):
        if i not in nums:
            missing_numbers.append(i)
    return missing_numbers


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_missing_numbers(nums))
