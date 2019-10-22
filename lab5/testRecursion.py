import Recursion as r

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None if next is None else next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        newNode = data if isinstance(data, Node) else Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = newNode
            newNode.next = None


def printList(items):
    if items is not None:
        print(items, end=' ')
        printList(items.next)


def createLLL1(head, items, size):
    if size >= 0:
        tail = Node(items[size], head)
        p = createLLL1(tail, items, size-1)
        return p
    else:
        return head


def createLLL2(head, n):
    if n == 1:
        return Node(Node(1), head)
    else:
        tail = Node(n, head)
        return createLLL2(tail, n-1)



l = [0,1,2,3,4,5,6,7,8,9]
o = []
L = ['A','B','C','D']

print('                 Fac = ',r.fac(5))
r.print1ToN(5)
r.printNto1(5)
print('                 Fib = ',r.fiboR(5))
print('                 Search = ',r.binarySearch(0,9,8,l))
r.move(3,'A','C','B')
print('                 Sum1 = ',r.sum(10,l))
print('                 Sum2 = ',r.sum2(l,0,9))
print('                 Sum3 = ',r.sum3(l))
print('                ',end = ' ')
r.printListForward(l)
print()
print('                ',end = ' ')
r.printListBackward(l)
print()
r.app(o,5)
print('                 o = ',o)
r.appB(o,5)
print('                 o = ',o)
LL = createLLL1(None,L,3)
print('                ',end = ' ')
printList(LL)
print()
LL = createLLL2(None,5)
print('                ',end = ' ')
printList(LL)
print()