class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort nums first to handle duplicates easily
        answer = []
        
        for i in range(len(nums)):
            # Skip duplicate elements for i as we search for same combination with same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    triplet = [nums[i], nums[j], complement]
                    answer.append(triplet)
                    # Skip duplicates for j
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
        
        # Remove duplicates by converting to a set of tuples and back to list
        unique_answer = set(tuple(sorted(triplet)) for triplet in answer)
        return [list(triplet) for triplet in unique_answer]

        