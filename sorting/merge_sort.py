arr = [3,7,1,8,2,5,9,4,6,10]

def merge(arr, startL, endL, startR, endR):
    temp = []
    i = startL
    j = startR
    while(i <= endL and j <= endR):
        if(arr[i] > arr[j]):
            temp.append(arr[j])
            j += 1
        else:
            temp.append(arr[i])
            i += 1
    while(i <= endL):
        temp.append(arr[i])
        i += 1
    while(j <= endR):
        temp.append(arr[j])
        j += 1
    for i in range(len(temp)):
        arr[startL + i] = temp[i] 
def mergeSort(arr, start, end): 
    if(start < end):
        #print("Trying to sort " + str(arr[start:end + 1]))
        mid = (start + end)//2 # (0 + 9)//2 = 4 0 to 4 5 to 9
        mergeSort(arr,start,mid) #0 to 4
        mergeSort(arr,mid + 1, end) # 5 to 9
        #print("Merging " + str(arr[start : mid + 1]) + " and " + str(arr[mid + 1: end + 1]))
        merge(arr, start, mid, mid+1, end)

mergeSort(arr, 0, len(arr) - 1)
print(arr)