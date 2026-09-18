class Solution:
    ## find smallest element index in the array using binary search
    def bs_helper(self, nums):
        low = 0
        high = len(nums)-1

        # optimization
        if nums[low] < nums[high]:
            return low
        # normal binary search
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid 
        return low
    # after identifying the part where element is, it is now normal binary search
    def bs(self, nums, low, high, target):
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid+1  
        if nums[low] == target:
            return low
        return -1

    def search(self, nums: List[int], target: int) -> int:
        smallest_index = self.bs_helper(nums)
        n = len(nums)
        print(smallest_index)
        if nums[smallest_index] == target:
            return smallest_index
        elif nums[smallest_index] < target and nums[n-1] >= target:
            return self.bs(nums, smallest_index, n, target)
        else:
            return self.bs(nums, 0, smallest_index, target)
        

        