class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        # error in leetcode testcase 12
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend

        result = 0
        is_negative = (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            decrement = divisor
            counter = 1
            while dividend >= decrement:
                dividend -= decrement
                result += counter
                counter += counter
                decrement += decrement

        valid_diapason = [0 - 2**31, 2**31 - 1]
        if result < valid_diapason[0]:
            return valid_diapason[0]
        elif result > valid_diapason[1]:
            return valid_diapason[1]

        return -result if is_negative else result
