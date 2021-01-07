#constructors - methods used to prepare an object being instantiated
#in Python, constructors usually refer to the _int_() method

class Shouter:
    def __init__(self, phrase):
        #make sure phrase is a string
        if type(phrase) == str:

            #then shout it out
            print(phrase.upper())

shout1 = Shouter("shout")
#prints "SHOUT"

shout2 = Shouter("shout")
#prints "SHOUT"

shout3 = Shouter("let it all out")
#prints "LET IT ALL OUT"
