# Selection sort

def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[minIdx]):
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr


def insertionSort(arr):
    for i in range(len(arr)):
        j = i-1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


def binarySearch(arr, x):
    mid = int((len(arr)) / 2)
    while(mid >= 0 and mid <= (len(arr)-1)):
        if arr[mid] > x:
            mid = int(mid/2)
        elif arr[mid] < x:
            mid = int((mid + len(arr) + 1)/2)
        else:
            return mid
    return "not found"


if __name__ == "__main__":
    print(insertionSort([1, 3, 4, 0, 1, 2, 11, 9, 10]))
    print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 9))
