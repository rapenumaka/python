def add10(x):
    return x+10

def twiceFunc(func, x):
    return func(func(x))

y = twiceFunc(add10,2)

print(y)
