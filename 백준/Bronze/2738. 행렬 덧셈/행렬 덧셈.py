N, M = map(int, input().split())

A = [[0]*M for i in range(N)]
B = [[0]*M for i in range(N)]

for i in range(N):
    x = list(map(int, input().split()))
    for j in range(M):
        A[i][j] = x[j]
        
for i in range(N):
    x = list(map(int, input().split()))
    for j in range(M):
        B[i][j] = x[j]
                    
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()