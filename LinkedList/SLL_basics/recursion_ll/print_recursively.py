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
# def printRecursiveLR(curr):
#     if curr is not None:
#         print(curr.data),
#         printRecursiveLR(curr.next)

def printRecursionRL(curr):
    if curr is not None:
        printRecursionRL(curr.next) #1
        print(curr.data), # 2
head = None
insertAtEnd(10)
insertAtEnd(20)
insertAtEnd(30)
insertAtEnd(40)
# printRecursiveLR(head)
printRecursionRL(head)