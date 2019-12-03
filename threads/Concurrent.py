from concurrent.futures import ThreadPoolExecutor
from time import sleep,time


@measure_time
def return_message(message):
    sleep(6)
    return message

pool = ThreadPoolExecutor(3)

future = pool.submit(return_message,("hello"))

print(future.done())
print(future.done())
print(future.done())
sleep(3)
print(future.done())
print(future.done())
sleep(3)
print(future.done())
print(future.result())

