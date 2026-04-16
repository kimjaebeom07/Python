def getIntRange(a, b, msg):
    while True:
        n = int(input(msg))
        if a <= n <= b:
            return n

month = getIntRange(1,12,"월: ")
day = getIntRange(1,31,"일: ")
print(f"{month}월 {day}일")