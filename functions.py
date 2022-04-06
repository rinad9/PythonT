# Functions must always all be lower case
# Function creation -- body should be indented
def sayhi(name, age):
    print("Hello " + name +" you are " + str(age))

# Calling the function
print("Top")
sayhi("Mike", 37)
sayhi("Steve", 60)
print("Bottom")

# Return statment
def cube(num):
    num*num*num

def cube1(num):
    return num*num*num
    print("code")
    
print(cube(3))
print(cube1(4))

# If statements
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male or tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You neither male nor tall or both")


# If statments & comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(1, 2, 3))