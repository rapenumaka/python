class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current


nums = MyRange(1,10)

print(next(nums))
print(next(nums))
print(next(nums))

"""
Creating the generator function
Generator functions have inbuilt __iter__() and __next()__

"""

def my_range (start,end):
    current = start
    while current <= end :
        yield current
        current +=1


nums = my_range(1,20)

for n1 in nums:
    print(n1)