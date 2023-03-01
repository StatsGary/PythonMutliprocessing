from time import sleep
from multiprocessing import Process

def task():
    sleep(1)

if __name__ == '__main__':
    process = Process(target=task)
    print(process.exitcode)
    process.start()
    print(process.exitcode)
    process.join()
    print(process.exitcode)
