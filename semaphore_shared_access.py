from time import sleep
from random import random
from multiprocessing import Process, Semaphore

# Task to run on the CPU
def task(shared_semaphore, ident):
    with shared_semaphore:
        val = random()
        sleep(val)
        print(f'Process {ident} got {val}', flush=True)

if __name__ =='__main__':
    # Create the shared semaphore
    semap = Semaphore(2)
    processes = [Process(target=task, args=(semap, i)) for i in range(100)]

    # Start Child processes
    for process in processes:
        process.start()

    # wait for child processes to finish
    for process in processes:
        process.join()
