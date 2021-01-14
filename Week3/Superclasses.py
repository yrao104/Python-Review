#super() lets us call methods from the parent class -> gives us a proxy object to invoke the method of an object's parent class aka superclass

#kitchensink's constructor takes additional parameter and calls constructor for sink with basin and nozzle using super() function
class Sink:
    def __init__(self, basin, nozzle):
        self.basin = basin
        self.nozzle = nozzle

class KitchenSink(Sink):
    def __init__(self, basin, nozzle, trash_compactor = None):
        super().__init__(basin, nozzle)
        if trash_comapctor:
            self.trash_compactor = trash_compactor
