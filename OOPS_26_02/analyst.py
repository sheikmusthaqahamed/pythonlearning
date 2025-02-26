from employee import Employee

class Analyst(Employee):

    def __init__(self,id,name,year_of_joining):

        super().__init__(id, name,year_of_joining)
        self.position = "Analyst" 

    def rating_info(self,rating,age):
        super().display_info(age)
        print(f"Rating is {rating} for position {self.position}")
        
    def do_work(self):
        print(f"Doing analyst level activities for {self.name}")
        
# ana1 = Analyst(2157925,"Sheik",2022)
# ana1.rating_info(4)
# ana1.submit_timesheet(5)