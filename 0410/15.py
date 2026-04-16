def checkPass(p):
    if len(p) < 8: return False
    has_upper = any(c.isupper() for c in p)
    has_lower = any(c.islower() for c in p)
    has_digit = any(c.isdigit() for c in p)
    return has_upper and has_lower and has_digit

p = input("비밀번호: ")
print("사용 가능" if checkPass(p) else "사용 불가")