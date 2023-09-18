import sys
T = int(sys.stdin.readline().rstrip())
x = []
y = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    x.append(A)
    y.append(B)
for j in range(T):
    result = x[j] + y[j]
    print(result)