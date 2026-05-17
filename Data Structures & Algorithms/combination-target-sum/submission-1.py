class Solution:
    def sum_helper(self, nums, index, target, res, temp):
        if target ==0:
            res.append(temp.copy())
            return
        elif target < 0:
            return
        # The main idea is to include the same element again and again till it becomes equal to or less than
        # target, once the target becomes negative, we remove the last element inserted and then insert the new element
        # in this way, we are identifying all the possible solutions of including the same element in the solution
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

        
        