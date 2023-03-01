from multiprocessing import current_process

if __name__=='__main__':
    process = current_process()
    print(process)
