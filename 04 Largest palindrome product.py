import time
start_time = time.time()

digit = 3
lim = 10**digit

multiply = []
for i in range(1,lim):
    if i%10==0:
        pass
    else:
        multiply.append(i)

i = 0
j = 0
palindrome = []

while True:
    
    if str(multiply[0]*multiply[j]) == str(multiply[0]*multiply[j])[::-1] :
        palindrome.append(multiply[0]*multiply[j])

    j+=1
    if j == len(multiply):
        j=0
        multiply.pop(0)
    
    if len(multiply)==0:
        break

palindrome.sort()
print(palindrome[-1])

print("--- %s seconds ---" % (time.time() - start_time))