""" Test is the function is palindrom"""

def check(word):
    mylist = []
    for char in word:
        mylist.append(char)
        print(char)


    print(mylist)
    nl =[]
    for o in reversed(mylist):
        print(o)
        nl.append(o)


    return mylist==nl

print(check('nitin'))