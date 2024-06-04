# Submission ID : 1277596525

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode() # dummy head node
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        
        cur = self.dummy_head.next # cur is real head node
        for i in range(index): # traversal
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        # real head node
        cur = ListNode(val, self.dummy_head.next)
        
        self.dummy_head.next = cur
        self.size += 1


    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        
        # when cur.next == None, cur points to the last node
        while cur.next != None:
            cur = cur.next

        cur.next = ListNode(val)

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 
        
        # if index = 0, add at head
        # if index = size, add at tail
        cur = self.dummy_head
        for i in range(index): 
            cur = cur.next
        cur.next = ListNode(val, cur.next)
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur = self.dummy_head
        for i in range(index): 
            cur = cur.next
        cur.next = cur.next.next

        self.size -= 1