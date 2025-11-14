#include <bits/stdc++.h>
using namespace std;

// ==================== COMMON FUNCTIONS ====================
void findWaitingTime(int n, int bt[], int wt[]) {
    wt[0] = 0;
    for (int i = 1; i < n; i++)
        wt[i] = bt[i - 1] + wt[i - 1];
}

void findTurnAroundTime(int n, int bt[], int wt[], int tat[]) {
    for (int i = 0; i < n; i++)
        tat[i] = bt[i] + wt[i];
}

void printAndAverage(int pid[], int n, int bt[], int wt[], int tat[]) {
    int total_wt = 0, total_tat = 0;
    cout << "\nP\tBT\tWT\tTAT\n";
    for (int i = 0; i < n; i++) {
        total_wt += wt[i];
        total_tat += tat[i];
        cout << "P" << pid[i] << "\t" << bt[i] << "\t" << wt[i] << "\t" << tat[i] << endl;
    }
    cout << "\nAverage Waiting Time = " << (float)total_wt / n;
    cout << "\nAverage Turn Around Time = " << (float)total_tat / n << endl;
}

// ==================== FCFS ====================
void FCFS(int n) {
    int pid[n], bt[n], wt[n], tat[n];
    cout << "Enter Burst Time:\n";
    for (int i = 0; i < n; i++) {
        cout << "P" << i + 1 << ": ";
        pid[i] = i + 1;
        cin >> bt[i];
    }
    findWaitingTime(n, bt, wt);
    findTurnAroundTime(n, bt, wt, tat);
    printAndAverage(pid, n, bt, wt, tat);
}

// ==================== SJF ====================
void SJF(int n) {
    int pid[n], bt[n], wt[n], tat[n];
    cout << "Enter Burst Time:\n";
    for (int i = 0; i < n; i++) {
        cout << "P" << i + 1 << ": ";
        pid[i] = i + 1;
        cin >> bt[i];
    }
    // Sorting by burst time (Selection Sort)
    for (int i = 0; i < n; i++) {
        int index = i;
        for (int j = i + 1; j < n; j++) {
            if (bt[j] < bt[index])
                index = j;
        }
        swap(bt[i], bt[index]);
        swap(pid[i], pid[index]);
    }

    findWaitingTime(n, bt, wt);
    findTurnAroundTime(n, bt, wt, tat);
    printAndAverage(pid, n, bt, wt, tat);
}

// ==================== Priority ====================
void PriorityScheduling(int n) {
    int pid[n], bt[n], priority[n], wt[n], tat[n];
    cout << "Enter Burst Time and Priority (higher number = higher priority):\n";
    for (int i = 0; i < n; i++) {
        pid[i] = i + 1;
        cout << "P" << pid[i] << " BT: ";
        cin >> bt[i];
        cout << "P" << pid[i] << " Priority: ";
        cin >> priority[i];
    }
    
    // Sorting by priority (higher first)
    for (int i = 0; i < n; i++) {
        int index = i;
        for (int j = i + 1; j < n; j++) {
            if (priority[j] > priority[index])
                index = j;
        }
        swap(priority[i], priority[index]);
        swap(bt[i], bt[index]);
        swap(pid[i], pid[index]);
    }

    findWaitingTime(n, bt, wt);
    findTurnAroundTime(n, bt, wt, tat);
    cout << "Order of execution: ";
    for(int i=0;i<n;i++) cout << "P" << pid[i] << " ";
    cout << endl;
    printAndAverage(pid, n, bt, wt, tat);
}

// ==================== Round Robin ====================
void RoundRobin(int n) {
    int pid[n], bt[n], wt[n], tat[n], quantum;
    cout << "Enter Burst Time:\n";
    for (int i = 0; i < n; i++) {
        cout << "P" << i + 1 << ": ";
        pid[i] = i + 1;
        cin >> bt[i];
    }
    cout << "Enter Quantum Time: ";
    cin >> quantum;

    int rem_bt[n];
    for (int i = 0; i < n; i++) rem_bt[i] = bt[i];
    int t = 0;
    while(true) {
        bool done = true;
        for(int i=0;i<n;i++){
            if(rem_bt[i]>0){
                done=false;
                if(rem_bt[i]>quantum){
                    t+=quantum;
                    rem_bt[i]-=quantum;
                } else {
                    t+=rem_bt[i];
                    wt[i]=t-bt[i];
                    rem_bt[i]=0;
                }
            }
        }
        if(done) break;
    }
    findTurnAroundTime(n, bt, wt, tat);
    printAndAverage(pid, n, bt, wt, tat);
}

// ==================== MAIN ====================
int main() {
    int choice, n;
    cout << "Enter number of processes: ";
    cin >> n;

    cout << "\nChoose Scheduling Algorithm:\n";
    cout << "1. FCFS\n2. SJF\n3. Priority\n4. Round Robin\n";
    cout << "Enter your choice: ";
    cin >> choice;

    switch(choice) {
        case 1: FCFS(n); break;
        case 2: SJF(n); break;
        case 3: PriorityScheduling(n); break;
        case 4: RoundRobin(n); break;
        default: cout << "Invalid choice!\n";
    }

    return 0;
}