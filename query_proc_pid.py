from multiprocessing import Process

if __name__ =='__main__':
    process = Process()
    print(process.pid)
    process.start()
    print(process.pid)
