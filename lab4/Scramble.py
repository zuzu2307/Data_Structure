import link_list


message = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
myList = link_list.List(message[0])
i = len(message)
n = 1
while n < i:
    myList.append(message[n])
    n += 1


def bottomUp(inputList, percent):
    l = inputList.size()
    p = (int)((percent/100) * l)
    end = p
    num = 0
    while num < end:
        inputList.append(myList.getNode(num))
        inputList.removeHead()
        num += 1


def riffleShuffle(inputList, percent):
    l = inputList.size()
    p = (int)((percent/100) * l)
    end = p
    num = 0
    while p < l:
        inputList.insert()


percentCut = 30
percentShuffle = 60


print(myList.size())
print(myList)
print('------------------------------bottomUp----------------------------------------')

bottomUp(myList, percentCut)
print(myList)
print('----------------------------riffleShuffle-------------------------------------')

#riffleShuffle(myList, percentShuffle)
#print(myList)
print('------------------------------------------------------------------------------')
