#Leet Code

#Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            y = int(str(x)[::-1])
            return y if y < 2**31 else 0
        else:
            y = -int(str(x)[:0:-1])
            return y if y > -2**31 else 0  