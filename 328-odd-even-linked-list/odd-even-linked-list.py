# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        temp = head
        l = []
        while curr and curr.next:
            l += [curr.val]
            curr = curr.next.next
        if curr: # at end of list
            l += [curr.val]
        curr = head.next
        while curr and curr.next:
            l += [curr.val]
            curr = curr.next.next
        if curr:
            l += [curr.val]
        print(l)
        i = 0
        curr = head
        while curr:
            curr.val = l[i]
            curr = curr.next
            i += 1 
        return head