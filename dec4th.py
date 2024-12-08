class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        i= 0
        j = 0
        alphabet = list("abcdefghijklmnopqrstuvwxyz")

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                j += 1
            else:
                prev_char = alphabet[(alphabet.index(str2[j]) - 1) % 26]
                if str1[i] == prev_char:
                    j += 1
            i += 1

        return j == len(str2)
