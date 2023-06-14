#Leet Code

#Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       import statistics
       return statistics.median(nums1 + nums2)  
   

#Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
 
        current=dummy=ListNode()   #initialize 2 pointers pointing to the first node
        while list1 and list2:
             if list1.val < list2.val:
                 current.next = list1
                 list1 = list1.next
             else:
                 current.next = list2
                 list2 = list2.next
             current = current.next

        if list1: current.next = list1
        if list2: current.next = list2      
        return dummy.next   #dummy is pointing to the node before the first node
                            #so return dummy.next which is the actual head    
