from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Lock

def task(shared_lock, ident, value):
    with shared_lock:
        print(f'*{ident} got a lock, sleeping {value}')
        sleep(value)

# Protect the entry point
if __name__=='__main__':
    lock = Lock()
    # Create a number of processes with different args
    processes = [Process(target=task,
                        args=(lock, i, random())) for i in range(10)]
    
    for process in processes:
        process.start()

    for process in processes:
        process.join()
