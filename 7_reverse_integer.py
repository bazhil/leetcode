class Solution:
    def reverse(self, x: int) -> int:
        valid_diapason = [-2**31, 2**31-1]

        if x == 0 or x < valid_diapason[0] or x > valid_diapason[1]:
            return 0

        str_int = str(x)
        if str_int[-1] == '0':
            str_int = str_int[:-1]

        reversed_str = str_int[::-1]
        if reversed_str[-1] == '-':
            reversed_str = reversed_str[-1] + reversed_str[:-1]

        result = int(reversed_str)
        if result < valid_diapason[0] or result > valid_diapason[1]:
            result = 0

        return result

if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))

