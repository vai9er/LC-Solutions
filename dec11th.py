class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        numsSort = sorted(nums)
        beauty,left_ptr = 0,0

        for right_ptr in range(len(nums)):
            while numsSort[right_ptr] - numsSort[left_ptr] > 2*k:
                left_ptr += 1
            current_window_size = right_ptr - left_ptr + 1
            if current_window_size > beauty: beauty = current_window_size
        return beauty