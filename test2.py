class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        s = ''
        tmp = self.head
        while tmp != None:
            s += str(tmp.data) + ' '
            tmp = tmp.next
        return s

    def __len__(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    def append(self, data):
        if isinstance(data, Node):
            newNode = data
        else:
            newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            tmp = self.head
            while True:
                if tmp.next == None:
                    tmp.next = newNode
                    break
                tmp = tmp.next

    def remove(self, data):
        removeNode = None
        if self.head.data == data:
            removeNode = self.head
            self.head = self.head.next
            removeNode.next = None
        else:
            tmp = self.head
            while tmp != None:
                if tmp.next != None and tmp.next.data == data:
                    removeNode = tmp.next
                    tmp.next = tmp.next.next
                    removeNode.next = None
                tmp = tmp.next
        return removeNode

    def add(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        elif data <= self.head.data:
            newNode.next = self.head
            self.head = newNode
        else:
            tmp = self.head
            while tmp != None:
                if tmp.next != None and data <= tmp.next.data:
                    tmp2 = tmp.next
                    tmp.next = newNode
                    newNode.next = tmp2
                    return
                tmp = tmp.next
            self.append(data)

    def Mean(self):
        divider = self.__len__()
        sum = 0
        tmp = self.head
        while tmp != None:
            sum += tmp.data
            tmp = tmp.next
        sum = sum/divider
        return str(sum)

    def Mode(self):
        l = []
        check = []
        s = ''
        n = 0
        tmp = self.head
        while tmp != None:
            n += 1
            if tmp.next != None and tmp.data != tmp.next.data:
                temp = n
                n = 0
                if l == []:
                    l.append(tmp.data)
                    check.append(temp)
                else:
                    while True:
                        a = check.pop()
                        if a < temp:
                            l.pop()
                            if(l == []):
                                l.append(tmp.data)
                                check.append(temp)
                                break
                        elif a == temp:
                            check.append(a)
                            check.append(temp)
                            l.append(tmp.data)
                            break
                        else:
                            check.append(a)
                            break
            tmp = tmp.next

        while l != []:
            s += str(l.pop(0)) + ' '

        return s


    def Median(self):
        l = []
        middle = int((self.__len__() - 1)/2)

        tmp = self.head
        while tmp != None:
            l.append(tmp.data)
            tmp = tmp.next

        sum = (l[middle] + l[middle + 1])/2
        return str(sum)



l = LinkedList()
print('Enter 12 number : ')
a = input().split()
for i in a:
    l.add(int(i))
print(l)
print('Mean = ' + l.Mean())
print('Mode = ' + l.Mode())
print('Median = ' + l.Median())
