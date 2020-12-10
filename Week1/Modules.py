from datetime import datetime

current_time = datetime.now()
print(current_time)


#Import random below:
import random

#Create random_list below:
random_list = []
random_list = [random.randint(1, 101) for i in range(101)]

#Create randomer_number below:
randomer_number = random.choice(random_list)

#Print randomer_number below:
print(randomer_number)


#Decimals in Python
from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumpdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumpdrop
#Returns 0.45 instead of 0.4499999999999999999999999999
print(cost_of_transaction)


#Decimal Practice
#import Decimal below:
from decimal import Decimal

#Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

#can import one module(.py file) into another to access the functions in that class
#Import library below:
from secondfile import always_three

#Call your function below:
always_three()
