# Create a two list

zoo = ['lion', 'tiger','elephant','panda','jaguar','leopard','ostrich','zebra','donkey','goat']
aqua = ['whale','dolphin','shark','catfish','tutle']

# Access list items

print('Accessing the elements in the list')

print('zoo= ',zoo)
print('aqua= ',aqua )

# Change the value of a list item

print('changing the panda to red-panda')

zoo[3]= 'red-panda'
print(zoo)

# Check if the item is present in the list

i =zoo.count('deer')
print(i)

if 'boar' in zoo:
    print('boor is present in zoo')
else:
    print('boar is not present in zoo')

# Get the length of item

print('Getting the lenght of the list')
print(len(zoo))
print(len(aqua))

# Adding an element to the list at end

print('add the giraffe to the list zoo')
zoo.append('giraffe')

print(zoo)

# Add the item at specified index of list

print('Adding peacock at the index  number =3')
zoo.insert(3,'peacock')
print(zoo)


# Add a list with another list
print(' Add the  list aqua to list zoo ')
print('zoo= ',zoo)
print('aqua= ',aqua )

zoo.extend(aqua)
print('zoo after extend aqua= ',zoo)

# Remove an item from list

print('Removing red-panda from zoo')
zoo.remove('red-panda')
print(zoo)

# Remove an item at a specified index
print('removing the animal from index =5')
del zoo[5]
print(zoo)

# Empty the list
print('aqua =' ,aqua)
aqua.clear()
print('aqua =' ,aqua)

## Create a list using a list() constructor

word= 'animals'
my_l = list(word)

print(my_l)



# Clear the list

# Create a list using list constructor