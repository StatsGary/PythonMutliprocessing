from time import sleep
from multiprocessing import active_children
from multiprocessing import Process

def task(): 
    sleep(1)

if __name__=='__main__':
    processes = [Process(target=task) for _ in range(5)]
    # Start the child processes
    for process in processes:
        process.start()

    children = active_children()
    print(f'Active children count:{len(children)}')

    for child in children:
        print(child)
