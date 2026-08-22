class Solution(object):
    def isPalindrome(self, x):
        num = x
        reverse_num = 0

        while num > 0:
            digit = num % 10
            reverse_num = reverse_num * 10 + digit
            num //= 10

        if x == reverse_num:
            return True
        else:
            return False