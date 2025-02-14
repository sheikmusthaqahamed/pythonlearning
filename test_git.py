list_of_list = ["sbf",23,"grvf",["fwedgv",[2,44,"tbg"],"3rfe"],4]
list2 = []
for value in list_of_list:
    if type(value) == list:
        for val2 in value:
            if type(val2)==list:
               for num in val2:
                list2.append(num)
            else:
                list2.append(val2)
    else:
        list2.append(value)

print(list_of_list)
print(list2)

a,b,c,d,e = ["ec","Ed","2de","wd"]

#     a,b,c,d,e = ["ec","Ed","2de","wd"]
#     ^^^^^^^^^
# ValueError: not enough values to unpack (expected 5, got 4)


#     a,b,c = ["ec","Ed","2de","wd"]
#     ^^^^^
# ValueError: too many values to unpack (expected 3)