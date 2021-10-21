#Approach 1

arr = [1, 20, 6, 7, 5, 8, 11, 3]
# arr = [5,4,3,2,1]
# temp_arr = [0]*(len(arr))
temp_arr = [] 
# def InversionCount(arr, n):
# 	count = 0
# 	for i in range(n):
# 		for j in range(i + 1, n):
# 			if (arr[i] > arr[j]):
# 				count += 1 # c operation
# 	return count

# print("Number of inversions are", InversionCount(arr, len(arr)))

#Approach 2

def mergeSort(arr, temp_arr, low, high):
    count = 0
    if low < high:
        mid = low + (high - low)/ 2
        count += mergeSort(arr,temp_arr,low,mid)
        count += mergeSort(arr,temp_arr,mid+1,high)
        count += merge(arr,temp_arr,low,mid,high)
    return count

def merge(arr, temp_arr, low, mid, high):
	i = low	 
	j = mid + 1 
	k = low 
	count = 0
	while i <= mid and j <= high:
		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			temp_arr[k] = arr[j]
			count += (mid - i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1
	while j <= high:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	# Copy the sorted subarray into Original array
	for i in range(low, high + 1):
		arr[i] = temp_arr[i]
		
	return count

print("Number of inversions are", mergeSort(arr, temp_arr, 0, len(arr)-1))
