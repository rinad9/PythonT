class chef:

    def make_chicken(self):
         print("The chef makes a chicken")
    
    def make_salad(self):
        print("The chef is making salad")
    
    # we will need to override this for the other chef
    def make_special_dish(self):
        print("The chef is making bbq ribs")
    
# class that modules a diffrente type of chef
# instead of normal chef ths is chinese chef
# we will creat a file called (chineseChef) for that class