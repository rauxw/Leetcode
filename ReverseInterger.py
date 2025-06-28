class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        number = int(str(abs(x))[::-1]) * sign

        if number > (2**31) - 1 or number < -2**31:
            return 0
        
        return number
        
        