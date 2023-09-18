while True:
    try:
        A, B = map(int, input().split())
    except:
        break
    result = A + B
    print(result)