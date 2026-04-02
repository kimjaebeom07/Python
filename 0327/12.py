import random

flag = True

while flag:
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    op = random.choice(['+', '-'])

    if op == '+':
        correct = x + y
    else:
        correct = x - y

    answer = int(input(f"{x} {op} {y} = "))

    if answer == correct:
        print("잘했어요!!")
        flag = False
    else:
        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")