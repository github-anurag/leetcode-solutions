# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None
        
        # reverse list 2
        l2 = self.reverseList(l2)

        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        
        curr.next = l1

        return dummy.next
            
                
