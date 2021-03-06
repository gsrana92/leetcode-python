"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(n, head):
    fast = slow = head

    for i in range(n):
        fast = fast.next

    if fast is None:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


def printList(head):
    while head.next:
        print(head.val, end='->')
        head = head.next
    print(head.val)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(removeNthFromEnd(2, a))
printList(a)
