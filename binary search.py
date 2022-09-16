#递归
def binarySearch (arr, item):
    n = len(arr)
    if n < 1:
        return False
    else:
        mid = n//2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            return binarySearch(arr[:mid], item)
        else:
            return binarySearch(arr[mid+1:], item)

"""
arr = [2, 3, 4, 10, 50,55]

result = binarySearch(arr, 10)
print(result)

result = binarySearch(arr, 22)
print(result)
"""



#循环
def binarysearch(arr, item):
    start = 0
    end = len(arr) -1
    index = None
    while start <= end:
        mid = (end+start)//2
        if item < arr[mid]:
            end = mid-1
        elif item > arr[mid]:
            start = mid+1
        elif item == arr[mid]:
            index = mid
            break
    return index


arr = [1,3,5,9,13,16,24,28]
result = binarysearch(arr,10)
print(result)