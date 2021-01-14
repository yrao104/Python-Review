#An Exception is a class that inherits from Python's Exception class
issubclass(ZeroDivisionError, Exception)
#Returns true

class KitchenException(Exception):
    '''
    exception that gets thrown when a kitchen appliance isn't working
    '''

class MicrowaveException(KitchenException):
    '''
    Exception for when the microwave stops working
    '''

class RefridgeratorException(KitchenException):
    '''
    Exception for when the refridgerator stops working
    '''

#attempt to retrieve food from the fridge and heat it in the microwave
#if either exception is raised, order takeout instead
#MicrowaveException is in our try/except block because both are subclasses of KitchenException
'''
def get_food_from_fridge():
    if refridgerator.cooling == False:
        raise RefridgeratorException
    else:
        return food

def heat_food(food):
    if microwave.working == false:
        raise MicrowaveException
    else:
        microwave.cook(food)
        return food

try:
    food = get_food_from_fridge()
    food = heat_food(food)
except KitchenException:
    food = order_takeout()
'''
