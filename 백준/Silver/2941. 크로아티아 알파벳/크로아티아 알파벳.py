word = input()
Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
count2 = 0
result = int(len(word))
# 2단어 체크
while(count < len(word)-1):
    check = word[count:count+2]
    for croatia in Croatia:
        if(check == croatia):
            result -= 1
    count += 1

# 3단어 체크
while(count2 < len(word)-2):
    check = word[count2:count2+3]
    for croatia in Croatia:
        if(check == croatia):
            result -=1
    count2 += 1
print(result)