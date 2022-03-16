import time
start_time = time.time()

n = 600851475143

def factor(num): # takes a int and returns set of factors
    factors = set()

    for i in range(1,int(num**(1/2))+1): # list of factors (using sq root)
        if num%i ==0:
            factors.add(i)
            factors.add(num//i)

    return factors



def prime_factor(num):
    factor_list = list(factor(num))
    factor_list.sort()
    prime_factors = []

    if len(factor_list) <= 2: # for input 1 and prime factors
        prime_factors.append(factor_list[-1])
    else:
        factor_list.remove(1)
        for i in factor_list: # sieve method
            for j in factor_list:
                if i!=None and j!=None and i!=j and j%i==0 :
                    factor_list[factor_list.index(j)] = None

    for i in factor_list:
        if i!=None:
            prime_factors.append(i)




    return prime_factors

print(prime_factor(n)[-1])

print("--- %s seconds ---" % (time.time() - start_time))