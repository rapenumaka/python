import time,multiprocessing


print('Multithreads thread')

start = time.perf_counter()

def dosomething():
    print("funtion sleeping zzzzzZZZZ")
    time.sleep(1)
    print("woke up")


p1 = multiprocessing.Process(target= dosomething)
p2 = multiprocessing.Process(target= dosomething)

p1.start()
p2.start()

## Join method will prevent execution till p1,p2 will
p1.join()
p2.join()


finish = time.perf_counter()

print('Total time taken {} secs'.format(round(finish-start,2)))