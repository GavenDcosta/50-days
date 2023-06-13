#Leet Code

#Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k = 0,0,0  #initializing 3 pointers
        temp = nums1.copy() #saving the nums1 for later use

        #checking both the arrays and adding the lesser one to the nums1 array
        while i<m and j<n:    
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1     

        #adding the remaining elements to the nums1 array
        while i<m:
            nums1[k] = temp[i]
            i+=1
            k+=1
        while j<n:
            nums1[k] = nums2[j]
            j+=1
            k+=1

            