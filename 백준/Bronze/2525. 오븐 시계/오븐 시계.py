H, M = map(int, input().split())
utime = int(input())

if (utime >= 60):
    input_h = int(utime/60)
    input_m = int(utime%60)
else:
    input_h = 0
    input_m = utime
    
if (M + input_m >= 60):
    result_h = int(input_h + (M + input_m)/60 + H)
    result_m = int((M + input_m)%60)
    if(result_h >= 24):
        result_h -= 24
else:
    result_h = int(input_h + H)
    result_m = int(M + input_m)
    if(result_h >= 24):
        result_h -= 24
    
print(str(result_h) + ' ' + str(result_m))