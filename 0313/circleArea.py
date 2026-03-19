import math

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = float(input("반지름을 입력하세요: "))
    area = circle_area(r)
    print(f"원의 면적은 {area:.2f}입니다.")