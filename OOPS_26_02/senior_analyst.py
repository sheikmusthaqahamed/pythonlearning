from analyst import Analyst


class SeniorAnalyst(Analyst):

    def __init__(self, id, name, year_of_joining,location):
        super().__init__(id, name, year_of_joining)
        self.location = location
        print("Senior Analyst Object Created")

    def show_loc(self):
        print(f"Location is {self.location}")

    def do_work(self):
        print(f"Doing SAnalyst level activities for {self.name}")
