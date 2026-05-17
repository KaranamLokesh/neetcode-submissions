class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(heap,[-distance, point])
            if len(heap)>k:
                heapq.heappop(heap)
        answer = []
        for d, point in heap:
            answer.append(point)
        return answer




        # point = [6,8]
        # dist = 10
        # heap = [[10, [6,8]], [5, [3,4]]]

        # heapq.heapify(heap)
        # print(heap)

        