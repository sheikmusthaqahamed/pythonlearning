InputList = [1,2,3,4,5,6]
# OutputList = [1,3,6,10,15,21]

def test2(list):

    OutputList=[]
    temp = 0 
    for value in list:
        temp=value+temp    #2+1 = 3
        OutputList.append(temp)
    return OutputList

def test(list):
    OutputList=[]
    sum = 0
    for index in range(0,len(list)):
        sum = list[index]+sum
        OutputList.append(sum)
    return OutputList


print(test(InputList))