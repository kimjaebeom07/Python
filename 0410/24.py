def sqrt_newton(x):
    g = x / 2  # 초기 추정값
    
    while True:
        new_g = (g + x / g) / 2
        if abs(new_g - g) < 0.0001:
            return new_g
        g = new_g

n = float(input("숫자 입력: "))
print(sqrt_newton(n))