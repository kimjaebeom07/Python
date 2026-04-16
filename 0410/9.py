def main():
    width = int(input("너비를 입력하시오 : "))
    height = int(input("높이를 입력하시오 : "))
    result = get_rect_area(width, height)
    print("사각형의 넓이 :", result)

main()