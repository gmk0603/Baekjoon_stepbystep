chess = list(map(int, input().split()))
chess_box = [1, 1, 2, 2, 2, 8]
result = []
for i in range(6):
    if (chess[i] != chess_box[i]):
        result.append(chess_box[i] - chess[i])
    else:
        result.append(0)
print(*result)