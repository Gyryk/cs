# Input data for binary search
array = [1, 2, 3, 5, 6, 7, 9, 10]

lowerBound = 0
upperBound = len(array) - 1
number = int(input("num: "))

def binSearch(low, up, arr, num):
    # Narrowing the search field with each search till value obtained
    while low < up:
        i = low + (up - 1)//2

        if arr[i] == num:
            return i
        elif arr[i] < num:
            low = i + 1
        else:
            up = i - 1

    return -1


# Outputting index of the search value
res = binSearch(lowerBound, upperBound, array, number)
if res != -1:
    print(res)
else:
    print(number, "not found")
