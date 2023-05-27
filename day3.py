#Leet code

#Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        n = len(s)
        i = n-1
        ans = 0
        while(i>=0):
            if(i < n-1 and Roman[s[i]] < Roman[s[i+1]]):
                ans -= Roman[s[i]]
            else:
                ans += Roman[s[i]]
            i-=1        

        return ans 