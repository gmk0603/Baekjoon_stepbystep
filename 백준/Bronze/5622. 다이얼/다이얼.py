word = list(input())
time = 0
for i in range(len(word)):
    if(87 <= ord(word[i]) <= 90):
        time += 10
    elif(84 <= ord(word[i]) <= 86):
        time += 9
    elif(80 <= ord(word[i]) <= 83):
        time += 8
    elif(77 <= ord(word[i]) <= 79):
        time += 7
    elif(74 <= ord(word[i]) <= 76):
        time += 6
    elif(71 <= ord(word[i]) <= 73):
        time += 5
    elif(68 <= ord(word[i]) <= 70):
        time += 4
    elif(65 <= ord(word[i]) <= 67):
        time += 3
print(time)