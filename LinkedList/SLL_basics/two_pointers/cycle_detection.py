#https://stackoverflow.com/questions/5130246/why-increase-pointer-by-two-while-finding-loop-in-linked-list-why-not-3-4-5

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
def createLoop():
    global head
    curr = head
    while(curr.next is not None):
        curr = curr.next
    curr.next = head.next
def findCycle():
    global head
    slow = head
    fast = head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False
def startOfCycle():
    global head
    slow = head
    fast = head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            slow = head
            while(slow != fast):
                slow = slow.next
                fast = fast.next
            return slow.data
    return "no cycle found"
def cycleLength():
    global head
    slow = head
    fast = head
    len = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            temp = fast
            while True:
                len += 1
                temp = temp.next
                if temp == fast:
                    break
            return len
    return "no cyle found"
#change in print function
def printLinkedList():
    curr = head
    while(curr):
        print(curr.data),
        curr = curr.next
        if(curr.next == head.next):
            print(curr.data)
            break

head = None
head = insertAtEnd(1)
insertAtEnd(2)
insertAtEnd(3)
insertAtEnd(4)
insertAtEnd(5)
createLoop()
printLinkedList()
print("cycle present : " + str(findCycle()))
print("starting point of the cycle " + str(startOfCycle()))
print("length of cycle = " + str(cycleLength()))