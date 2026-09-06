class Solution(object):
    def myAtoi(self, s):

        t = ""
        sign = 1
        i = 0

        
        while i < len(s) and s[i] == " ":
            i += 1

        
        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1

        
        while i < len(s) and s[i].isdigit():
            t += s[i]
            i += 1

       
        if t == "":
            return 0

        num = 0

        for i in range(len(t)):
            num = num * 10 + int(t[i])

        num = num * sign

       
        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return num