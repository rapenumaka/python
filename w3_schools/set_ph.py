"""
Sets are lists but they will not contain similar elements (no repetation)
Set are not ordered
"""

# Create a set

es = {'apple','dell','hp','micromax'}

# Loop through a set

for e in es :
    print(e)

# Check if a item exists in set

print('check if asus is present')

if 'asus' in es:
    print('Asus is present in the set = es')
else:
    print('Asus is not present in the set')

# Add a item to set

es.add('asus')
print(es)

# Add multiple items to set

ns = {'pixel','samsung','sony','asus'}
es.update(ns)
print(es)



# Get the length

print(len(es))

# Remove an item in a set

es.remove('asus')
print(es)

# Remove an item in a set usin discard method

es.discard('pixel')
print(es)

# Remove the last item in a set using the pop method

print(es.pop())


# Empty a set

es.clear()
print(es)
# Delete a set
try:
    del es
except NameError:
    print('the set es has been removed')


## Using the set() constructor to create a set
word = 'apple'
apple_word = set(word)
print(apple_word)

