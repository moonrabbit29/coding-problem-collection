# given an array of integers arr and an integer k, find the kth largest element

def kth_largest(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k:n]


if __name__ == "__main__":
    arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
    print(kth_largest(arr, 4))
