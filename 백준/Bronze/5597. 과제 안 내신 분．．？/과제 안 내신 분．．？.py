n = []
for i in range(28):
    put = int(input())
    n.append(put)
output = []
for i in range(1, 31):
    if (i not in n):
        output.append(i)
print(min(output))
print(max(output))