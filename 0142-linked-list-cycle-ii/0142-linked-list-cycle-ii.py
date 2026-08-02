# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        hascycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                hascycle = True
                break

        if not hascycle:
            return None

        # Find cycle length
        l = 1
        fast = fast.next

        while fast != slow:
            l += 1
            fast = fast.next

        slow = head
        fast = head

        # Move fast l steps ahead
        for _ in range(l):
            fast = fast.next

        # Move both together
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow




        