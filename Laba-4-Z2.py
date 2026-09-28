P=1.0
for n in range (1,21):
    P *=((2*n**2+5*n+1)/(n**3/4+2*n**2+1))
print(P)