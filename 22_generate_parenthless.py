class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        stack = []
        result = []

        def backtrack(open_cnt, close_cnt):
            if open_cnt == close_cnt == n:
                result.append("".join(stack))
                return

            if open_cnt < n:
                stack.append("(")
                backtrack(open_cnt + 1, close_cnt)
                stack.pop()

            if close_cnt < open_cnt:
                stack.append(")")
                backtrack(open_cnt, close_cnt + 1)
                stack.pop()

        backtrack(0, 0)

        return result
