#coding: utf-8

a1 = "440hz"
c1 = "256Hz"

l = [2, 2, 1, 2, 2, 2, 1]
d = {}
chars = "cdefgab"
acc = 0

for i in range(3):
    for c in range(0, chars.__len__()):
        symbol =  chars[c] + str(i)
        d[symbol] = acc
        acc += l[c]

def frequency(s):
    interval = d['a1'] - d[s]
    return 440.0 / 2 ** (interval/12.0)
    

c1 = frequency('c1')

print c1
