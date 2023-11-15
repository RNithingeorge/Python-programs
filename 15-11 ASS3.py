lst = [3, 0, 1]

missing_number = set(range(len(lst) + 1)) - set(lst)

print(missing_number.pop())
