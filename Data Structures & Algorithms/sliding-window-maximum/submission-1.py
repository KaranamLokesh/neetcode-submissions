class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result =[]
        heap = []
        for i in range(len(nums)):
            ## heap by default in python is min heap by default, but in c++ it is max heap
            ## it means the minimum number will be stored at the top, so we use - sign to make it bigger
            heapq.heappush(heap,(-nums[i], i))
            if i >=k-1:
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
        return result



        