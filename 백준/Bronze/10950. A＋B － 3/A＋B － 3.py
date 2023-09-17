T = int(input())
a = []
b = []
for i in range(T):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
for j in range(T):
    if (a[j]=='' or b[j]==''):
        continue
    result = a[j] + b[j]
    print(result)