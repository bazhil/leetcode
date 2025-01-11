class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        values = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        if len(s) == 1:
            return values[s]

        for i in range(len(s)):
            if s[i] == "M":
                result += 1000
            elif s[i] == "D":
                result += 500
            elif s[i] == "C":
                if i + 1 < len(s) and s[i + 1] in ["D", "M"]:
                    result -= 100
                else:
                    result += 100
            elif s[i] == "L":
                result += 50
            elif s[i] == "X":
                if i + 1 < len(s) and s[i + 1] in ["L", "C"]:
                    result -= 10
                else:
                    result += 10
            elif s[i] == "V":
                result += 5
            elif s[i] == "I":
                if i + 1 < len(s) and s[i + 1] in ["X", "V"]:
                    result -= 1
                else:
                    result += 1

        return result
