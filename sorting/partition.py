arr = [7,2,1,6,8,5,3,4]
# arr = [1,4,2,4,4,2,1,1,1,2,4,4]
print(arr)

n = len(arr)
pivot = arr[n-1] # 4
pIndex = 0
for i in range(n-1):
    if(arr[i] <= pivot):
        #a , b = b, a
        arr[i],arr[pIndex] = arr[pIndex],arr[i]
        pIndex += 1
        print("After Swapping")
        print(arr)
print("swap pivot")
arr[n-1],arr[pIndex] = arr[pIndex],arr[n-1]

print(arr)