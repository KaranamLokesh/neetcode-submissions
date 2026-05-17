from typing import List

class Solution:
    def bin_search(self, low: int, high: int, nums: List[int], target: int) -> int:
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        # Find the index of the smallest element (pivot)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        pivot = low

        # Determine which part of the array to search
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            return self.bin_search(pivot, len(nums) - 1, nums, target)
        else:
            return self.bin_search(0, pivot - 1, nums, target)
