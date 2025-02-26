
class Employee:

    def __init__(self,id,name):
        self.id = id
        self.name=name

    def display_info(self,position):
        print(f"The {position} has id as {self.id} and name as {self.name}")

emp1 = Employee(2157925,"Sheik")
emp2 = Employee(2157926,"Musthaq")



emp1.display_info("PA")
emp2.display_info("PAT")