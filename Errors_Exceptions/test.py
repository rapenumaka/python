import sys

try :
    print('This will be printed ')
    sys.exit(0)
    f = open('curruptfile.txt')

    print('This will not be printed ')

except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
finally:
    print("Executing Finally...")

print('End of program')