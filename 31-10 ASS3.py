n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, 5+1):
        print(i+j-1+(j-1), end=" ")
    print()
