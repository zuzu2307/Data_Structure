import Queue as Qu


def enCode(inputStr, i_Series):
    encode = Qu.Queue()
    outputStr = ''
    i = 0

    for c in inputStr:
        if c == ' ':
            outputStr += ' '
            continue

        a = ord(c) + i_Series[i]

        if ord(c) >= 65 and ord(c) <= 90:
            if a > 90:
                a -= 26

        if ord(c) >= 97 and ord(c) <= 122:
            if a > 122:
                a -= 26

        encode.enQueue(a)
        outputStr += chr(encode.deQueue())
       # print(outputStr)
        i += 1
        if(i == len(i_Series)):
            i = 0

    return outputStr


def deCode(inputStr, i_Series):
    decode = Qu.Queue()
    outputStr = ''
    i = 0

    for c in inputStr:
        if c == ' ':
            outputStr += ' '
            continue

        a = ord(c) - i_Series[i]

        if ord(c) >= 65 and ord(c) <= 90:
            if a < 65:
                a += 26

        if ord(c) >= 97 and ord(c) <= 122:
            if a < 97:
                a += 26

        decode.enQueue(a)
        outputStr += chr(decode.deQueue())
       # print(outputStr)
        i += 1
        if(i == len(i_Series)):
            i = 0

    return outputStr
