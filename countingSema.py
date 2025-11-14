## Counting semaphore

import threading
import time
import random


semaphore = threading.Semaphore(3)

def access_resource(thread_id):
    
    print(f"Thread-{thread_id} wants to access the resource...\n")
    semaphore.acquire()

    print(f"Thread-{thread_id} is using the resource.\n")
    time.sleep(random.randint(1, 4)) #Protita thread 1-4 sec resource use korbe


    print(f"Thread-{thread_id} has released the resource.\n")
    semaphore.release()


threads = []


for i in range(5):
    t = threading.Thread(target=access_resource, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have finished their work.")
