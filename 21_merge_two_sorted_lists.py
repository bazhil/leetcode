# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if not left and not right:
            return None
        elif not left:
            return right
        elif not right:
            return left

        current = ListNode()
        result = current

        while left and right:
            if left.val < right.val:
                result.next = left
                left = left.next
            else:
                result.next = right
                right = right.next

            result = result.next

        if left:
            result.next = left
        elif right:
            result.next = right

        return current.next
