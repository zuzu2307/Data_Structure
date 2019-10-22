import math


def eat(n):
    if n < 1:
        print('                 eat ', n)
    else:
        print('                 eat ', n)
        eat(n/2)


def fac(n):
    # 5 * 4 * 3 *2 *1
    if n > 1:
        return n * fac(n-1)
    else:
        return 1


def sum1ToN(n):
    if n > 1:
        return n + sum1ToN(n-1)
    else:
        return 1


def printNto1(n):
    if n == 1:
        print('                ', n)
    else:
        print('                ', n)
        printNto1(n-1)


def print1ToN(n):
    if n >= 1:
        print1ToN(n-1)
        print('                ', n)


def fiboR(n):
    if n <= 2:
        return n-1
    else:
        return fiboR(n-1) + fiboR(n-2)


def binarySearch(low, high, x, lists):
    if high < low:
        return
    mid = math.floor(int((high+low)/2))
    if x == lists[mid]:
        return mid
    elif lists[mid] < x:
        return binarySearch(mid+1, high, x, lists)
    else:
        return binarySearch(low, mid-1, x, lists)


def move(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("                 Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    move(n-1, from_rod, aux_rod, to_rod)
    print("                 Move disk", n, "from rod", from_rod, "to rod", to_rod)
    move(n-1, aux_rod, to_rod, from_rod)


def sum(n, lists):
    if n == 0:
        return 0
    elif n == 1:
        return lists[0]
    else:
        return sum(n-1, lists) + lists[n-1]


def sum2(lists, fromIndex, toIndex):
    if fromIndex > toIndex:
        return 0
    elif fromIndex == toIndex:
        return lists[fromIndex]
    else:
        x = lists[fromIndex]
        y = sum2(lists, fromIndex+1, toIndex)
        return x+y


def sum3(lists):
    size = len(lists)
    if size == 0:
        return 0
    elif size == 1:
        return lists[0]
    else:
        x = lists[0]
        y = sum3(lists[1:])
        return x+y


def printListForward(items):
    size = len(items)
    if size == 1:
        print(items[0], end=' ')
        return
    else:
        print(items[0], end=' ')
        printListForward(items[1:])


def printListBackward(items):
    size = len(items)
    if size == 0:
        return
    else:
        temp = items[0]
        printListBackward(items[1:])
        print(temp, end=' ')


def app(items, n):
    if n == 1:
        items.append(1)
    else:
        app(items, n-1)
        items.append(n)


def appB(items, n):
    if n == 1:
        items.append(1)
    else:
        items.append(n)
        appB(items, n-1)


