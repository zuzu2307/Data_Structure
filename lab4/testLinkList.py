import link_list


message = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
myList = link_list.List(message[0])
i = len(message)
n = 1
while n < i:
    myList.append(message[n])
    n += 1

print(myList)
print('------------------------------------------------------------')

myList.addHead('A')
print(myList)
print('------------------------------------------------------------')

print(myList.before('2'))
print('------------------------------------------------------------')

print(myList.isIn('3'))
print('------------------------------------------------------------')

print('remove 3')
myList.remove('3')
print(myList)
print('------------------------------------------------------------')

myList.removeHead()
print(myList)
print('------------------------------------------------------------')

myList.removeTail()
print(myList)
print('------------------------------------------------------------')

