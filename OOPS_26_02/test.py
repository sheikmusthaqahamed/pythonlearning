from senior_analyst import SeniorAnalyst
from junior_analyst import JuniorAnalyst
from analyst import Analyst

print()
sa1 = SeniorAnalyst(2222,"Maddy",2000,"Chennai")
ja1 = JuniorAnalyst(3333,"Returns",2015,"Bengaluru")
print()
sa1.do_work()
print()
sa1.display_info(88)
print()
sa1.submit_timesheet(5)
print()
sa1.rating_info(5,87)
print()

ana1 = Analyst(3333,"Returns",2015)
ana1.do_work()
ana1.display_info(45)
ana1.submit_timesheet(4)