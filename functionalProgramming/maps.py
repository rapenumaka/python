def add(x):
    return x+2
mylist = [10,20,30,40,50]

result = list(map(add,mylist))

result1 = list(map(lambda x:x+2,mylist))

print(result)

print(result1)