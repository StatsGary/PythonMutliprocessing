from multiprocessing import Process

if __name__=='__main__':
    process = Process(name='FunkyProcess')
    print(process.name)
