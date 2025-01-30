class Solution:
    # first version
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     for i in nums:
    #         while nums.count(i) > 1:
    #             nums.remove(i)
    #
    #     return len(nums)

    #second version
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums.count(nums[i]) > 1:
                nums.remove(nums[i])
            else:
                i += 1

        return len(nums)

