def round_robin(processes, burst_times, quantum):
    rem_bt = burst_times.copy() 
    n = len(processes)
    time = 0
    waiting_time = [0] * n
    
    gantt_chart = []   #  Gantt Chart 

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    time += quantum
                    rem_bt[i] -= quantum
                    gantt_chart.append((processes[i], time))
                else:
                    time += rem_bt[i]
                    waiting_time[i] = time - burst_times[i]
                    gantt_chart.append((processes[i], time))
                    rem_bt[i] = 0
        if done:
            break

    turnaround_time = [burst_times[i] + waiting_time[i] for i in range(n)]

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for p, bt, wt, tat in zip(processes, burst_times, waiting_time, turnaround_time):
        print(f"{p}\t{bt}\t\t{wt}\t\t{tat}")

    # Gantt Chart 
    print("\nGantt Chart:")
    chart = "|"
    timeline = "0"
    prev_time = 0
    for p, t in gantt_chart:
        chart += f" P{p} |"
        timeline += f"{' ' * (len(chart) - len(timeline))}{t}"
        prev_time = t
    print(chart)
    print(timeline)


# Example run
processes = [1, 2, 3]
burst_times = [10, 4, 5]
quantum = 4

round_robin(processes, burst_times, quantum)
