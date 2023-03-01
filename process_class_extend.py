from time import sleep
from multiprocessing import Process

class CustomProcess(Process):
    def run(self):
        sleep(1)
        print('This is another process', flush=True)
    def __str__(self):
        return 'This is another process'

# Create entrypoint script in Python
if __name__ == '__main__':
    process = CustomProcess()
    print(process)
    process.start()
    print('Waiting for the process to finish')
    process.join()
