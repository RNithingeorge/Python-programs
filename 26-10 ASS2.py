n = int(input("Enter a number: "))
res = 0
temp = n
while temp > 0:
    r= temp % 10
    res += r ** 3
    temp //= 10
if n == res:
     print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")



