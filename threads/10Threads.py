import time,multiprocessing
import concurrent.futures


print('10 thread')

start = time.perf_counter()

def dosomething(seconds):
    print(f"funtion sleeping {seconds} zzzzzZZZZ")
    time.sleep(seconds)
    print("woke up")

processes =[]


with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(dosomething,1)
    f2 = executor.submit(dosomething,1)

    print(f1.result())
    print(f2.result())

print("doneeee")


for _ in range(10):
    p = multiprocessing.Process(target=dosomething ,args=[1.2])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print('Total time taken {} secs'.format(round(finish-start,2)))