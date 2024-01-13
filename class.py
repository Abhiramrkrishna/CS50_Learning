
### Dict
# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print (f"{student['name']} from {student['house']}")

# def get_student():
    
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# main()


###Class

# class Student:
#     ...


# def main():
#     student = get_student()
#     # if student["name"] == "Padma":
#     #     student["house"] = "Ravenclaw"
#     print (f"{student.name} from {student.house}")

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")

    
#     # name = input("Name: ")
#     # house = input("House: ")
#     # student = Student(name, house) #Constructor call/contructing an object

#     return student

# main()


## Test class
# class Student:
#     def __init__(self, name, house,patronus):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ("Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"):
#             raise ValueError("Wrong House")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self): ###init and str are built in functions
#         return (f"{self.name} from {self.house} has {self.patronus} charm")
    
#     def charm(self):
#         match self.patronus:
#             case "Stag" : return (":Horse:")
#             case "Otter" : return (":Otter:")
#             case "Dawg" : return (":Dog:")
#             case _: return None


# def main():
#     student = get_student()
#     print ("Expecto Patronum!!")
#     print(student.charm())
#     print(student)
    

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus:")
#     student = Student(name, house, patronus) #Constructor call/contructing an object
#     try:
#         return student
#     except Value:
#         ...

# main()


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
    
        self.name = name
        self.house = house
        

    def __str__(self): ###init and str are built in functions
        return (f"{self.name} from {self.house}")
    
    @property ##Getter fn to avoid modification/alteration - decorator
    def house(self):
        return self._house
    
    @house.setter  ##Setter fn to avoid modification/alteration - decorator
    def house(self, house):
        if house not in ("Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"):
            raise ValueError("Wrong House")
        self._house = house
    

def main():
    student = get_student()
    # student.house = "Ajj" ### To avoid modification like this one
    print(student)
    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus:")
    student = Student(name, house) #Constructor call/contructing an object
    try:
        return student
    except Value:
        ...

main()