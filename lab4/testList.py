import node as ll
a = ll.Node('A')
b = ll.Node('B')
c = ll.Node('C')
d = ll.Node('D')

a.setNext(b)
b.setNext(c)
c.setNext(d)

print(a)
print(a.next)
print(b.next)
print(c.next)