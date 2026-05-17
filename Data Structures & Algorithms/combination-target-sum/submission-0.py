class Solution:
    def sum_helper(self, nums, index, target, res, temp):
        if target ==0:
            res.append(temp.copy())
            return
        elif target < 0:
            return
        
        for i in range(index,len(nums)):
            
            temp.append(nums[i])
            self.sum_helper(nums, i, target-nums[i], res, temp)
            temp.pop()



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        self.sum_helper(nums, 0, target, res, temp)
        return res

        
        