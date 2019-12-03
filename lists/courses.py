courses = ['History','Science','Maths','English']

## Accessing the list through the index
print(courses.__len__())
print(courses[-1])

## Access the first two values [0:2] 0 is inclusive and 2 is exclusive

print(courses[0:2])

print(courses[:2])

print(courses[1:])

courses[0] ='Arts'

print(courses)