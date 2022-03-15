import time
start_time = time.time()

def LCM(num):
    lcm=1
    for i in range(2,num+1):
        if lcm%i!=0: # checks if the LCM acheived so far is divisible by new number
            for j in range(2,num+1):
                if (lcm*j)%i==0: # if not checks what number(factor) multiplied will be able to divide the LCM with new number
                    lcm*=j
                    break
    return lcm

print(LCM(20))
print("--- %s seconds ---" % (time.time() - start_time))