studList = [12.0,[40, 50, "apple"],["mango","apple","banana"],40 ,"apple"]
print(studList.index("apple",2,3))

# for index in range(0,len(studList)):
#     if type(studList[index]) == list:
#         for index2 in range(0,len(studList[index])):
#             if studList[index][index2] == "apple":
#                 print(f"{studList[index][index2]}   [{index}][{index2}]")
#     elif studList[index] == "apple":
#         print(f"{studList[index]}   [{index}]")
