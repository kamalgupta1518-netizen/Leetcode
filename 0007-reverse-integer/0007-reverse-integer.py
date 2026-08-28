class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_val = int(str(abs(x))[::-1]) * sign
        if reversed_val < -2**31 or reversed_val > 2**31 - 1:
            return 0
        return reversed_val

        