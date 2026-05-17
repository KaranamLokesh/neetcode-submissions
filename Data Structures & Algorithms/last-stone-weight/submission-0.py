class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x,y)
            if x < y:
                heapq.heappush(stones,-(y - x))
        stones.append(0)
        return abs(stones[0])
            

    