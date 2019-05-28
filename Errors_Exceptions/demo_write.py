file = open("demo.txt",'w')
file.write("This is second line \n")
file.close()

# this will replace the content of the file previously present

# To append the content to the file

file = open("demo.txt",'a')
file.write("This is third line ")
file.close()
