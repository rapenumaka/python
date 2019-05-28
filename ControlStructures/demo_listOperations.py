numbers = [1,1,1,1]
# How to insert values to List ,
# insert the value '5' at position 2, # this will replace the postion of 1 with 5

numbers[2] = 5
print(numbers)


new_number=[2.4,5,6]

# adding the two list.. joining the list

print(numbers + new_number)


print(numbers*3)

# check if the element exist in the list

fruits = ['apples', 'mango', 'peach']
print("grapes" in fruits) ## this will be false

print("apples" in fruits)  ## this will be true

print(numbers+fruits)

# appending an element into a list

basket = ['apples', 'grapes','cantolopes','water melons']
# adding banana to the basket at the last position

basket.append('bananas')
print(basket)

basket.append('oranges')
print(basket)

# Printing the size of the list
print(basket.__len__())

# insert the element at position without deleting the values already present there
# The size of the list increases and elements in the list shift to the next postion

basket.insert(1,"blackberry")

print(basket)

# Printing the size of the list
print(basket.__len__())

# Getting the index of a particular item present in the list

print('The index of blackberry in basket list', basket.index("blackberry"))

print(basket.index("Blueberry"))



