x = []
for i in range(9):
    a = int(input())
    x.append(a)
print(max(x))
print(x.index(max(x))+1)