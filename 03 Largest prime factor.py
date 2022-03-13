n = 600851475143

factors = []
prime = []
for i in range(1,int(n**(1/2))+1):
    if n%i ==0:
        factors.extend([i,n//i])

def check_prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n%i==0:
            return False
            break
    return True

for i in factors:
    if check_prime(i):
        prime.append(i)
prime.remove(1)

print(prime[-1])