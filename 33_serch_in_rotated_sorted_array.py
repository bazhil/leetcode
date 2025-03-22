class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        if target in nums:
            index = nums.index(target)

        return index
