def calc(a, b):
    return a+b, a-b, a*b, a/b

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))

print(calc(a,b))