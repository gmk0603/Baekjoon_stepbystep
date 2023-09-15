H, M = map(int, input().split())
time = int(input())
alterMinute = H*60+M+time
Hour = (alterMinute//60)%24
Minute = alterMinute%60
print(str(Hour) + ' ' + str(Minute))