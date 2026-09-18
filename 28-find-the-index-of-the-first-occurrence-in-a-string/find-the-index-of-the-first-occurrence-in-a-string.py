class Solution(object):
    def strStr(self, haystack, needle):
        h = haystack
        n = needle 
        l1 = len(h)
        l2 = len(n)
        i =0 
        
        if l2 > l1 :
            return -1 

        while i < l1 :
            j = 0 
            l = i 
            count = 0 
            while j < l2 and i <l1  and h[i] == n[j]  :
                j = j+1 
                i = i+1
                count += 1
                if count == l2 :
                    return l  
                
             
            else :
                i = l 
                i +=1 
        
        return -1 