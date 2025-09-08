# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None 
        c = 0
        temp = head
        while temp:
            c += 1
            temp = temp.next
        if c == n:
            return head.next
        res = c - n
        temp = head
        for _ in range(res - 1):
            temp = temp.next
        temp.next = temp.next.next
        
        return head


            