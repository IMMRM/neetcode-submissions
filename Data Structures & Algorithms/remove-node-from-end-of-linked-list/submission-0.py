# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        fast=slow=dummy
        # step 1: Move fast pointer to n+1 steps (to ensure n+1 gap is there between slow and fast)
        for _ in range(n+1):
            fast=fast.next
        # step 2: Move until fast reaches null
        while(fast):
            fast=fast.next
            slow=slow.next
        
        # step 3: Remap the pointers
        slow.next=slow.next.next

        return dummy.next
    
        

        