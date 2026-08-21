class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
         
                
        for x in nums2 :
            nums1.append(x)
    
        q = quicksort(nums1)


        n = len(q)

        if n % 2 == 1:
            med = q[n // 2]
        else:
            mid = n // 2
            med = (q[mid - 1] + q[mid]) / 2.0
           

        return med

        
            
def quicksort(nums1):
    x = 0
    if len(nums1) <= 1:
            return nums1

    pivot = nums1[len(nums1)//2]

    right = [x for x in nums1 if x <pivot]
    left = [x for x in nums1 if x >pivot]
    middle =[x for x in nums1 if x == pivot] 
                
    return quicksort(left) + middle +  quicksort(right)

    
    
    
    
    

    
