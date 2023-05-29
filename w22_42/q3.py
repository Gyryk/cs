global Queue # Array
global headPointer # Integer
global tailPointer # Integer

Queue = [-1 for i in range(100)]
headPointer = -1
tailPointer = 0

def Enqueue(value):
    global Queue
    global tailPointer
    global headPointer

    if tailPointer < 100:
        if headPointer == -1:
            headPointer = 0
        Queue[tailPointer] = value
        tailPointer += 1
        return True
    else:
        return False
    
def RecursiveOutput(start):
    global Queue

    if start == 0:
        return Queue[start]
    else:
        return Queue[start] + RecursiveOutput(start-1)
    
allQueued = False
for x in range(1, 21):
    allQueued = Enqueue(x)

if allQueued:
    print('Successful')
else:
    print('Unsuccessful')

print(RecursiveOutput(19))
