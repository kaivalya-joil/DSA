class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = len(s)
        subs = []
        best = 0 
        i= 0 
        while i < l:
            if s[i] not in subs :
                subs.append(s[i])
                cbest = len(subs)
                i = i + 1 
            else :
                subs.pop(0)

            if cbest>best :
                best = cbest 

        return best

