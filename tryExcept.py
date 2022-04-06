# asking the user to enter a number but we try 
# entering a text instead

# value = 10/0 THAT WILLTHROW AN ERROR

try:
# when added here it will be handeled by the except
    value = 10/0 
    number = int(input("enter a number: "))
    print(number)   

 
# (Except:) on its own is too broad exception clause, 
# and that means it will handle any error in the program
# if we wanted to make diffrent error capture 
# we add except and specfy 
except ZeroDivisionError as err: 
    print(err)
except ValueError:
    print("invalid value")
