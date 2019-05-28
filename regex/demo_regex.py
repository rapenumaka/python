import re
# String contain eggs
pattern = r"eggs"

# to check if the strings starts with eggs
if re.match(pattern,'eggssss'):
    print('Match found')
else:
    print('No Match found')

# to search the string if the pattern is the part of string

if re.search(pattern,'bbeggssss'):
    print('Match found')
else:
    print('No Match found')


# using find all

if re.search(pattern,'bbeggssss'):
    print('Match found')
else:
    print('No Match found')
