#Leet Code

#Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(n+1):
            if 3**i == n:
                return True
            if 3**i>n:
                return False    
        return False  
    

#Power of Four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n+1):
            if 4**i == n:
                return True
            if 4**i>n:
                return False    
        return False      