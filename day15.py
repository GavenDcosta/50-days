#Leet Code

#Average Salary Excluding the Minimum and Maximum Salary

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = 0
        avg = 0
        count = 0
        for i in range(1,len(salary)-1):
            total+=salary[i]
            count+=1
            avg = total/count
        return avg    
