class Solution(object):
    def maxSubArray(self, nums):

        curr = nums[0]
        
        btot = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            btot = max(btot, curr)

        return btot
            

        
        