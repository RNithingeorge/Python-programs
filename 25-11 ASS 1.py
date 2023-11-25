n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
col_sums = []
for j in range(len(matrix[0])):
  
    col_sum = 0

    for i in range(n):
       
        col_sum += matrix[i][j]
   
    col_sums.append(col_sum)

print(*col_sums)
