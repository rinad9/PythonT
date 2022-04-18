# r : read \/
# w : write
# a : append
# r+ : read, write
emp_file = open("ReadFile.txt", "r")

# boolian to check if he file is readable or not
print(emp_file.readable())

# read the file
print(emp_file.read())

# read a line from the file 
# & if doubled it will print the first two lines
# with a space
print(emp_file.readline())
print(emp_file.readline())

# better function at reading lines in an array 
# or you can specify an index 
print(emp_file.readlines()[2])

# for loop to read the array using readlines()
for employee in emp_file.readlines():
    print(employee)

# a good practise is to close any file you open 
# after finishing 
emp_file.close()
