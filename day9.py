#Leet Code


#Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(50000):
            if i*i==num:
                return True
        else:
            return False


#Square root of a number

class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))