class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = nums
        for num in nums :
            if num == 0 :
                temp.remove(num)
                temp.append(num)

        nums = temp
        return nums