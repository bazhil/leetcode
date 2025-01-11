class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1 or len(set(strs)) == 1:
            return strs[0]

        empty_values = list(filter(lambda x: len(x) == 0, strs))
        if len(empty_values) > 0:
            return ""

        prefix_len = 1
        while prefix_len:
            prefixes = {i[:prefix_len] for i in strs}
            if len(prefixes) > 1:
                prefix_len -= 1
                break
            prefix_len += 1

        return strs[0][:prefix_len]
