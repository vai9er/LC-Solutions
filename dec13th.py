class Solution:
    def makeHeap(self, nums):
        heap = []
        i = 0
        while i<len(nums):
            heap.append((nums[i], i))
            i+=1
        return heap
    def findScore(self, nums):
        result = 0

        #using a min-heap (need to keep popping smallest)
        heap = self.makeHeap(nums)
        heapq.heapify(heap)
        marked = [False] * len(nums)

        while heap:
            value, i = heapq.heappop(heap)
            if not marked[i]:
                result += value
                
                #mark the neighbours
                marked[i] = True
                if i-1 >= 0:
                    marked[i-1] = True
                if i+1 < len(nums):
                    marked[i+1] = True

        return result
