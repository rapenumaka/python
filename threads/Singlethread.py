import time

print('Single thread')

start = time.perf_counter()

def dosomething():
    print("funtion sleeping zzzzzZZZZ")
    time.sleep(1)
    print("woke up")

dosomething()
dosomething()

finish = time.perf_counter()

print('Total time taken {} secs'.format(round(finish-start,2)))