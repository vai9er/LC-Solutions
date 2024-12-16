class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        left = count = 0
        elements = {}
        
        for right in range(len(nums)):
            elements[nums[right]] = elements.get(nums[right], 0) + 1
            minVal = min(elements)
            maxVal = max(elements)

            while maxVal - minVal > 2:
                elements[nums[left]] -= 1
                if elements[nums[left]] == 0:
                    del elements[nums[left]]
                left += 1

                if elements:
                    minVal = min(elements)
                    maxVal = max(elements)

            count += right - left + 1

        return count