def testPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(2, 101):
    if testPrime(i):
        print(i, end=" ")