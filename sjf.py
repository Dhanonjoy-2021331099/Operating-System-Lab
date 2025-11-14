def sjf(processes, burst, arrival):
    n = len(processes)
    waiting = [0] * n
    turnaround = [0] * n
    completion = [0] * n
    finished = [False] * n

    time = 0
    completed = 0

    while completed < n:
        # ready queue: যেগুলা এসে গেছে কিন্তু শেষ হয়নি
        ready = [i for i in range(n) if arrival[i] <= time and not finished[i]]

        if not ready:
            # যদি কোনো process ready না থাকে, তাহলে সময় বাড়াও
            time = min([arrival[i] for i in range(n) if not finished[i]])
            continue

        # ready queue থেকে সবচেয়ে ছোট burst ওয়ালা নির্বাচন
        idx = min(ready, key=lambda i: burst[i])

        waiting[idx] = time - arrival[idx]
        time += burst[idx]
        completion[idx] = time
        turnaround[idx] = completion[idx] - arrival[idx]
        finished[idx] = True
        completed += 1

    # Output
    print("Process\tArrival\tBurst\tWaiting\tTurnaround")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += waiting[i]
        total_tat += turnaround[i]
        print(f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{waiting[i]}\t{turnaround[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")


# 🔹 Example Input
processes = [1, 2, 3, 4, 5]
arrival = [4, 0, 1, 6, 2]
burst = [5, 2, 5, 7, 3]

sjf(processes, burst, arrival)
