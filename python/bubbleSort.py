arr = [5, 2, 3, 9, 1, 0, 10]

upperBound = len(arr) - 1
swap = True
temp = 0

while swap or upperBound >= 0:
    for i in range(upperBound):
        swap = False
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            swap = True
    upperBound -= 1
    print(arr)
