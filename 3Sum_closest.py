class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        result = {"total": None, "diff": None}
        nums = sorted(nums)
        length = len(nums)

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = length - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                new_diff = abs(total - target)

                if not result["diff"] or result["diff"] > new_diff:
                    result["total"] = total
                    result["diff"] = new_diff

                if total == target:
                    return total
                elif total < target:
                    l += 1
                elif total > target:
                    r -= 1

        return result["total"]