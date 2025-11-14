import threading
import time

binary_semaphore = threading.Semaphore(1)

def critical_section(thread_id):
    print(f"Thread-{thread_id} trying to enter critical section \n")
    binary_semaphore.acquire()

    print(f"Thread-{thread_id} entered critical section \n")
    time.sleep(3)

    binary_semaphore.release()
    print(f"Thread-{thread_id} exited critical section \n")

t1 = threading.Thread(target=critical_section, args=(1,))
t2 = threading.Thread(target=critical_section, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()
