if __name__ == '__main__':
    no_process = 0
    no_process = int(input("Enter no of process:"))
    process = []
    burst_time = []
    waiting_time = []
    turn_around_time=[]
    # taking values
    for i in range(no_process):
        x = int(input("Enter Process:"))
        process.append(x)
        y = int(input("Enter Burst Time: "))
        burst_time.append(y)

    # Printing values
    print()
    print("executing")

    # calculating waiting time
    x = 0
    waiting_time.append(x)
    for i in range(1, no_process):
        x = burst_time[i - 1] + waiting_time[i - 1]
        waiting_time.append(x)


    # Calculating Turn Around Time
    for i in range(0,no_process):
        x=burst_time[i]+waiting_time[i]
        turn_around_time.append(x)
    #calculating avg waiting and turn around time
    avgwt=0
    avgtat=0
    for i in range(0, no_process):
        avgwt=avgwt+waiting_time[i]
        avgtat=avgtat+turn_around_time[i]

    avgtat=avgtat/no_process
    avgwt=avgwt/no_process

    # printing Turn around Time and waiting
    print()
    for i in range(0, no_process):
        print("Process=", process[i])
        print("Burst Time=", burst_time[i])
        print("Waiting Time=", waiting_time[i])
        print("Turn Around Time=",turn_around_time[i])

    print()
    print("Average Waiting Time=",avgwt)
    print("Average Turn Around Time=",avgtat)