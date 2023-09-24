word = input()
result = 0
front = 0
for i in range(int(len(word))):
    if(word[front] == word[-1-i]):
        result = 1
        front += 1
    else:
        result = 0
        break
print(result)