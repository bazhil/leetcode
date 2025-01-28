# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head

        dummy = ListNode(0, head)

        prev_group = dummy

        while True:
            kth = self.get_k(prev_group, k)
            if not kth:
                break

            next_group = kth.next

            prev, curr = kth.next, prev_group.next

            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        return dummy.next

    def get_k(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
