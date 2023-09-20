N, M = map(int, input().split())
box = []
for i in range(N):
    box.append(i+1)
box2 = []
for j in range(M):
    x, y = map(int, input().split())
    for k in range(y, x-1, -1):
        box2.append(box[k-1])
    count = 0
    while(count < len(box2)):
        box[x-1] = box2[count]
        x += 1
        count += 1
    box2 = []
print(*box)