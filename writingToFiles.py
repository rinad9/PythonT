# r : read
# w : write \/ overwriting everything OR create new file
# a : append \/ adding at the end of the file
# r+ : read, write
emp_file = open("ReadFile.txt", "a")

# Overwriting everything
emp_file = open("ReadFile.txt", "w")

# Create new file
emp_file = open("ReadFile1.txt", "w")

# Creating HTML file
emp1_file = open("index.html", "w")

# 1- writing to a file but  
# you have to be carefull because running twice will add again
# 2- if you have a line previosly 
# or the line will be added to the existent one
# 3- adding escape character \n for new line

emp_file.write("\nKelly - Customer Service")

emp1_file.write("<p>This is HTML</p>")


# a good practise isto close any file you open 
# after finishing 
emp_file.close()
