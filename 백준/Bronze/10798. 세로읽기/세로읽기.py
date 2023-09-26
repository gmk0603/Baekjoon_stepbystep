letter = [[' ']*15 for i in range(5)]
for i in range(5):
    word = input()
    if(len(word) > 15):
        print("처음부터 ㄱ")
        break
    for j in range(len(word)):
        letter[i][j] = word[j]
        
for i in range(15):
    for j in range(5):
        if (letter[j][i] == ' '):
            continue
        print(letter[j][i], end='')