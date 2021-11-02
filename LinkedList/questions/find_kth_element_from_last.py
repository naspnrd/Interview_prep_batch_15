class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None
def insertAtEnd(data):
    global head 
    newNode = Node(data)
    if(head is None):
        return newNode
    curr = head
    while(curr.next is not None):
        curr = curr.next
    #now we are at last node , so we will attach to the last node
    curr.next = newNode
def findLength():
    global head
    count = 0
    curr = head
    while(curr is not None):
        count += 1
        curr = curr.next
    return count
# def kthElement_1(k):
#     global head
#     len = findLength() # 5
#     if(len < k):
#         return
#     k = len - k # 5 -3 = 2
#     curr = head
#     while(k):
#         curr = curr.next
#         k -= 1
#     return curr.data

# Approach 2

def KthElement_2(k):
    global head
    first = head
    second = head
    while(k):
        if first == None:
            return
        first = first.next
        k -= 1
    
    while first is not None:
        second = second.next
        first = first.next
    
    return second.data

def printLinkedList():
    curr = head
    while(curr is not None):
        print(curr.data),
        curr = curr.next 
head = None
head = insertAtEnd(10)
insertAtEnd(20)
insertAtEnd(30)
insertAtEnd(40)
insertAtEnd(50)
printLinkedList()
print("\nvalue = "+ str(kthElement_1(2)))

