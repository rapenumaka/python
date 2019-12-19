
s = 'this is a long interesting string'

# Get the character at position 1 in the string

print(s[1])

# Substring. Get the character from position2 to position 5

print(s[2:5])

#
m = 'name '

# Remove the whitespaces at the beginning or ending of the string

print(len(m))

print(m.strip())

# Convert the string to lower case

print(m.upper())
print(m.lower())

m = 'name'
new = m.replace('n','l')
print(new)

# Split the string into substrings

batch = 'the | fox |is |climbing| up'
bl = batch.split('|')
print(bl)

## Palindrom in Python
a = 'nitin'
b2 = (list(a))
b3 = []

for a in reversed(b2):
    b3.append(a)
b4 = [a for a in reversed(b2)]
print(b2==b3)
print(b4==b3)


