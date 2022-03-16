import time
start_time = time.time()

limit_value = 4000000

term = 1
fib_seq = [0]
sum = 0

while term < limit_value :

    if term%2 == 0:
        sum += term

    fib_seq.append(term)
    term = fib_seq[-1] + fib_seq[-2]

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))