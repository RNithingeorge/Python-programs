n = int(input())
lst = list(map(int, input().split()))

unique_set = set(lst)
duplicate_count = len(lst) - len(unique_set)

print(duplicate_count)
