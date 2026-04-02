n = int(input("숫자를 입력하시오: "))

result = 1
for i in range(n, 0, -1):
    result *= i

print(result)