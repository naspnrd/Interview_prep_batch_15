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
    while(curr):
        count += 1
        curr = curr.next
    return count
def kthElement(k):
    global head
    len = findLength()
    print("\nlen = ", len),
    if(len < k):
        return
    k = len - k
    print("\nk = ", k),
    curr = head
    while(k):
        curr = curr.next
        k -= 1
    return curr.data
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
print("value = "+ str(kthElement(2)))