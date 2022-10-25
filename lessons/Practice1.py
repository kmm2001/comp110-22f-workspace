
x : 3
def x(x=int) -> bool:
    "return bool"
    while x != 6:
        if x>0:
            return "A"
        elif x==3:
            return "B"

def y1(x = int, y = int) -> bool:
    "return bool"
    while x > y:
        if x > 3:
            x = x + 1
        else:
            return False
    return True