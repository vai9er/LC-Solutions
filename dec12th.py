class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort(reverse=True)
        for i in range(k):
            gifts[0] = floor(gifts[0] ** 0.5)
            gifts.sort(reverse=True)
        return sum(gifts)