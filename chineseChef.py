from chefClass import chef
class ChineseChef(chef):

    def make_fried_rice(self):
        print("The chef makes fried rice")

    # override the spcecial dish of the normal chef
    def make_special_dish(self):
        print("The chef makes orange chicken")