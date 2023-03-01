from time import sleep
from random import random
from multiprocessing import Process, Event

def task(shared_event, number):
    print(f'Process {number} waiting...', flush=True)
    shared_event.wait()
    value = random()
    sleep(value)
    print(f'Process {number} got {value}', flush=True)

if __name__ == '__main__':
    event = Event()
    processes = [Process(target=task, args=(event, i)) for i in range(5)]

    for process in processes:
        process.start()
    
    print('Main process blocking...')
    sleep(2)
    # Trigger all child processes
    event.set()

    for process in processes: 
        process.join()
