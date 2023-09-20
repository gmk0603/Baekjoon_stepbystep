N = int(input())
test = []
score = list(map(int, input().split()))
M = max(score)
for j in range(N):
    score[j] = score[j]/M*100
print(sum(score)/len(score))