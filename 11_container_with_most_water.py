class Solution:
    def maxArea(self, height: List[int]) -> int:
        amount = 0

        l = 0
        r = len(height) - 1

        while l < r:
            l_val = height[l]
            r_val = height[r]

            new_amount = (r - l) * min(l_val, r_val)
            if new_amount > amount:
                amount = new_amount

            if l_val < r_val:
                l += 1
            else:
                r -= 1

        return amount
