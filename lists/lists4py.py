

### List in Python

vowels = ['a','e','i','o','u']

### Printig all the list

print('List of vowels {}'.format(vowels))

for v in vowels:
    print(v)

print('Reversing the list and printing them ')

for v in reversed(vowels):
    print(v)

### Getting the index of a value in list . If the value is not present it gives a ValueError

print('Find the index of e in vowels list')

print(' Index of e in vowels list :{}'.format(vowels.index('e')))

print('Raises a ValueError f we search for p in vowels list as it is not present')

another = [1, 2 ,('a','b'),9,'c']

print(another)

print('index of a,b in this list {}'.format(another.index(('a','b'))))

print("______________________________________________________________________________")

"""
Append methods appends the object at the end of the list

"""

animals = ['dog','cat','buffalo']
animals.append('pig')

print(animals)

print("You can also append a list to another list ")

wild_animals = ['tiger','zebra','lion']

animals.append(wild_animals)

print(animals)


print("______________________________________________________________________________")

"""
Extends - Use to entend the list with all the elements of list or set or tuples
"""

languages = ['english','spanish','italian','hebrew']
print(languages)
indian_languages = ['tamil','telugu','urdu','hindi']
print(indian_languages)

languages.extend(indian_languages)
print('Languages after extending witb other list: ', languages)


print("______________________________________________________________________________")

"""
Insert 
list.insert(index,element)
"""

a = [1,2,3,4]

print(a)

a.insert(2,9)
print(a)

a.insert(10,{0,8})
print(a)
print(a.__len__())

print("______________________________________________________________________________")

""""
remove()
"""

print(a)
a.remove(1)
print(a)

print("_______________________________________________________________________________")

"""
pop - Takes the argument of the index that needs to be popped off 
if no argument is supplied it removes the last element
"""

langs = ['python','c','c++','java','javascript']
x = langs.pop()

print(x)


"""
reverse() function does not return any value

"""
phones = ['samsung','lg','motorola','pixel','huewei']

print(phones)
phones.reverse()

print(phones)

print("_______________________________________________________________________________")

"""
sort(): just sorts but does not return anything

sorted() : it sorts and returns the list

list.sort(reverse =True) : This sorts in descending order


"""

arvind = ['a','r','v','i','n','d']

print(sorted(arvind,reverse=False))

print(sorted(arvind,reverse=True))

print("_______________________________________________________________________________")

rem = [1,2,3,4,5,6]
print(rem)
rem =[]
print(rem)
