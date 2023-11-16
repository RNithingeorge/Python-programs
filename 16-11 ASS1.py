
def second_minimum(lst):
    if len(lst) < 2:
        return None
    min1 = min2 = float('inf')
    for num in lst:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num
    return min2

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(second_minimum(lst)) 
