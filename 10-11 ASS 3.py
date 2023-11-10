n=int(input())
while n>9:
    s=0
    while n!=0:
        r=n%10
        s=s+r*r
        n=n//10
    n=s
if n==1 or n==7:
    print('happy number')
else:
    print('Not a happy number')
