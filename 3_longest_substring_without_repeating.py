class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(set(s)) == 1:
            return 1

        max_len = 0
        start = 0

        dct = {}

        for ind in range(len(s)):
            if s[ind] in dct and start <= dct[s[ind]]:
                start = dct[s[ind]] + 1
            else:
                max_len = max(max_len, ind - start + 1)
            dct[s[ind]] = ind

        return max_len
