def second_maximum(lst):
    if len(lst) < 2:
        return None
    max1 = max2 = float('-inf')
    for num in lst:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max2

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(second_maximum(lst))
