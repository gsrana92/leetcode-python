"""
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100


Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def swapNodes(head):
    if not head or not head.next:
        return head

    prev = None
    curr = head
    nxt = curr.next
    newhead = nxt.next

    while curr and nxt:
        #SWAPPING NODES
        curr.next = nxt.next
        nxt.next = curr
        if prev:
            prev.next = nxt

        #ADVANCING POINTERS
        prev = curr
        curr = curr.next
        if curr:
            nxt = curr.next
    return newhead

def printList(head):
    while head.next:
        print(head.val, end='->')
        head = head.next
    print(head.val)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print(swapNodes(a))
printList(b)

