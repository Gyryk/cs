global StackPointer # Integer
global StackData # Array

MaxLength = 10
StackData = [0 for i in range(MaxLength)]
StackPointer = 0

def PrintData():
    global StackData
    global StackPointer

    for n in range(len(StackData)):
        print(StackData[n])

    print("Stack Pointer:", StackPointer)

def Push(integer):
    global StackData
    global StackPointer

    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = integer
        StackPointer += 1
        return True
    
def Pop():
    global StackPointer
    global StackData

    if StackPointer == 0:
        return -1
    else:
        item = StackData[StackPointer -1]
        StackPointer -= 1
        return item

inx = 1
while inx <= 11:
    num = int(input("Please enter an integer: "))
    if Push(num):
        print("Number was successfully added to the stack")
    else:
        print("Stack is full, number not added")
    inx += 1
PrintData()

Pop()
Pop()
PrintData()
