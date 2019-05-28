
def calculateBmi(height,weight):
    return weight/(height*height)

weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))

print(calculateBmi(height,weight))