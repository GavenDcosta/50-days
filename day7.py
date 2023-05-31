#Leet Code

#Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()
        return len(ans[-1])