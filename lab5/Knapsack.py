def printSack(sack, maxi):
    global price
    global name
    print('                ',end = ' ')
    for i in range(maxi+1):
        #print(price[sack[i]], end=' ')
        print(name[sack[i]], price[sack[i]], end=' ')
    print()


def pick(sack, sackIndex, mLeft, priceIndex):
    global size
    global price
    if priceIndex < size:
        curPrice = price[priceIndex]

        if mLeft < priceIndex:
            pick(sack, sackIndex, mLeft, priceIndex+1)
        else:
            mLeft -= curPrice
            sack[sackIndex] = priceIndex
            if mLeft == 0:
                printSack(sack, sackIndex)
            else:
                pick(sack, sackIndex+1, mLeft, priceIndex+1)
            pick(sack, sackIndex, mLeft+curPrice, priceIndex+1)


price = [20, 10, 5, 5, 3, 2, 20, 10]
name = ['soap', 'potato chips', 'loly pop',
        'toffy', 'pencil', 'rubber', 'milk', 'cookie']
size = len(price)
sack = size*[-1]
pick(sack, 0, 20, 0)