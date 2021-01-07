#instance variables and class variables are both accessed similarly in Python
#if we try to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an Attribute Error

class NoCustomAttributes:
    pass

attributeless = NoCustomAttributes()

try:
    attributeless.fake_attrubyte
except AttributeError:
    print("This text gets printed!")

#hasattr() will return True if an object has a given attribute and False otherwise
    #hasattr(object, "attribute"):
        #object - the object we are test to see if it ahs a certain attribute
        #attribute - name of attribute we are checking to see if it exists
#getattr() - to get actual value of attribute
    #getattr(object, "attribute", default)
        #object - the object whose attribute we want to evaulate
        #attribute - the name of the attribute we want to evaluate
        #default - the value that is returned if the attribute does not exist(note: this paramter is optional)


