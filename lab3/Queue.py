class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return True if self.items == [] else False

    def deQueue(self):
        return self.items.pop(0)
