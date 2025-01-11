class Solution:
    def intToRoman_v1(self, num: int) -> str:
        m_count = num // 1000
        c_count = (num - m_count * 1000) // 100
        x_count = (num - (m_count * 1000 + c_count * 100)) // 10
        i_count = (num - (m_count * 1000 + c_count * 100 + x_count * 10)) // 1

        roman = ""

        if m_count:
            roman += "M" * m_count

        if c_count:
            if c_count == 5:
                roman += "D"
            elif c_count < 5:
                roman += "CD" if c_count == 4 else "C" * c_count
            else:
                roman += "CM" if c_count == 9 else "D" + "C" * (c_count - 5)

        if x_count:
            if x_count == 5:
                roman += "L"
            elif x_count < 5:
                roman += "XL" if x_count == 4 else "X" * x_count
            else:
                roman += "XC" if x_count == 9 else "L" + "X" * (x_count - 5)

        if i_count:
            if i_count == 5:
                roman += "V"
            elif i_count < 5:
                roman += "IV" if i_count == 4 else "I" * i_count
            else:
                roman += "IX" if i_count == 9 else "V" + "I" * (i_count - 5)

        return roman

    def intToRoman(self, num: int) -> str:
        symbols = (
            ("I", 1), ("IV", 4), ("V", 5), ("IX", 9),
            ("X", 10), ("XL", 40), ("L", 50), ("XC", 90),
            ("C", 100), ("CD", 400), ("D", 500), ("CM", 900),
            ("M", 1000)
        )

        roman = ""
        for sym, val in reversed(symbols):
            count = num // val
            if count:
                roman += sym * count
                num = num % val

        return roman
