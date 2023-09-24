subRate = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

jihoonSubName = []
jihoonGrades = []
jihoonRate = []

for i in range(20):
    x, y, z = map(str, input().split())
    jihoonSubName.append(x)
    jihoonGrades.append(y)
    jihoonRate.append(z)

result = 0

for i in range(20):
    if(jihoonRate[i] == 'P'):
        continue
    else:
        result = result + (float(jihoonGrades[i]) * float(subRate[jihoonRate[i]]))

sumjihoonGrade = 0
for j in range(20):
    if(jihoonRate[j] == 'P'):
        continue
    sumjihoonGrade += float(jihoonGrades[j])
    
result = result / sumjihoonGrade
print(result)    