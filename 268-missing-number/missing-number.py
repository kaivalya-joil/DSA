class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(nums[-1]+2):
            if i not in nums :
                return i 
      