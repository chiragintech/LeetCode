# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        curr1 = l1
        while curr1:
            first = first + str(curr1.val)
            curr1 = curr1.next
        second = ""
        curr2 = l2
        while curr2:
            second = second + str(curr2.val)
            curr2 = curr2.next
        rev_ans = str(int(first[::-1]) + int(second[::-1]))
        head = ListNode(int(rev_ans[len(rev_ans)-1]))
        curr = head
        for i in range(len(rev_ans) - 2, -1, -1):
            curr.next = ListNode(int(rev_ans[i]))
            curr = curr.next
        return head