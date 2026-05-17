class Solution:
    def permute_helper(self, nums, index, visited, res, temp):
        if len(temp) == len(nums):
            res.append(temp.copy())
            return


        for i in range(len(nums)):
            if visited[i] == False:
                visited[i] = True
                temp.append(nums[i])
                self.permute_helper(nums, i, visited, res, temp)
                temp.pop()
                visited[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False]* len(nums)
        res = []
        temp = []
        self.permute_helper(nums, 0, visited, res, temp)
        return res



        