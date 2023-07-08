#Leet Code

#Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ram = list(set(nums))
        if len(ram)>=3:
            ram.sort(reverse=True)
            return ram[2]
        else:
            return max(ram)
        
        