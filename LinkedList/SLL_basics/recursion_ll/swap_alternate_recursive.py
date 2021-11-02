
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
def swapPair(head):
    if head is None or head.next is None:
        return head
    prev = head
    curr = head.next
    nxt = curr.next
    prev.next = nxt
    curr.next = prev
    if nxt is not None:
        prev.next = swapPair(nxt)
    return curr
def printLinkedList():
    curr = head
    while curr:
        print(curr.data),
        curr = curr.next
head = None
insertAtEnd(1)
insertAtEnd(2)
insertAtEnd(3)
insertAtEnd(4)
insertAtEnd(5)
print("before swap = "),
printLinkedList()
head = swapPair(head)
print("\nAfter Swap = "),
printLinkedList()