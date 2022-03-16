lim = 10001

prime = [2]
i=2
while len(prime) < lim:
    for j in prime:
        if i%j == 0: # check if the next number is divisible by any of the primes found so far
            break
    else:
        prime.append(i) #if not , its out new prime
    i+=1

prime.sort()

print(prime[-1])