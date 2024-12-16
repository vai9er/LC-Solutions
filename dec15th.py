import heapq
from typing import List

class Solution:
    def incrementalGain(self, passed: int, total: int) -> float:
            currentRatio= passed/total
            newRatio = (passed + 1)/(total + 1)
            return newRatio - currentRatio

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        maxHeap = []
        for p, t in classes:
            gain =self.incrementalGain(p,t)

            #largest gain is the smallest negative number
            heapq.heappush(maxHeap,(-gain,p,t))

        i = 0
        while i < extraStudents:
            negGain, p, t = heapq.heappop(maxHeap)
            p += 1
            t += 1
            updatedGain = self.incrementalGain(p, t)
            heapq.heappush(maxHeap,(-updatedGain, p, t))
            i+=1

        totalRatioSum = 0.0
        i = 0
        for i, p, t in maxHeap:
            totalRatioSum += p/t

        return totalRatioSum/len(classes)
        