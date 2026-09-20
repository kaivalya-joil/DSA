class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0 
        l = len(s)
        s = list(s)
        m = []
        
        for ch in s :
            if ch.isalnum():
                m += ch.lower()
        k = list(m)
        m.reverse()
        if m == k :
            return True 
        else :
            return False
        

       
