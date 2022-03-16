import time
start_time = time.time()

triplet_sum = 1000

num_list = list(range(1,triplet_sum+1))

checker = True
for i in num_list:
    if checker == False:
        break
    for j in num_list:
        if checker == False:
            break
        for k in num_list:
            if i!= None and j!= None and k!= None and i<j<k and i+j+k==triplet_sum and i**(2) + j**(2) == k**(2):
                print(i*j*k)
                checker = False
                break
    num_list[num_list.index(i)] = None

print("--- %s seconds ---" % (time.time() - start_time))