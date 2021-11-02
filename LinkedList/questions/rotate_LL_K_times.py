class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None
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
def rotateList():
    global head
    global k
    len = 1
    if(head is None or head.next is None or k == 0):
        return head
    print("\nRotating the Linked List " + str(k) + " times"),
    curr = head
    while(curr.next is not None):
        len += 1
        curr = curr.next
    print("\nlen = " + str(len))
    k = k % len
    #pointing last node to first;
    curr.next = head
    #reset the curr is you want otherwose it will start from head as it now becoem circularr so
    #no changes if you delete is line also
    curr = head
    k = len - k - 1
    while(k > 0):
        curr = curr.next
        k -= 1
    #make the curr next node to head and break the connection;
    head = curr.next
    curr.next = None
    return head
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
insertAtEnd(7)
k = 3

print("before rotation "),
printLinkedList()

head = rotateList()
print("After rotation "),
printLinkedList()
