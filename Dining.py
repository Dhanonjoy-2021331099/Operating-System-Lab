import threading
import time
import random

# Number of philosophers
N = 5

# Initialize forks as semaphores
forks = [threading.Semaphore(1) for _ in range(N)]

def philosopher(id):
    left = id
    right = (id + 1) % N
    
    # Philosopher is thinking
    print(f"Philosopher {id} is thinking", flush=True)
    time.sleep(random.uniform(0.5, 1.5))  # Random thinking time
    
    # Pick forks in order to avoid deadlock
    if id % 2 == 0:
        forks[left].acquire()
        forks[right].acquire()
    else:
        forks[right].acquire()
        forks[left].acquire()
    
    # Philosopher is eating
    print(f"Philosopher {id} is eating\n", flush=True)
    time.sleep(random.uniform(1, 2))  # Random eating time
    
    # Release forks
    forks[left].release()
    forks[right].release()
    print(f"Philosopher {id} finished eating\n", flush=True)

# Create philosopher threads
threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("\nAll philosophers have finished eating.\n")


