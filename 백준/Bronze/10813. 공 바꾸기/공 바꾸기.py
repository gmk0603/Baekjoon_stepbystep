N, M = map(int, input().split())
for input1 in range(N):
    globals()["a{}".format(input1+1)] = input1+1

for input2 in range(M):
    i, j = map(int, input().split())
    globals()["a{}".format(i)], globals()["a{}".format(j)] = globals()["a{}".format(j)], globals()["a{}".format(i)]
    
for input3 in range(N):
    print(globals()["a{}".format(input3+1)], end=' ')