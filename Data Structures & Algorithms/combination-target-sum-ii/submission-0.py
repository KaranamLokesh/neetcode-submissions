class Solution:
    # the idea is to divide the arguments into 3 parts
    # 1. sub problem, (candidates, index, target) this includes all the variables we need for the sub problem
    # 2. final result variable, res, to store the entire result
    # 3. temp result variable, that stores the result of each step and it will be sued in base case to populate the final result
    
    def sum_helper(self, candidates, index, target, res, temp):
        if target ==0:
            res.append(temp.copy())
            return
        elif target < 0:
            return
        # this is a combination of subsets problem, and combination sum 1,
        # the idea is if we have enumerated for a number, we need not enumerate for the same number again, so we skip
        # and i > index is used to skip the duplicates, we are checking current element to the previous element,
        # but are not checking the first element,
        ## eg: lets say we have 1,1,1,2,3. in the first iteration, nums[i] == nums[i-1], this condition will not hold,
        # we already enumerate for the first 1, then we go to second 1,
#         Why Do We Need i > index?
# i > index ensures you only skip duplicates after the first occurrence at the current recursion level.

# The first occurrence (when i == index) is always allowed.

# You only skip the subsequent occurrences (when i > index), which would otherwise generate duplicate combinations. 
        for i in range(index, len(candidates)):
            if candidates[i] == candidates[i-1] and i > index:
                continue
            temp.append(candidates[i])
            self.sum_helper(candidates, i+1, target - candidates[i], res, temp)
            temp.pop()
            

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        temp = []
        self.sum_helper(candidates, 0, target, res, temp)
        return res
        