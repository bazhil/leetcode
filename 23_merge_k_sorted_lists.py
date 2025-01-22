# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        # code from leetcode_21 - merge 2 sorted lists
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or (len(lists) == 1 and lists[0] == []):
            return ListNode().next

        if len(lists) == 1:
            return lists[0]

        #first try
        # while len(lists) != 1:
        #     lists[0] = self.mergeTwoLists(lists[0], lists[1])
        #     lists.pop(1)

        # second try
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists

        return lists[0]
