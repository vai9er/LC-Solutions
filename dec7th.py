class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(max_balls):
            operations = 0
            for num in nums:
                if num > max_balls:
                    operations += (num - 1) // max_balls
            return operations <= maxOperations

        left = 1
        right = max(nums)
        while left < right:
            if canDivide((left + right) // 2):
                right = (left + right) // 2
            else:
                left = ((left + right) // 2) + 1
        return left
