import math
x = 2.5
p1 = math.exp(math.cos(x/5))
p2_u = (1+x**3)/(0.5*math.log(x))
p2 = math.sin(3*x)+ math.sqrt(p2_u)
y = p1 * p2
print(f'{y:.5f}')