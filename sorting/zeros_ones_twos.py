#Approach 1

# arr = [ 0, 2, 0, 1, 0, 1, 2]
arr = [2,0,2,1,1,0]
# def sort012(arr, n):
#     print("hi")
#     count0 = 0
#     count1 = 0
#     count2 = 0
#     for i in range(0,n):
#         if (arr[i] == 0):
#             count0 = count0 + 1
#         elif (arr[i] == 1):
#             count1 = count1 + 1
#         elif (arr[i] == 2):
#             count2 = count2 + 1
#     i = 0
#     while(count0):
#         arr[i] = 0
#         i += 1
#         count0 -= 1
#     while(count1):
#         arr[i] = 1
#         i += 1
#         count1 -= 1
#     while(count2):
#         arr[i] = 2
#         i += 1e
#         count2 -= 1
#     return

# n = len(arr)
# print("before sorting " + str(arr)[1:-1])

# sort012(arr, n)

# print("After sorting " + str(arr)[1:-1])


#Approach - 2
def sort012(arr, n):
    low = 0
    mid = 0
    high = n - 1
    while(high >= mid):
        if(arr[mid] == 0):
            arr[low],arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif(arr[mid] == 1):
            mid += 1
        elif(arr[mid] == 2):
            arr[mid],arr[high] = arr[high], arr[mid]
            high -= 1
        # print("Inside loop: mid =  " + str(mid) + " "+ str(arr))
    return 0
n = len(arr)
print("before sorting = " + str(arr))

sort012(arr, n)

print("After sorting = " + str(arr))

