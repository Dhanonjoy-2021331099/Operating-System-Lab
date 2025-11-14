import threading
import time
# Number of philosophers
N = 5

# Semaphore for each fork
forks = [threading.Semaphore(1) for _ in range(N)]

def philosopher(id):
    left = id
    right = (id + 1) % N
    
    for _ in range(1):  # eat 1 times
        print(f"Philosopher {id} is thinking ")
        time.sleep(1)
        
        print(f"Philosopher {id} is hungry ")
        
        # To avoid deadlock, pick lower numbered fork first
        first, second = (left, right) if id % 2 == 0 else (right, left)
        
        forks[first].acquire()
        forks[second].acquire()
        
        print(f"Philosopher {id} is eating ")
        time.sleep(2)
        
        forks[first].release()
        forks[second].release()
        
        print(f"Philosopher {id} finished eating\n")
        
# Create threads for each philosopher
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

# Wait for all philosophers to finish
for t in threads:
    t.join()

print("Dinner is over ")