#Leet Code

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    ans.append(i)
                    ans.append(j)
                    return ans