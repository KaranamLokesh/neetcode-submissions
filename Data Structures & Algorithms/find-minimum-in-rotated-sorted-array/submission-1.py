class Solution:
    def is_found(self, mid:int, nums:List[int], high:int) -> bool:
        return (nums[mid]> nums[high])


    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low<high:
            ## calculate mid after predicate function is finalized
            mid = low + (high - low)//2
            # print(mid, low, high)
            if (self.is_found(mid, nums, high)):
                low = mid+1
            else:
                high = mid
        return nums[low]

        
        