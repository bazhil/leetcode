import random

class Solution:
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        """bad speed - timeout error"""
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        result = [
            list(tplt)
            for tplt in {tuple(sorted(random.sample(nums, 3))) for _ in range(len(nums) ** 3)}
            if sum(tplt) == 0
        ]

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """better speed"""
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        result = []
        nums = sorted(nums)
        length = len(nums)

        for i in range(length - 2):
            if i > 0 and nums[i]==nums[i-1]:
                continue

            l = i + 1
            r = length - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result
