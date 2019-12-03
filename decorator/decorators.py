"""
Deoorators wrap a function and modify its behaviour in one way without
changing the source code of original function
"""

def decorator_func(myfunction):
    def wrapper_function():
        print('Modified through decorator')
        myfunction()

    return wrapper_function

def decorator_func2(myfunction):
    def wrapper_function():
        print('Second')
        myfunction()

    return wrapper_function


@decorator_func2
@decorator_func
def say():
    print('Hello Word')


say()

#ello = decorator_func(say)
#hello()
