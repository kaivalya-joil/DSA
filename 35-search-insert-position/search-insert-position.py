class Solution(object):
    def searchInsert(self, nums, target):
        i = 0 
        if target in nums :
            return nums.index(target)

        else :
            
            while i < len(nums) and nums[i] < target    :
                i= i+1 
            return i 
            
        
            
        return len(nums)