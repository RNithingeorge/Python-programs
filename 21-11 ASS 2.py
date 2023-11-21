lst = list(map(int, input().split()))

new_lst = [ ]

for i in lst:
    new_lst.append(i)
    if i % 2 != 0:
        new_lst.append(i)

print(*new_lst)
