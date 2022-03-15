n = 600851475143

factors = []
for i in range(1,int(n**(1/2))+1):
    if n%i ==0:
        factors.extend([i,n//i])

i = 0
while i<len(factors):
    for j in factors:
        if j%factors[i]==0  and j!=factors[i] :
            factors.remove(j)
    i+=1

print(factors[-1])