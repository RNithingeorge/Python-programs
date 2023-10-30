def is_perfect(n):
    div= [ ]
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    return sum(div) == n

t = int(input())
for i in range(t):
    num = int(input())
    if is_perfect(num):
        print("PERFECT")
    else:
        print("NOT PERFECT")
