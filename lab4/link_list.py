import node


class List:
    def __init__(self, head=None):
        if head == None:
            self.head = None
        else:
            self.head = node.Node(head)

    def __str__(self):
        list_str = []
        current = self.head
        output = ''
        while current != None:
            list_str.append(current.data)
            current = current.next
        output = ','.join(list_str)
        return output

    def addHead(self, data):
        current = self.head
        while current != None:
            if current == self.head:
                temp = current
                current = node.Node(data)
                self.head = current
                current.next = temp
                return
            current = current.next


    def getNode(self, number):
        count = 0
        current = self.head
        while current != None:
            count += 1
            if count == number:
                return current.data
            current = current.next

    def setLink(self, beforeData, data):
        current = self.head
        temp = current
        while current != None:
            if current.data == data:
                temp = current
            if current.data == beforeData:
                current.next = temp
                return
            current = current.next

    def setHead(self, headdata):
        current = self.head
        while current != None:
            if current.data == headdata:
                self.head = current
                return
            current = current.next

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node.Node(data)

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
        current = self.head
        while current != None:
            if current.next != None and current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


    def removeTail(self):
        current = self.head
        while current != None:
            if current.next.next == None:
                current.next = None
                return
            current = current.next

    def removeHead(self):
        self.head = self.head.next

    def insert(self, beforeData, data):
        current = self.head
        while current != None:
            if current.data == beforeData:
                temp = current.next
                current.next = node.Node(data)
                current.next.next = temp
                return
            current = current.next
