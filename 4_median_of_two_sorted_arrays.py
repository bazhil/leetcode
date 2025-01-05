class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if nums1 and nums2:
            median = self.find_median(nums1 + nums2)
        elif nums1 and not nums2:
            median = self.find_median(nums1)
        elif nums2 and not nums1:
            median = self.find_median(nums2)

        return median

    def find_median(self, arr):
        n = len(arr)

        # First we sort the array
        arr.sort()

        # check for even case
        if n % 2 != 0:
            return arr[n // 2]

        return (arr[(n - 1) // 2] + arr[n // 2]) / 2.0
