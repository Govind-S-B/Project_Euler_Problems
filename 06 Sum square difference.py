import time
start_time = time.time()

lim = 100

sq_sum_diff = 0

list_nums =  list(range(1,lim+1))
for i in list_nums:
    for j in list_nums:
        if i!=None and j!=None and i!=j :
            sq_sum_diff += 2*i*j
    list_nums[list_nums.index(i)] = None

print(sq_sum_diff)

print("--- %s seconds ---" % (time.time() - start_time))