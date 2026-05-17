class Solution:
    def backtrack(self, nums, interim, result, start, n):
        if start == n:
            result.append(interim.copy())
            return
        interim.append(nums[start])
        self.backtrack(nums, interim, result, start+1, n)
        interim.pop()
        self.backtrack(nums, interim, result, start+1, n)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        interim = []
        n = len(nums)
        self.backtrack(nums, interim, result, 0, n)
        return result

        
        