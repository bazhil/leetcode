class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) <= 0:
            return False

        dct = {}
        for ind, val in enumerate(nums):
            if val in dct:
                return dct[val], ind
            else:
                dct[target - val] = ind
