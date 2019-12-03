nums = [2,3,4,5,7,3,4]

my_list = []

for n in nums:
    my_list.append(n)

print(my_list)
print(id(nums))
print(id(nums))

val = [1 ,2 ,3, 4 ,5]

squars = [n*n for n in val]

""" Similar to map function"""
squars_revers = [n*n for n in reversed(val)]

print(val)
print(squars)
print(squars_revers)

"""" Similar to filter functions"""

evens = [n for n in val if n%2==0]
print(evens)

pairs_for = []
for char in 'abcd':
    for x in range(4):
        pairs_for.append((char,x))
print(pairs_for)


""" Nested For loopes"""
pairs_lc = [(letter, num) for letter in 'abcd' for num in range(4)]
print(pairs_lc)

seeks = [1,2,3,4,5,6,7,8,9,10]

"""
Use the list comprehension with generator
"""

my_gen = (n*n for n in seeks)
for i in my_gen:
    print(i)