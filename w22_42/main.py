global NumberOfJobs # Integer
global Jobs # Array
Jobs = [[0]*2 for i in range(100)]


def Initialise():
    global NumberOfJobs
    global Jobs

    NumberOfJobs = 0
    for inx in range(len(Jobs)):
        Jobs[inx][0] = -1
        Jobs[inx][1] = -1


def AddJob(jobNum, priority):
    global Jobs
    global NumberOfJobs

    if NumberOfJobs < 100:
        Jobs[NumberOfJobs][0] = jobNum
        Jobs[NumberOfJobs][1] = priority
        NumberOfJobs += 1
        print('Added')
    else:
        print('Not Added')


def InsertionSort():
    global Jobs
    global NumberOfJobs

    for i in range(1, NumberOfJobs):
        curr1 = Jobs[i][0]
        curr2 = Jobs[i][1]
        while i > 0 and Jobs[i-1][1] > curr2:
            Jobs[i][0] = Jobs[i-1][0]
            Jobs[i][1] = Jobs[i-1][1]
            i -= 1
        Jobs[i][0] = curr1
        Jobs[i][1] = curr2


def PrintArray():
    global Jobs
    global NumberOfJobs
    for inx in range(0, NumberOfJobs):
        print(Jobs[inx][0], "Priority: ", Jobs[inx][1])

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
InsertionSort()
PrintArray()