A = []
while True:
    num = int(input())
    if (num < 0 or num > 1000):
        continue
    A.append(num)
    if(len(A) == 10):
        break
result = []
i = 0
while(len(result) < 10):
    num2 = A[i] % 42
    result.append(num2)
    i += 1
result2 = []
for i in range(10):
    if (result[i] not in result2):
        result2.append(result[i])
    else:
        continue

print(len(result2))