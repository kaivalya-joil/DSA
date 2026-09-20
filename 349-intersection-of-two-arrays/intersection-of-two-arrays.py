class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = set(nums1)
        n2 = set(nums2)
        ans = []
        if len(n1) >len(n2):
            for num in n1 :
                if num in n2 :
                    ans.append(num)
        
        else:
            for num in n2 :
                if num in n1 :
                    ans.append(num)

        return ans