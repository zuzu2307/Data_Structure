import node
a = node.Node('A')
b = node.Node('B')
c = node.Node('C')
d = node.Node('D')

a.setNext(b)
b.setNext(c)
c.setNext(d)


print(a)
print(a.next)
print(b.next)
print(c.next)