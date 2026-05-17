class Solution:
    def is_found(self, mid:int, nums:List[int]) -> bool:
        return (nums[mid] < nums[0]) 


    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low<high:
            ## calculate mid after predicate function is finalized
            mid = low + (high - low)//2
            # print(mid, low, high)
            if (self.is_found(mid, nums)):
                high = mid
            else:
                low = mid+1
        if nums[0] < nums[low]:
            return nums[0]
        elif nums[len(nums)-1] < nums[low]:
            return nums[len(nums)-1]
        else:
            return nums[low]

        
        