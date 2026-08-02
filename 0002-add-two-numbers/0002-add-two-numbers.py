# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = head1
        curr2 = head2

        ans = ListNode(-1)
        curr3 = ans

        c = 0

        while curr1 or curr2:

            total = c
            c = 0

            if curr1:
                total += curr1.val
                curr1 = curr1.next

            if curr2:
                total += curr2.val
                curr2 = curr2.next

            if total >= 10:
                c = 1
                total -= 10

            curr3.next = ListNode(total)
            curr3 = curr3.next

        if c:
            curr3.next = ListNode(c)

        return ans.next



        