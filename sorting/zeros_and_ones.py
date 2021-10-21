#Approach 1
arr = [ 0, 1, 0, 1, 1, 0]
# def sort0and1(arr, n) :
# 	count = 0
# 	for i in range(0, n) :
# 		if (arr[i] == 0) :
# 			count += 1

# 	for i in range(0, count) :
# 		arr[i] = 0

# 	for i in range(count, n) :
# 		arr[i] = 1

# n = len(arr)
# print("before sorting " + str(arr)[1:-1])
# sort0and1(arr, n)

# print("After sorting " + str(arr)[1:-1])


#Approach 2

def sort0and1(arr, size):
    left = 0
    right = size-1
    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1

		# If left is smaller than right then there is a 1 at left
		# and a 0 at right. Exchange arr[left] and arr[right]
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

	return arr

n = len(arr)

print("before sorting " + str(arr)[1:-1])

sort0and1(arr, n)

print("After sorting " + str(arr)[1:-1])


