class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} is in {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)
    
    
    """##GETTER NAME
    @property
    def name(self):
        return self._name
    ##SETTER NAME
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is required")
        self._name = name
    
    
    #GETTER HOUSE
    @property
    def house(self):
        return self._house
    #SETTER HOUSE
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("House is not valid")
        self._house = house"""


#STUDENT
def main():
    student= Student.get()
    print(student)

if __name__ =="__main__":
    main()

