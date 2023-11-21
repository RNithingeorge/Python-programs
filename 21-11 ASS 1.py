n = int(input())
lst = list(map(int, input().split()))

even = [ ]
odd = [ ]

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even, odd)
