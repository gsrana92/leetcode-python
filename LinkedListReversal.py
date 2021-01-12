from __future__ import print_function


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def print_list(self):

        cur_node = self.head

        while cur_node:
            print(cur_node.data, end=' -> ')
            cur_node = cur_node.next

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print('Previous node is not in the list')
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None

        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node.next = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node.next = None

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print (name + " : " + node.data)

    def llist_reversed(self):
        curr_node = self.head
        prev_node = None

        if curr_node.next == None:
            return curr_node

        while curr_node :
            temp = curr_node.next
            curr_node.next = prev_node

            self.print_helper(prev_node, "PREV_NODE")
            self.print_helper(curr_node, "CURRENT")
            self.print_helper(temp, "TEMP")
            print ("\n")

            prev_node = curr_node
            curr_node = temp
        self.head = prev_node

    def nth_to_the_last_node(self, n, head):

        right_pointer = head
        left_pointer = head

        for i in range(n-1):
            if not right_pointer.next:
                raise LookupError('Error: n is larger than the linked list')
            right_pointer = right_pointer.next

        while right_pointer.next:
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next
        print (left_pointer.data)
        print ('\n')

        return left_pointer

    def reverse_to_kth_node(self, k, head):
        left = head
        right = head

        curr = head
        prev = None
        nextnode = None

        for i in range(k):
            right = right.next

        while left != right:
            left = left.next

            nextnode = curr.next
            curr.next = prev
            prev = curr

            curr = nextnode

        return prev


   




llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')
llist.insert_after_node(llist.head.next, 'G')
#llist.delete_node('D')
#llist.delete_node_at_pos(1)
#llist.llist_reversed()
#llist.reverse_to_kth_node(3, llist.head)
llist.nth_to_the_last_node(3,llist.head)
llist.print_list()
