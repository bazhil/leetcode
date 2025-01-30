class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in nums:
            while nums.count(i) > 1:
                nums.remove(i)

        return len(nums)
