

class Employee:

    def __init__(self,id,name,year_of_joining):
        self.id = id
        self.name = name
        self.year_of_joining = year_of_joining
    
    def display_info(self,age):
        print(f"Employee {self.name} of age {age} of id {self.id} and year of joining {self.year_of_joining}")
    
    def submit_timesheet(self,no_of_days):
        print(f"Timesheet for {self.name} is submitted for {no_of_days} days")