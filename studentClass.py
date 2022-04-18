# Class is another data type that you can define its discriptions
from xml.etree.ElementPath import get_parent_map


class student:

    # initialize function : has the attributes of the subject
    # after calling the function it will be stored in those parameters
    def __init__(self, name, major, gpa, is_on_probation):

    # the actual object . name is = that you passed to the function above
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    
    # function
    def on_honor_roll(self):
    # reverring to actual stu gpa
        if self.gpa >= 3.5:
            return True
        else:
            return False





