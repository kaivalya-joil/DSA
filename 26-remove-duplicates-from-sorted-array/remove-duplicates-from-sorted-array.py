class Solution(object):
    def removeDuplicates(self, nums):
        
        dupe  = []
        k = 0 
        for i in range(len(nums)):
            
            if nums[i] not in dupe:
                dupe.append(nums[i])
                k = k+1

        for i in range(len(dupe)): 
            nums[i] = dupe[i]
        
        return len(dupe)
        
       