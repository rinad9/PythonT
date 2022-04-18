from studentClass import student

# creating Object
# Object is an instantce of a class
# Class is like template
student1 = student("jim", "CS", 3.1, False)

# calling the function
student2 = student("Raoud", "art", 5, False)

print(student1.name)
print(student1.gpa)

print(student1.on_honor_roll())

print(student2.name)
print(student2.gpa)
print(student2.on_honor_roll())
