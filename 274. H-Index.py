class Solution:
    def hIndex(self, cites: list[int]) -> int:
        cites.sort(reverse=True)
        h = 0
        for i, c in enumerate(cites, 1):
            if c >= i:
                h = i
        return h
