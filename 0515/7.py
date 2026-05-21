from random import randint

class Dice :

    def __init__(Self, x, y) :
        self._x = x
        self._y = y
        self._size = 30
        self._value = 1

            def read_dice(Self) :
                return self._value

            def print_dice(Self) :
                print("주사위의 값=", self._value)

            def roll_dice(Self) :
                self._value = randint(1, 6)

d = Dice(100, 100)
d.roll_dice()
d.print_dice()