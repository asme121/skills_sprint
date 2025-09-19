#oop allows us to model real world entities in code

# key differences
#     encapsulation
#     objects
#     methods - functions 'belong' to specific objects
#
# oop pillars

class GradeBook:
    def __init__(self, grades):
        self.grades = grades

    def calculate_average(grades):
        total = sum(self.grades)
        return total / len(self.grades)

    def display_average(self):
        average = self.calculate_average()
        print('The average is', average)

def main():
    #create an instance of the gradebook class
    gradebook = GradeBook([85,90,78,92,99, 100])

    #use the objects methods
    gradebook.display_average()


main()

# main terms for us to understand to effectively begin modelling objects and data...
    # the class - this is the entity we are modelling (e.g. the Car, the Animal, the Person, the House)

    # the object - this is the instance of the class/instance, which has data and behaviours attached to it (e.g. the BMW, the Dog, the Sam)

    # the attribute - this is the info, or the data, that relates to the object... on the class we denote what data is related to the entity we are modelling... on the object we assign actual value to these data points

    # the methods - this is the behaviour / the things it can do, on the class we define the details of this behaviour (the functionality)

    # the constructor - this is a special method which sets our data to the objects when instantiated


#oop pillars
#abstraction - conventions and behaviours that we want to adhere to in our code. hide implementations details and
# show only essential features. users dont need to know how it works, just how to use
#achieved in python via abstract base classes


#encapsulation - bundling data and the methods that operate on the data. control over the data/attriubtes
# can only be updated from within the class i.e. through methods like setters. achieved in python using public(everywhere), protected( child class (_) ) and private ( this class only (__) )

#polymorphism - same method name can behave differently depending on  the object. achieved in python using method overriding

#inheritance - allows a child class to reuse and extend functionality from another class (parent)

#in python a child class inherits using parenthesis

