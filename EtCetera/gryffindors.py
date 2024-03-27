students = ["Hermione", "Harry" , "Ron"]

for i, student in enumerate(students):
    print(i+1,student)
    

















"""students = [{"name": "Hermione","house": "Gryffindor"},
            {"name": "Draco", "house": "Gryffindor"},
            {"name": "Harry", "house": "Gryffindor"},
            {"name": "Luna", "house": "Ravenclaw"},
]

def is_griff(s):
    return s["house"] == "Gryffindor"
    
gryffindors = filter(is_griff, students)

for gryffindor in sorted(gryffindors, key=lambda s: s['name']):
    print(gryffindor['name'])


#gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]

#for gryffindor in sorted(gryffindors):
#    print(gryffindor)
"""

