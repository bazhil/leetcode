class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s) == 1:
            return s

        res = ""

        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i + 1)
            res = max(odd, even, res, key=len)

        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1:r]
