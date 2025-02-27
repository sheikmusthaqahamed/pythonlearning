str1 = "Hi John, Thank you for placing order! Your Order Number is: Test125625"


#1
print(str1[str1.index("Test"):])

#2
print(str1[str1.find("Test"):])

#3
list1 = str1.split(": ")
print(list1)
for value in list1:
    if value.startswith("Test"):
        print(value)

#4
list1 = str1.split(" ")
print(list1)
for value in list1:
    if value.startswith("Test"):
        print(value)

#5
list1 = str1.split(":")
print(list1)
for value in list1:
    if value.find("Test") != -1:
        print(value.strip())

#6
list1 = str1.split(":")
print(list1)
for value in list1:
    if value.count("Test"):
        print(value.strip())


#7
import re
match1 = re.search(r"Te\w+\d+",str1)
print(match1.group())