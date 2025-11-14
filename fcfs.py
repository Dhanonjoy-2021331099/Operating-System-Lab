def fcfs(processes, burst, arrival):
    n = len(processes)
    waiting = [0] * n
    turnaround = [0] * n
    completion = [0] * n

    # process gulo arrival time onujyi sajano
    order = sorted(range(n), key=lambda i: arrival[i])

    time = 0
    for i in order:
        if time < arrival[i]:
            time = arrival[i]   # CPU idle thkle wait korbe
        waiting[i] = time - arrival[i]
        time += burst[i]
        completion[i] = time
        turnaround[i] = completion[i] - arrival[i]

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
arrival = [3, 4, 0, 3, 5]
burst = [1, 5, 2, 7, 5]

fcfs(processes, burst, arrival)
