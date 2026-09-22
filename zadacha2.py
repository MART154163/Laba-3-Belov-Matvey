import math
a = 0.1
b = 0.9
h = 0.05
n  = round ((b-a)/h)+1
print('-'*25)
print(f'x  y(x)')
print('-'*25)
for i in range(n):
    x = round (a +i *h, 4)
    y = (2 ** math.asin(x)) + math.log2(x)
    print (f'{x:7.2f}     {y:11.5f}')
print('-'*25)