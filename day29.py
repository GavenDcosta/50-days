#Leet Code

#Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = int(num1) * int(num2)
        return str(a)
    
 
#Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                 matrix[i][j] , matrix[j][i]= matrix[j][i] , matrix[i][j]    
    
    