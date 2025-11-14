## synchronize Co operative process

import threading
import time

# Binary semaphore (0 or 1)
sem = threading.Semaphore(1)

def process(name):
    print(f"{name} wants to enter critical section\n", flush=True)
    
    sem.acquire()  # Wait (no busy wait)
    print(f"{name} entered critical section\n", flush=True)
    
    time.sleep(2)  # critical section simulate
    
    print(f"{name} leaving critical section\n", flush=True)
    sem.release()  # signal

# Two cooperative processes
t1 = threading.Thread(target=process, args=("Process 1",))
t2 = threading.Thread(target=process, args=("Process 2",))

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("All processes finished.")
