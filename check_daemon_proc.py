from multiprocessing import Process

if __name__== '__main__':
    proc = Process(daemon=True)
    print(proc.daemon)
