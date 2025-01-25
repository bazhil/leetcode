# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        dummy = ListNode(0, head)

        prev, curr = dummy, head

        while curr and curr.next:
            nxt = curr.next.next
            scnd = curr.next

            scnd.next = curr
            curr.next = nxt
            prev.next = scnd

            prev = curr
            curr = nxt

        return dummy.next
