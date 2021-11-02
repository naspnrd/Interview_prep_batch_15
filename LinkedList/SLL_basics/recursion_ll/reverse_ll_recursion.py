class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtEnd(data):
    global head
    newNode = Node(data)
    if head is None:
        head = newNode
        return
    curr = head
    while(curr.next is not None):
        curr = curr.next
    curr.next = newNode
# def reverseIterative():
#     global head
#     prev = None
#     curr = head
#     while curr is not None:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr =  nxt
#     return prev
def reverseRecursive(curr, prev):
    if curr is not None:
        nxt = curr.next
        curr.next = prev
        return reverseRecursive(nxt, curr)
    return prev
def printLinkedList():
    curr = head
    while curr is not None:
        print(curr.data),
        curr = curr.next
head = None
insertAtEnd(10)
insertAtEnd(20)
insertAtEnd(30)
insertAtEnd(40)
print("before reverse = "),
printLinkedList()
head = reverseRecursive(head, None)
print("\nafter reverse = "),
printLinkedList()
