
"""
List is iterable because it can be iterated
Tuple,String

List is iterable but not an iterator

"""
nums = [1,2,3]

for n in nums:
    print(n)

i_nums = nums.__iter__()

i_neat = iter(nums)
print(next(i_nums))

"""
Note that i_nums and i_neat will have __next__() method
"""
print(dir(i_neat))
print(next(i_neat))
print(next(i_neat))
print(next(i_neat))
print(next(i_neat))

"""
If something is iterable it should have 

__iter__()
iter is an object that knows the state
it also know knows what is next well 
"""
