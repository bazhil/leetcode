class Solution:
    def myAtoi(self, s: str) -> int:
        valid_diapason = [0 - 2 ** 31, 2 ** 31 - 1]
        valid_chars = [' ', '+', '-']
        result = ''
        is_negative = False

        if not s or len(s) == 1 and not s.isdigit():
            return 0

        for i in range(len(s)):
            char = s[i]
            if not char.isdigit() and not char in valid_chars or result and not char.isdigit():
                break
            elif char == ' ':
                continue
            elif char in ['-', '+']:
                next_char = s[i+1]
                if not next_char.isdigit():
                    break
                if char == '-':
                    is_negative = True
                continue
            else:
                result += char

        if not result:
            return 0
        else:
            result = int(result)
            if is_negative:
                result = -result

        if result < valid_diapason[0] or result > valid_diapason[1]:
            return valid_diapason[0] if is_negative else valid_diapason[1]

        return result


if __name__ == '__main__':
    print(Solution().myAtoi("42"))
    print(Solution().myAtoi(" -042"))
    print(Solution().myAtoi("1337c0d3"))
    print(Solution().myAtoi("0-1"))
    print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("3.14159"))
    print(Solution().myAtoi("+-12"))
    print(Solution().myAtoi("-+12"))
    print(Solution().myAtoi("+1"))