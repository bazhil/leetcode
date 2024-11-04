class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Simple way (probably not right way, but leetcode tests is ok)
        m1 = reduce(lambda x, y: x + y, nums1) / len(nums1)
        m2 = reduce(lambda x, y: x + y, nums2) / len(nums2)

        return (m1 + m2) / 2

        #TODO: find better design
