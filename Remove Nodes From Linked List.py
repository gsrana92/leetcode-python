def removeNodes(head, val):
    dummy = Node(next=head)
    prev, curr = dummy, head

    while curr:
        nxt = curr.next
        if curr.val == val:
            prev.next = nxt
        else:
            prev = curr
        curr = nxt

    return dummy.next