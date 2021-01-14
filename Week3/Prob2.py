class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_item = price_of_item

class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return 0.001*self.price_of_item

class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return 0.00005*self.price_of_item