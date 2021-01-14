class Employee():
    def __init__(self, name):
        self.name = name

argus = Employee("Argus Filch")
print(argus)

#duner method _repr_() can be used to tell Python what we want the string representation of the class to be
#can have only one parameter, self, and must return a string