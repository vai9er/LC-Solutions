class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        special = [0] * len(nums)
        for i in range(1, len(nums)):
            special[i] = special[i-1] + (nums[i] % 2 != nums[i-1] % 2)
        
        result = []
        for start, end in queries:
            result.append(special[end] - special[start] == end - start)
        
        return result