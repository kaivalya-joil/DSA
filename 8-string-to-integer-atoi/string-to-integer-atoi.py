
class Solution(object):
    def myAtoi(self, s):

        t = ""
        sign = 1
        start = 0

        for i in range(len(s)):
            if s[i] != " ":
                start = i
                break

        if start < len(s) and s[start] == "-":
            sign = -1
            start += 1
        elif start < len(s) and s[start] == "+":
            start += 1

        for i in range(start, len(s)):
            if s[i].isdigit():
                t += s[i]
            else:
                break

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

