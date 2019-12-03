

def encounter_exception(divide_finction):
    def wrap_function(a,b):
        print("value of a = {} , b = {}".format(a,b))
        if b == 0:
            raise ZeroDivisionError(" Value of b should not be zero")
            return
        return divide_finction(a,b)
    return wrap_function



@encounter_exception
def divide(x,y):
    return x/y

print(divide(2,3))