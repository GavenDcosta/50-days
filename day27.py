#Leet Code

#Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = len(needle)
        for i in range(len(haystack)):
            if haystack[i:ans+i] == needle:
                return i
        return -1      

