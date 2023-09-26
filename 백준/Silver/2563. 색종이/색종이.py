draw = [[0]*100 for _ in range(100)]

N = int(input())
for i in range(N):
    x, y = list(map(int, input().split()))
    
    for j in range(x, x+10):
        for k in range(y, y+10):
            draw[j][k] = 1
            
result = 0
for i in range(100):
    for j in range(100):
        if(draw[i][j] == 1):
            result += 1
    
print(result)