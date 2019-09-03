import Stack
nameStack = Stack.Stack()

for char in 'Korntawat':
    nameStack.push(char)

print(nameStack.items)
print(nameStack.size())
print(nameStack.isEmty())
print(nameStack.peek())

for i in range(9):
    print(nameStack.pop())

print(nameStack.isEmty())

print('---------------------------------------------------------------------------------')


testStack = Stack.Stack()
error = False
myStr = ' ( 3 + 2 ) / { 4**5 }'

for char in myStr:
    if char == '(' or char == '[' or char == '{':
        testStack.push(char)
    elif char == ')' or char == ']' or char == '}':
        if testStack.isEmty() :
            error = True
        else :
            oPen = testStack.pop()
            if not ((oPen == '(' and char == ')') or (oPen == '[' and char == ']') or (oPen == '{' and char == '}')) :
                error = True
if error :
    print('MISMATCH')
else :
    if not (testStack.isEmty()):
        print('MISMATCH open paren. exceed')
    else :
        print('MATCH')



print('---------------------------------------------------------------------------------')

carStackA = Stack.Stack()
carStackB = Stack.Stack()


for i in range(1,5):
    if i <= carStackA.maximum :
        carStackA.push(i)
        print('car ' + str(i) + ' arrive        ' + 'space left ' + str(4-i))
    else :
        print('car ' + str(i) + ' cannot arrive : SOI FULL')

def depart(item):
    for i in range (4-item) :
        carStackB.push(carStackA.pop())
    carStackA.pop()
    for i in range (carStackB.size()):
        carStackA.push(carStackB.pop())


depart(2)
print(carStackA.items)
print(carStackB.items)
print(carStackA.isFull())



