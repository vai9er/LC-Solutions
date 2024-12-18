class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for i in range(k):
            minNums = min(nums)
            nums[nums.index(minNums)] = minNums * multiplier
        return nums