class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        pre = [False] * (n + 1)

        for num in nums:
            if 1 <= num <= n:
                pre[num] = True

        for i in range(1, n + 1):
            if not pre[i]:
                return i

        return n + 1