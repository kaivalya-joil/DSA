class Solution(object):
    def removeElement(self, nums, val):
        rem = []
        for i  in range(len(nums)):
            if nums[i] == val:
                pass
            else :
                rem.append(nums[i])

        for i in range(len(rem)):
            nums[i] = rem[i]
        

        return len(rem)