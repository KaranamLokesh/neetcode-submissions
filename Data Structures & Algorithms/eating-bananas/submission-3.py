class Solution:
    def hrs_to_eat(self, mid, piles):
        ans = 0
        for i in range(len(piles)):
            ans += math.ceil(piles[i]/mid)
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high - low)//2
            if self.hrs_to_eat(mid, piles) > h:
                low = mid + 1
            else:
                high = mid
        return high

        