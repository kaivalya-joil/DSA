class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1 
        count = 0 
        if len(s) == 1 :
            if s[0] == " ":
                return 0
            elif s[0].isalpha():
                return 1 
        else:

            while i >= -len(s) and   s[i].isalpha() != True:
                i -= 1

            while i >= -len(s) and  s[i].isalpha():
                i -= 1 
                count += 1 
            
            return count