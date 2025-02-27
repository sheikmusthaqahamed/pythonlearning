# #with 30 mins
# for hr in range (12,0,-1):
#     #list_min = ["30","00"]
#     list_min = range(30,-1,-30)

#     for min in list_min:
#         if min ==0:
#             str_min = "00"
#         else:
#             str_min = str(min)
#         if hr==12:
#             print(str(hr)+":"+str_min+" PM")
#         elif hr==10 or hr==11:
#             print(str(hr)+":"+str_min+" AM")
#         else:
#             print("0"+str(hr)+":"+str_min+" AM")

for hr in range (12,0,-1):
    list_min = range(30,-1,-30)
    for min in list_min:
        if hr==12:
             print(f"{hr:02}:{min:02} PM")
        else:
             print(f"{hr:02}:{min:02} AM")


# #with 60 minutes
# for hr in range (12,0,-1):
#     for min in range (59,-1,-1):
#         if min < 10:
#             min_str = "0"+str(min)
#         elif min==-1:
#             min_str = "00"
#         else:
#             min_str = str(min)
#         if hr==12:
#             print(str(hr)+":"+min_str+" PM")
#         elif hr==10 or hr==11:
#             print(str(hr)+":"+min_str+" AM")
#         else:
#             print("0"+str(hr)+":"+min_str+" AM")
