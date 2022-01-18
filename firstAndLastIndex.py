def firstLastIndex(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            start = i
            while i+1 < len(arr) and arr[i+1] == x:
                i += 1
            return [start, i]
    return [-1, 1]


if __name__ == '__main__':
    print(firstLastIndex([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 4))
