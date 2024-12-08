class Solution:
    def maxTwoEvents(self, events):
        times = []

        for start, end, value in events:
            times.append((start, 1, value))
            times.append((end + 1, 0, value))

        #sort by the start time
        times.sort()

        ans, cur_max = 0, 0
        for t, is_start, v in times:
            if is_start:
                ans = max(ans, (v + cur_max))
            else:
                cur_max = max(cur_max, v)

        return ans
