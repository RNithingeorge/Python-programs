n = int(input()) 
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split())) 
l3 = [l1[i] + l2[i] for i in range(n)]
print(*l3, min(l3))
