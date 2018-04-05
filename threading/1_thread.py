import threading

def thread_fun():
    '''
    Thread Function
    '''
    for i in [1,2,3]:
        print("Thread is running")

if __name__ == "__main__":
    # create the thread
    th1 = threading.Thread(target=thread_fun)

    # start the thread
    th1.start()

    # wait until thread to finish its work
    th1.join()

    print("Exiting main....")
