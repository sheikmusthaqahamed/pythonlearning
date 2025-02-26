from analyst import Analyst


class JuniorAnalyst(Analyst):

    def __init__(self, id, name, year_of_joining,location):
        super().__init__(id, name, year_of_joining)
        self.location = location
        print("Junior Analyst Object Created")

    def show_loc(self):
        print(f"Location is {self.location}")