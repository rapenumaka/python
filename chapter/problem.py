from math import hypot

def calculate(x1,y1,x2,y2):
    return hypot(x2-x1, y2-y1)

print(str(calculate(0,0,-10,10)))