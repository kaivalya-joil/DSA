class Solution(object):
    def reverse(self, x):
        
        rev = 0 
        sign = 1 
        temp = x 
        if x < 0 :
            sign = -1
            temp = temp *-1

        while temp >0 :
            
            
            digit = 0 
            digit = temp%10
            rev = rev*10 + digit
            temp = temp//10
        
        if rev >= (2**31)-1 or rev <= -2**31:
            return 0
        else :
            pass

        return sign*rev