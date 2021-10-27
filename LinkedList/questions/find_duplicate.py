# arr = [2,5,9,6,9,3,8,9,7,1]
arr = [1,3,4,2,2  ]
def findDuplicate():
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if(slow == fast):
            break
    slow = arr[0]
    while(slow != fast):
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

print("duplicate = " + str(findDuplicate()))