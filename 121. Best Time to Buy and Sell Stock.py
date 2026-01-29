class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float('inf')
        gain = 0
        for p in prices:
            if p < low:
                low = p
            elif p - low > gain:
                gain = p - low
        return gain
