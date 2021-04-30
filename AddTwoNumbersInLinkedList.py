class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2):
    head = l3 = Node(0)

    carry = 0

    out = []

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        l3.val = carry % 10
        carry = carry // 10
        out.append(l3.val)

        if l1 or l2 or carry:
            l3.next = Node(0)
            l3 = l3.next

    return out


a = Node(2)
b = Node(4)
c = Node(3)
a.next = b
b.next = c

d = Node(5)
e = Node(6)
f = Node(4)
d.next = e
e.next = f

print(addTwoNumbers(a, d))
