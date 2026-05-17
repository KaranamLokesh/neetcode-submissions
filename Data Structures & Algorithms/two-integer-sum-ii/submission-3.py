class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = defaultdict(set)
        # for i in range(len(numbers)):
        #     if target - numbers[i] in seen:
        #         return [seen[target-numbers[i]], i+1]
        #     seen[numbers[i]]=i+1
        l=0
        r = len(numbers)-1
        while l < r:
            if numbers[l]+ numbers[r]>target:
                r-=1
            elif numbers[l]+ numbers[r]<target:
                l+=1
            else:
                return [l+1,r+1]
        return []


            

        
        