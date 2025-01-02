class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        valid_diapason = [0 - 2 ** 31, 2 ** 31 - 1]
        if x <= valid_diapason[0] or x >= valid_diapason[1]:
            return False

        str_x = str(x)

        return str_x[::-1] == str_x
