class Solution:
    def calc_rate(self, k:int, piles:List[int]) -> int:
        ## calculate the rate of eating here
        hours = 0
        for i in range(len(piles)):
            hours+= math.ceil(piles[i]/k)
        return hours
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        while low < high:
            ## calculate mid based on the predicate function below
            ## this is a lower mid as mid is extending 
            mid = low + (high - low)//2


            ## we are aiming for first T in here, 
            ## ex: piles = [1,4,3,2], h = 9,
            ## 1,2,3,4,5,6,7,8,9
            ## F,T,T,T,T,T,T,T,T

            if self.calc_rate(mid, piles) > h:
                low = mid + 1
            else:
                high = mid
            
        return low
            


        