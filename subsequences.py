# basically the test would give you two arrays
# let's say array1 and array2
# then you are ask to make a function to determine if array2 a subsequence of the first array
# the order of occurrence must be the same
# and it will return true if condition are meet and false if doesn't
# EG-1 :
#  array1 = [1,2,3,4,5]
#  array2 = [1,2,3]
# result : true
# EG-2 :
# array1 = [1,3,2,4,5]
# array2 = [1,2,3]
#  result : false

def test2(arr1, arr2):
    b = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[b]:
            b += 1
            if len(arr2) == b:
                return True

    return False


if __name__ == "__main__":
    print(test2([1, 3, 2, 5, 8, 2, 3],  [1, 2, 3]))
