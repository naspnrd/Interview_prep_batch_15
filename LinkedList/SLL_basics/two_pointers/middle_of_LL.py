#Approach 1 (code only if needed)
class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None
def lenLL():
    global head
    count = 0
    curr = head
    while(curr):
        count += 1
        curr = curr.next
    return count
# two traversal
def findMiddle1():
    len = lenLL()
    # len = len//2 - 1 if len % 2 == 0 else len//2
    len = len//2
    curr = head
    while(len > 0):
        curr = curr.next
        len -= 1
    return curr.data
# using Fast and Slow Pointer
def findMiddle2():
    slow = head
    fast = head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow.data
def insertAtEnd(data):
    global head
    newNode = Node(data)
    if head is None:
        return newNode
    curr = head
    while(curr.next is not None):
        curr = curr.next
    #now we are at last node , so we will attach to the last node
    curr.next = newNode
def printLinkedList():
    curr = head
    while(curr):
        print(curr.data),
        curr = curr.next

head = None
head = insertAtEnd(1)
insertAtEnd(2)
insertAtEnd(3)
insertAtEnd(4)
insertAtEnd(5)
insertAtEnd(6)
# insertAtEnd(7)
printLinkedList()

print("\nMiddle = " + str(findMiddle2()))

