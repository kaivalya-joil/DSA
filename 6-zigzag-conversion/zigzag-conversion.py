class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        ans = [""] * numRows
        j = 0
        direction = 1

        for ch in s:
            ans[j] += ch

            if j == 0:
                direction = 1
            elif j == numRows - 1:
                direction = -1

            j += direction

        return "".join(ans)
