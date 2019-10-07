class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        result = -1

        if self.items != []:
            result = self.items.pop()

        return result

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        result = -1

        if self.items != []:
            result = self.items[len(self.items) - 1]

        return result


def isOperand(c):
    return (c >= 'a' and c <= 'z') or (c >= 'A'and c <= 'Z')


operator = '+-*/'


def isOperator(c):
    return c in operator


def getPriority(c):
    num = 0
    for ch in operator:
        num += 1
        if ch == c:
            if ch in '-/':
                num -= 1
            break
    return num


def toPostfix(inputStr):
    out = ''
    stack = Stack()

    for char in inputStr:
        if isOperand(char):
            out += char

        elif isOperator:
            while True:
                topChar = stack.peek()

                if stack.isEmpty() or topChar == '(':
                    stack.push(char)
                    break
                else:
                    thisPriority = getPriority(char)
                    brforePriority = getPriority(topChar)

                    if thisPriority > brforePriority:
                        stack.push(char)
                        break

                    else:
                        out += stack.pop()

        elif char == '(':
            stack.push(char)

        elif char == ')':
            tmp = stack.pop()
            while tmp != '(':
                out += tmp
                tmp = stack.pop()

    while not stack.isEmpty():
        out += stack.pop()

    return out


def toInfix(inputStr):
    out = ''
    stack = Stack()

    for char in inputStr:
        if isOperand(char):
            stack.push(char)
        else:
            e2 = stack.pop()
            e1 = stack.pop()
            newStr = '(' + e1 + char + e2 + ')'
            stack.push(newStr)

    out = stack.pop()
    return out


Input = 'A*B+C'
print(toPostfix(Input))
a = 'AB*C+'
print(toInfix(a))
