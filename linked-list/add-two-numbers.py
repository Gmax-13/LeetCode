# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head simplifies list creation and edge cases
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop continues if there are nodes left to process or a leftover carry
        while l1 or l2 or carry:
            # Extract values from current nodes, defaulting to 0 if a list is empty
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the single digit value
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next
        