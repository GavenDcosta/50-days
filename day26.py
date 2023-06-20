#Leet Code

#Check if the Number is Facinating

class Solution:
    def isFascinating(self, n: int) -> bool:
        concat = str(n) + str(2*n) + str(3*n)
        if '0' in concat:
            return False
        if len(concat)>9:
            return False
        for i in range(1,10):
            if str(i) not in concat:
                return False
        return True 