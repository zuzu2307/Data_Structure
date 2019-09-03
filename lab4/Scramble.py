import link_list

message = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
i = len(message)
n = 1
myList = link_list.List(message[0])

while n < i:
    myList.append(message[n])
    n += 1

print(myList.size())

print(myList)
