# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes left
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
            
        if count < k:
            return head
            
        # Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # head is now the tail of the reversed group; recursively reverse the rest
        head.next = self.reverseKGroup(curr, k)
        return prev
        