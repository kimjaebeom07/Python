def getMoneyText(amount):
    units = ["", "십", "백", "천"]
    nums = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    result = ""
    
    s = str(amount)[::-1]
    
    for i in range(len(s)):
        if i >= 4:
            break
        
        n = int(s[i])
        if n != 0:
            result = nums[n] + units[i] + " " + result
    
    return result.strip()

money = int(input("1000 이하 입력: "))
print(getMoneyText(money))