n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
col_max = []
for j in range(len(matrix[0])):
    col_maxi = matrix[0][j]
  
    for i in range(1, n):
     
        if matrix[i][j] > col_maxi:
       
            col_maxi = matrix[i][j]

    col_max.append(col_maxi)

print(*col_max)
