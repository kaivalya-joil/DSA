class Solution(object):
    def longestCommonPrefix(self, strs):
        
        ans=""
        for i in range(len(strs[0])):
            p = strs[0][i]

            for wrd in strs :
                if i < len(wrd) and wrd[i] == p :
                  pass  
                else :
                    return ans

            ans +=p
        
        return ans
            
            
        


              