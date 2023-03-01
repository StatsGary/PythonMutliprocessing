from multiprocessing import parent_process

if __name__=='__main__':
    process = parent_process()
    print(process)
