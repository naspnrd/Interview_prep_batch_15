
class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def insert(data):
    global head
    newNode = Node(data)
    if head is None:
        head = newNode
        return
    newNode.next = head
    head.prev = newNode
    head = newNode
def printList():
    global head
    curr = head
    while curr:
        print(curr.data),
        curr = curr.next
head = None
insert(5)
insert(4)
insert(3)
insert(2)
insert(1)
printList()