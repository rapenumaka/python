def function1(a,b):
    try :
        print(a/b)
    except ZeroDivisionError :
        print('the denominator should not be zero')
    finally:
        print ('This block will be executed finally at all times even if the exception is not caught')

function1(2,0)