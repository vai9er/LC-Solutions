import math
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                resultToAdd = -1
                if prices[j] <= prices[i]:
                    resultToAdd = prices[i] - prices[j]
                    break
            
            if resultToAdd == -1: result.append(prices[i])
            else: result.append(resultToAdd)
                
        result.append(prices[-1])
        return result