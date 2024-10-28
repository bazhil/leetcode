# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = curr = ListNode(0)
        cur_val = 0
        while l1 or l2 or cur_val:
            if l1:
                cur_val += l1.val
                l1 = l1.next
            if l2:
                cur_val += l2.val
                l2 = l2.next
            curr.next = ListNode(cur_val % 10)
            curr = curr.next
            cur_val = cur_val // 10

        return result_list.next
