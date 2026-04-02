user_id = ""
password = ""

while True:
    user_id = input("아이디를 입력하시오: ")
    password = input("암호를 입력하시오: ")

    if user_id == "admin" and password == "pythonisfun":
        print("로그인 성공")
        break
    else:
        print("아이디 또는 암호가 올바르지 않습니다.")