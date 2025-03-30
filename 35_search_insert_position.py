class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            previous = target - 1
            if previous in nums:
                return nums.index(previous) + 1

            while previous not in nums:
                previous -= 1

            return nums.index(previous) + 1
