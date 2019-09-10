import node


class List:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        temp = self.head
        s = ''
        while temp != None:
            s += str(temp.data) + ' '
            temp = temp.next
        return s

    def addHead(self, data):
        if isinstance(data, node.Node):
            newNode = data
        else:
            newNode = node.Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        if isinstance(data, node.Node):
            newNode = data
        else:
            newNode = node.Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.next == None:
                    temp.next = newNode
                    break
                temp = temp.next

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    def isIn(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False

    def before(self, data):
        current = self.head
        while current != None:
            if current.next != None and current.next.data == data:
                return current
            current = current.next
        return None

    def remove(self, data):
        dataRef = self.before(data)
        removedNode = None
        if dataRef != None:
            temp = self.head
            while temp != dataRef:
                temp = temp.next
            removedNode = temp.next
            temp.next = temp.next.next
        else:
            if self.head != None and self.head.data == data:
                removedNode = self.head
                self.head = self.head.next
        return removedNode

    def removeTail(self):
        tail = None
        if self.head != None:
            if self.head.next == None:
                tail = self.head
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                tail = temp.next
                temp.next = None
        return tail

    def removeHead(self):
        h = self.head
        if self.head != None:
            self.head = self.head.next
            if self.head != None:
                h.next = None
        return h

    def addByIndex(self, index, data):
        if isinstance(data, node.Node):
            newNode = data
        else:
            newNode = node.Node(data)

        if index == 0:
            if self.head == None:
                self.head = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            temp = self.head
            for i in range(0, index-1):
                temp = temp.next
            aNode = temp.next
            temp.next = newNode
            newNode.next = aNode

    def removeByIndex(self, index):
        removedNode = None
        if index == 0:
            if self.head != None:
                removedNode = self.head
                self.head = self.head.next
                removedNode.next = None
        else:
            temp = self.head
            for i in range(0, index - 1):
                temp = temp.next
            removedNode = temp.next
            temp.next = temp.next.next
            removedNode.next = None
        return removedNode
