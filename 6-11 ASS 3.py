n = int(input())
count = 0
primes = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1
        primes.append(i)
print(f"{count}({','.join(map(str, primes))})")
