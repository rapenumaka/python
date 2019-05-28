import argparse

parser = argparse.ArgumentParser(
    description = "This is sample"
)

print('Hello Parser')
parser.add_argument('-value1', action="store", type=str)
parser.add_argument('-value2', action="store")

args = parser.parse_args()
print(parser.parse_args())

print(args.value1)
print(args.value2)