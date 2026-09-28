import math
s = 0.0
for n in range (1,26):
    term = ((n**2 +2) / (2 * n**2 + 3))
    s += term 
print (f'{s:.5f}')