'''
n=int(input())#6
l=list(map(int,input().split()))#4 5 6 7 8 2
k=int(input())#3
l=list(set(l))#for removing duplicates 4 5 6  2
for i in range(1,k):#i=1<1
    m=min(l)#7
    l.remove(m)
print(min(l))#6
'''
def k_min(lst, k):
    return sorted(lst)[:k][-1]

lst = list(map(int, input().split()))
k = int(input())
print(k_min(lst, k))
