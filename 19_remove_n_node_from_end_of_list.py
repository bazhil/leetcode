# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        nodes = {}
        index = 0
        while head:
            nodes[index] = head
            head = head.next
            index += 1

        len_nodes = len(nodes)
        prev_pass = len_nodes - n - 1
        after_pass = prev_pass + 2

        if prev_pass < 0:
            return nodes[after_pass]
        if after_pass <= len_nodes - 1:
            nodes[prev_pass].next = nodes[after_pass]
        else:
            nodes[prev_pass].next = None

        return nodes[0]
