import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = re.match(p, s)
        if match is not None:
            return match.group(0) == s

        return False