import sys
introduce = list(map(str, sys.stdin.readlines()))
for i in range(len(introduce)):
    print(introduce[i].strip())