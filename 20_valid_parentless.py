class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        revert_pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for i in s:
            if i in revert_pairs:
                if stack and stack[-1] == revert_pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)


        return not bool(stack)

