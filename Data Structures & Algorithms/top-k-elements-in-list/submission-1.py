import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for num in nums:
            ans[num]+=1
        l=[]
        sorted_dict = dict(sorted(ans.items(), key=lambda item:item[1], reverse=True))
        for n in sorted_dict:
            l.append(n)
        return l[:k]




        