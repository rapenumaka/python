# Create two variables - your name and age

name = 'Raja Penumaka'
age = 32

# Function that prints name and age

def printMyDetails():
    print('My name is '+name+'and i am '+str(age)+' years old')

printMyDetails()


# Calcuate decade you have lived on the earth
print("Enter the year you are born")
age = input();

present_year = 2018

difference = present_year-int(age)

print(str(difference))
decades = difference / 10

print('It has been '+str(decades)+ " decades since you have been born")