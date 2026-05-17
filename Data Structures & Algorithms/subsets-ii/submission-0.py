class Solution:
    def subset_helper(self, nums, index, res, temp):
        res.append(temp.copy())

        for i in range(index, len(nums)):
            if nums[i] == nums[i-1] and i > index:
                continue
            temp.append(nums[i])
            self.subset_helper(nums, i+1, res, temp)
            temp.pop()


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        self.subset_helper(nums, 0, res, temp)
        return res

        
        