n = int(input())
lst = list(map(int, input().split()))

duplicate_list = []
for i in lst:
    if lst.count(i) > 1 and i not in duplicate_list:
        duplicate_list.append(i)

for i in duplicate_list:
    print(i, end=' ')
