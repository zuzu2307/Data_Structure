import Caesar_Cipher as CC

I = [2, 5, 6, 1, 8, 3]
ms = 'I love PythZz'
print('Message : ' + ms)

ms = CC.enCode(ms, I)
print('Encode  : ' + ms)

ms = CC.deCode(ms, I)
print('Decode  : ' + ms)

print('------------------------------------------------------------------------------------')