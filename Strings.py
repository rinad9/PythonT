ex_1 = 'This is a string. '
ex_2 = "This is also a string. "
# no deffrence between using either quouts
# better to use "" so you can use '' within string 
# without having to use escape seqence

ex_3 = '1984!'
ex_4 = "LiVe LONG and PRosPEr. "
ex_5 = "!@#$%^&*(){?|}{"
ex_6 = ""
ex_7 = "0123456" # index no
ex_8 = "orange"

# print by index
print(ex_8[2])
print("apple"[4])

# String slicing
ex_10 = "apricots"

# slicing from beginning to a certain point
print(ex_10[:3])
# from starting point to an ending point
print(ex_10[2:5])
# from a starting point all the way to the end of the string
print(ex_10[4:])

# Concatenation 
# = adding strings to each others
print("pecan" + " " + "pie")

concatenated = "R2" + "-" + "D2"
print(concatenated)
print(concatenated[3])
print(concatenated[1:4])

# effects of accessing by index and string slicing on variables
# they dont change and dont effect
unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)

# type() returns the type of a variable 
ex_11 = False
ex_12 = 29
ex_13 = 4.1352

print(type(ex_11))
print(type(ex_12))
print(type(ex_13))

# str() converts whatever in between the () to string
ex_14 = str(True)
ex_15 = str(5)
ex_16 = str(3.21)

print(type(ex_14))
print(type(ex_15))
print(type(ex_16))

# escape sequence
