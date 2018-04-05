import threading

def thread_fun_1(n):
    '''
    Thread Function
    '''
    for i in [1,2,3]:
        print(threading.current_thread().name," is running with n = ", n)

def thread_fun_2(n):
    '''
    Thread Function
    '''
    for i in [1,2,3]:
        print(threading.current_thread().name," is running with n = ", n)

if __name__ == "__main__":
    # create the threads
    th1 = threading.Thread(target=thread_fun_1, args=(1,), name = "my thread")
    th2 = threading.Thread(target=thread_fun_2, args=(2,))
    
    # start the thread
    th1.start()
    th2.start()

    # wait until thread to finish its work
    th1.join()
    th2.join()

    print("Exiting ", threading.current_thread().name)
