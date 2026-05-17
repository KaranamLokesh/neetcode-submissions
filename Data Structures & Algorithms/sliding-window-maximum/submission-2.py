class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i in range(len(nums)-k+1):
            max_el = -10000
            for j in range(i,k+i):
                if nums[j]>max_el:
                    max_el = nums[j]
            answer.append(max_el)
        return answer


        