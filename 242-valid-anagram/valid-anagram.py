class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        if len(s)!= len(t):
            return False

        for i in range(len(s)):
            if s[i] not in t :
                return False 
            else:
                t.remove(s[i])
        
        return True 
        