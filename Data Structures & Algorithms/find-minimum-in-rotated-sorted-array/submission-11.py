class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] < nums[n-1]:
            return nums[0]
        low, high = 0, n-1
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        return nums[low]
        