class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        M = list(magazine)

        for ch in ransomNote:
            if ch in M :
                M.remove(ch)
            else:
                return False

        return True
        