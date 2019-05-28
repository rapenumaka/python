import re

string = "My name is John, Hi I'm John"

pattern =r"John"
newstring = re.sub(pattern,"Rob",string)
print(newstring)
