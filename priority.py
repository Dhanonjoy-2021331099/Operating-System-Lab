# Priority Scheduling

def priority_scheduling(processes, burst_times, priorities):
    n = len(processes) 
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Sort by priority 
    proc = sorted(zip(processes, burst_times, priorities), key=lambda x: x[2])

    # Waiting time 
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + proc[i-1][1]

    # Turnaround time 
    for i in range(n):
        turnaround_time[i] = proc[i][1] + waiting_time[i]

    # Result Table
    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{proc[i][0]}\t{proc[i][1]}\t\t{proc[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    #  Gantt Chart 
    print("\nGantt Chart:")
    chart = "|"
    timeline = "0"
    time = 0
    for p, bt, pr in proc:
        chart += f" P{p} |"
        time += bt
        timeline += f"{' ' * (len(chart) - len(timeline))}{time}"
    print(chart)
    print(timeline)


# Example Run
processes = [1, 2, 3, 4]
burst_times = [1, 2, 1, 4]
priorities = [3, 1, 4, 2]

priority_scheduling(processes, burst_times, priorities)
