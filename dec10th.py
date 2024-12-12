class Solution:
    def getMaxLength(self, subCount, k, max_length):
        for count in subCount.values():
            if count >= 3:
                return k
        return max_length
    def maximumLength(self, s: str) -> int:
        n = len(s)
        maxLength = -1
        subCount = {}
        for k in range(1, n + 1):
            for i in range(n - k + 1):
                substring = s[i:i + k]

                #e.g if we have "aaa" as a substring -> putting it in a set will just be {a}
                #dont consider substrings that arent special
                if len(set(substring)) == 1:
                    subCount[substring] = subCount.get(substring,0) + 1

            maxLength = self.getMaxLength(subCount, k, maxLength)
            subCount = {}
        return maxLength