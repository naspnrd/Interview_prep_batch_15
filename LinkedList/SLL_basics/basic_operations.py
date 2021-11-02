class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None
def insertAtBeginning(data):
    global head
    newNode = Node(data)
    # print("newNode = ", newNode)
    newNode.next = head
    head = newNode
    return head
def insertAtEnd(data):
    global head
    newNode = Node(data)
    if head is None:
        return newNode
    curr = head
    while(curr.next is not None):
        curr = curr.next
    curr.next = newNode
def deleteAtBeginning():
    global head
    if head is not None:
        head = head.next
def deleteAtEnd():
    global head
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None

def printLinkedList():
    global head
    curr = head
    # while(curr is not None):
    #     print(curr.data),
    #     if curr.next is not None:
    #         curr = curr.next.next
    #     else:
    #         break
    while curr:
        print(curr.data),
        curr = curr.next
    # print("curr ", curr.data)
head = None
# head = insertAtBeginning(30)
# # print("head 30 = ", head)
# head = insertAtBeginning(20)
# # print("head 20 = ", head)
# head = insertAtBeginning(10)
# head = insertAtBeginning(5)
head = insertAtEnd(5)
insertAtEnd(10)
insertAtEnd(15)
insertAtEnd(20)
insertAtEnd(25)
# print("before deleting"),
# printLinkedList()
# deleteAtBeginning()
# print("\nafter deleting"),
# printLinkedList()
# print("\nbefore deleting"),
# printLinkedList()
# deleteAtBeginning()
# print("\nafter deleting"),
# printLinkedList()
print("before deleting"),
printLinkedList()
deleteAtEnd()
print("\nafter deleting"),
printLinkedList()
print("\nbefore deleting"),
printLinkedList()
deleteAtEnd()
print("\nafter deleting"),
printLinkedList()