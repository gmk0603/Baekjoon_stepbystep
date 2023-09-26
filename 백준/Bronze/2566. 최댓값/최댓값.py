A = [[0]*9 for i in range(9)]

for i in range(9):
    x = list(map(int, input().split()))
    for j in range(9):
        A[i][j] = x[j]

result = 0
row = 0
column = 0
for i in range(9):
    for j in range(9):
        if(result <= A[i][j]):
            result = A[i][j]
            row = i+1
            column = j+1

print(result)
print(row, column)