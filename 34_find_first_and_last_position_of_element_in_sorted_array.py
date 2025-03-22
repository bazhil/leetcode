class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if len(nums) == 0:
            return result

        if target in nums:
            first = nums.index(target)
            result[0] = first
            result[-1] = first

            count = nums.count(target)
            if count > 1:
                reversed_nums = nums[::-1]
                last = reversed_nums.index(target)
                result[-1] = (len(reversed_nums) - 1) - last

        return result
