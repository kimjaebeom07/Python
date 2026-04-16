import random

def dice_game():
    while True:
        print("====== dice_game() 호출 ======")
        
        human = random.randint(1,6)
        com = random.randint(1,6)
        
        print("인간:", human)
        print("컴퓨터:", com)
        
        if human > com:
            print("인간승리")
        elif human < com:
            print("컴퓨터승리")
        else:
            print("무승부")
        
        print("====== dice_game() 복귀 ======")
        
        stop = input("중단할까요? Y/N: ")
        if stop.lower() == 'y':
            break

dice_game()