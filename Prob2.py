class Circle:
    pi = 3.14
    def area(self, diameter):
        radius = diameter/2
        return self.pi*radius**2
    def __init__(self, diameter):
        print("New circle with diameter", diameter)


#circle = Circle()
#pizza_area = circle.area(12)
#teaching_table_area = circle.area(36)
#round_room_area = circle.area(11460)
#print(pizza_area)
#print(teaching_table_area)
#print(round_room_area)

teaching_table = Circle(36)
