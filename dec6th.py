class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        set_banned = set(banned)

        result = 0
        for i in range(1,n+1):
            if i not in set_banned and maxSum-i >= 0:
                maxSum -= i
                result += 1

        return result
