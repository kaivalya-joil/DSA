class Solution(object):
    # kai
    def twoSum(self, nums, target):
        l = len(nums)
        answer = []
        
        for i in range (0,l):
            
            for j in range(i+1,l):
                 
                    if nums[i]+nums[j]==target:
                        answer.append(i)
                        answer.append(j)
                        
        return answer 

nums = [2,7,11,15]
target = 9

                    
twosum = Solution()
answer = twosum.twoSum(nums, target)
print(answer)
        