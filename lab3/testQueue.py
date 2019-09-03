import Queue
nameQueue = Queue.Queue()

for char in 'Korntawat':
    nameQueue.enQueue(char)

print(nameQueue.items)
print(nameQueue.isEmpty())

for i in range(9):
    print(nameQueue.deQueue())
    print(nameQueue.items)

print(nameQueue.isEmpty())
