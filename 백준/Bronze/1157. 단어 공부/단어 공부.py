word = input()
lowercase = []
uppercase = []
result = []
for i in range(65, 91):
    lowercase.append(word.count(chr(i)))
for j in range(97, 123):
    uppercase.append(word.count(chr(j)))
for k in range(len(uppercase)):
    result.append(lowercase[k] + uppercase[k])

resultmax = max(result)
resultmax_count = 0
i = 0
answer = ''
for l in range(65, 91):
    if(resultmax == result[i]):
        if(resultmax_count < 1):
            answer = chr(int(l))
            resultmax_count += 1
        else:
            answer = '?'
    i += 1
    
print(answer)