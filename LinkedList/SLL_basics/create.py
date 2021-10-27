class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(5) #create me a node with value 5 and node nameis first

#print
# print(first.data)
# print(first.next)
# print(first)

second = Node(10)
third = Node(15)
fourth = Node(20)
# print(first)
# print(second)
# print(third)
# print(fourth)
head = first
# print("head ", head)
first.next = second
second.next = third
third.next = fourth

#traverse
def printLinkedList():
    curr = head
    while(curr is not None):
        print(curr.data),
        curr = curr.next #i++
printLinkedList()