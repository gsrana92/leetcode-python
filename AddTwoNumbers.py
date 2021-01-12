class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Solution():
    def addTwoNumbers(self, l1, l2):
        """

        :param l1:  ListNode
        :param l2:  ListNode

        :return:
        """
        head = l3 = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.value
                l1 = l1.next

            if l2:
                carry += l2.value
                l2 = l2.next

            l3.value = carry % 10
            carry = carry // 10

            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next

        return head


