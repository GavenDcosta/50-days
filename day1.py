#Leet code

#day 1

#Given an integer x, return true if x is a 
#palindrome
#, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False    