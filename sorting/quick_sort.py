arr = [2,1,3,8,7,5,4]

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start,end):
        if(arr[i] < pivot):
            #swapping
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex += 1
    arr[end],arr[pIndex] = arr[pIndex],arr[end]

    return pIndex

def quickSort(arr, start, end):
    if(start < end): 
        pivot = partition(arr,start,end)
        print("pivot element " + str(arr[pivot]) + " pivot index " + str(pivot))
        print("After partitioning " + str(arr[0:len(arr)]))
        quickSort(arr, start, pivot - 1) #left side
        quickSort(arr,pivot + 1, end)   #right side

print("Original array " + str(arr))

n = len(arr)

quickSort(arr, 0, n-1)

print("After Sorting" + str(arr))