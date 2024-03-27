"""students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

by_house = {}
for house in houses:
    letter = house[0]
    if letter not in by_house:
        by_house[letter]=students
    else:
        by_house[letter].append(students)
        
print(by_house)   """

"""
def main():
    dibujarEs(5)
    
def dibujarEs(ex):
    for i in range(ex):
           print("a" * (i+1))
main()
"""
def main():
    x = int(input("what is X? "))
    print("x squared is ",square(x))
    
def square(x):
    return x*x
    
if __name__== "__main__":
    main()
