import link_list as ll
import math

def bottomUp(list, percent):
    n = math.floor(int(percent / 10))
    for i in range(0, n):
        list.append(list.removeHead())
    print('bottomup   : ', list)

def deBottomUp(list, percent):
    n = math.floor(int(percent / 10))
    for i in range(0, n):
        list.addHead(list.removeTail())
    print('debottomup : ', list)

def riffle(list, percent):
    n = math.floor(int(percent / 10)) 
    loop = 10 - n
    if n <= 5:
        loop = n-1
    index = 1
    for i in range(0, loop):
        temp = list.removeByIndex(n)
        list.addByIndex(index, temp)
        n += 1
        index += 2
    print('riffle     : ', list)

def deRiffle(list, percent):
    n = math.floor(int(percent / 10)) 
    indexToAdd = list.size() - 1
    if n > 5:
        n = 10 - n
    else:
        n = n - 1
        indexToAdd = n * 2
    for i in range(0, n):
        temp = list.removeByIndex(i + 1)
        list.addByIndex(indexToAdd, temp)
    print('deriffle   : ', list)

    
    
myList = ll.List()

for i in range(1, 11):
    myList.append(i)

print('message    : ', myList)
bottomUp(myList, 30)
riffle(myList, 60)
riffle(myList, 30)
deRiffle(myList, 30)
deRiffle(myList, 60)
deBottomUp(myList, 30)