def findSmallest(arr):
    smallest = arr [0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
array = [4,5,2,1,5,8,9,4,2,6,8,4,2,1,6,9,0,5,42,1,4,5523,4234,65767,2423,1332,677889,84453,56]
print (selectionSort(array))
