class Node(object):

    def __init__(self, value):
        self.val = value
        self.next = None


def cycle_check(node):
    marker1 = marker2 = node

    while marker1 is not None and marker2 is not None:
        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True
    return False


def linkedList_reversal(head):
    current = head
    previous = None
    next = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous

def reverse_to_nth_node(node):
    


def print_linkedList(node):
    while node.next is not None:
        print(node.val, end=' ->')
        node = node.next
    print(node.val)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
# d.next = a

# print(cycle_check(a))

print('Before reversal:')
print_linkedList(a)

print('\n')
print('After reversal:')
print(linkedList_reversal(a))
print_linkedList(d)
