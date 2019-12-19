# Create a tuple

shop_cart = ('soap','shampoo','tea','pizza','coke')

soft_drink = ('pepsi','mountain-dew','coke','minute-maid')

# Access tuple items
print(shop_cart)

# Change tuple values
try:
    shop_cart[2]='coffee'
except TypeError:
    print('Tuple does not support changing the values')

# Loop though a tuple

for i in shop_cart:
    print(i)

# Check if a tuple item exists

if 'fruits' in shop_cart:
    print('fruits are present in shop_cart')
else:
    print('fruits are not present in shop_cart')

# Get length of a tuple

print(len(shop_cart))

# Delete a tuple
del soft_drink

print('you will get NameError if you try to access the object that is not present')


# Using a tuple() constructor to create a tuple

word ='apple'

apple_tuple = tuple(word)

print(apple_tuple)
