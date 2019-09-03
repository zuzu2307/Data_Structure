def triangle(p):
    trilis = []
    for a in range(p):
        for b in range(a, p):
            c = p - a - b
            if c*c == a*a + b*b and c > a and c > b:
                trilis.append((a, b, c))
    return trilis
print(triangle(180))

#def genMid(s) :
#    news = ''
 #   i = 2 * len(s) - 1
 #   for n range(i) :
 #       a = i // 2 
 #       if



#def genPatten(s) :
 #   if len(s) == 1 :
 #       return s
  #  else :
 #       genMid(s)



#sTr = 'X'
#print(genPatten(sTr))
def aLine(s):
    res = '' #result
    for i in range(1, len(s)):
        res = s[i] + res
        res = res + s[i-1]
    res = '.'.join(res)
    return res
def gen_pattern(s):
    n = 3*len(s)+1
    mid = aLine(s) + '\n'
    for i in range(1,len(s)):
        r = aLine(s[i:len(s)])
        r = r.center(n,'.')
        r = r + '\n'
        mid = r + mid + r
    return mid
s = 'wxyz'
print(gen_pattern(s))