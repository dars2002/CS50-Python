students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Hermione", "house": "Gryffindor"},
]

houses = set()

for student in students:
    houses.add(student["house"])
        
        
for house in sorted(houses):
    print(house)