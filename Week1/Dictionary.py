#dictionary example - key: value pairs
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
print(sensors)

person = {"name": "Shuri", "age": 18, "siblings": ["T'Chaka", "Ramonda"]}


#a key cannot be a list in a dictionary
#dictionary keys are immutable and must be hashable
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

my_dict = {}
my_dict["new_key"] ="new_value"
menu["cheescake"] = 8

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)


#adding multiple keys
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


#overwriting values
menu["oatmeal"] = 5
menu.update({"carrot juice": 7, "cheescake": 9})
print(menu)

oscar_winners = {"Best Picture": "La La Land", "Best Actor":
    "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)


#list comprehensions to dictionaries
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#zip() combines two lists into a zipped list of pairs
students = {key:value for key, value in zip(names, heights)}
print(students)

city = ['Fremont', 'Palo Alto', 'San Francisco']
temperature = [54, 68, 70]
weather = {key:value for key, value in zip(city, temperature)}
print(weather)
