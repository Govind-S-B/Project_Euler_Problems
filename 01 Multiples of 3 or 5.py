import time
start_time = time.time()

range_input = 1000
sum = 0

for i in range(1,range_input):
    if i%3==0 or i%5==0 :
        sum += i

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))