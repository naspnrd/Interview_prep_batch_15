# merge two lists

class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtEnd(self, data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            return
        curr = self.head
        while(curr.next is not None):
            curr = curr.next
        curr.next = newNode
    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.data),
            curr = curr.next
#Approach 1
# def mergeLists_1(headA, headB):
#     if(headA is None):
#         return headB
#     if(headB is None):
#         return headA
#     dummy = Node(0)
#     temp = dummy
#     currA = headA
#     currB = headB
#     while currA is not  None and currB is not None:
#         if currA.data < currB.data:
#             newNode = Node(currA.data)
#             temp.next = newNode
#             temp = temp.next
#             currA = currA.next
#         else:
#             newNode = Node(currB.data)
#             temp.next = newNode
#             temp = temp.next
#             currB = currB.next
#     while currA is not None:
#         newNode = Node(currA.data)
#         temp.next = newNode
#         temp = temp.next
#         currA = currA.next
#     while currB is not None:
#         newNode = Node(currB.data)
#         temp.next = newNode
#         temp = temp.next
#         currB = currB.next
#     return dummy.next

#Approach 2
def mergeLists_2(l1, l2):
    if(l1 is None):
        return l2
    if(l2 is None):
        return l1
    if l1.data > l2.data:
        l1, l2 = l2, l1
    res = l1
    while l1 is not None and l2 is not None:
        temp = None
        while l1 is not None and l1.data <= l2.data :
            temp = l1
            l1 = l1.next
        temp.next = l2
        l1, l2 = l2, l1
    return res

listA = LinkedList()
listB = LinkedList()

listA.insertAtEnd(5)
listA.insertAtEnd(7)
listA.insertAtEnd(9)

listB.insertAtEnd(3)
listB.insertAtEnd(4)
listB.insertAtEnd(8)
listB.insertAtEnd(10)

listA.head = mergeLists_2(listA.head, listB.head)
listA.printLinkedList()
