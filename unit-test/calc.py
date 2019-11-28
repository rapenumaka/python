def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y ==0:
        raise ValueError('The denominator cant be zero')
    return x/y

print(__name__)