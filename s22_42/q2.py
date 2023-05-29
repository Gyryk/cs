import random


def printArr():
    for a in range(len(arr)):
        for b in range(len(arr[a])):
            print(arr[a][b], " ", end='')
        print("")


def BinarySearch(array, lower, upper, value):
    if upper >= lower:
        mid = (lower+(upper-1))//2
        if array[0][mid] == value:
            return mid
        elif array[0][mid] > value:
            return BinarySearch(array, lower, mid-1, value)
        else:
            return BinarySearch(array, mid+1, upper, value)
            
    return -1

arr = [[0]*10 for i in range(10)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = random.randint(1, 100)

print("Before:")
printArr()

arrLength = 10
for x in range(0, arrLength):
    for y in range(0, arrLength-1):
        for z in range(0, arrLength-y-1):
            if arr[x][z] > arr[x][z+1]:
                temp = arr[x][z]
                arr[x][z] = arr[x][z+1]
                arr[x][z+1] = temp

print("After:")
printArr()
print(BinarySearch(arr, 0, 10, int(input("Enter value 1: "))))
print(BinarySearch(arr, 0, 10, int(input("Enter value 2: "))))