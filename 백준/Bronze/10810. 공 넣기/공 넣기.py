N, M = map(int, input().split())
for input1 in range(N):
    globals()["a{}".format(input1+1)] = 0

result = []

for input2 in range(M):
    i, j, k = map(int, input().split())
    while(i<=j):
        globals()["a{}".format(i)] = k
        i+=1

for input3 in range(N):
    result.append(globals()["a{}".format(input3+1)])
    print(result[input3], end=' ')