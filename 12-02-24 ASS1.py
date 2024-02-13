num = int(input())
n= num  
t= 0
while num > 0:
        r = num % 10
        t += r** 3
        num //= 10

if n == t:
    print(" Armstrong number")
else:
    print(" not an Armstrong number")
