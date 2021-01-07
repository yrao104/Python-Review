class CoolClass:
    #indicates that the body of the class was intentionally left blank -> so no error
    #class instance - object
    #type(object) prints out the class that the object is an instance of
    pass

#class variable - a variable that is the same for every instance of the class
class Musician:
    title = "Rockstar"

drummer = Musician()
print(drummer.title)
#prints "Rockstar"

#methods - functions defined as part of a class
class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

    pipi_pitbull = Dog()
    pipi_pitbull.time
