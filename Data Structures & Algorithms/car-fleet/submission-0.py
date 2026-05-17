class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        divisors = []
        pair = [(p,s) for p,s in zip(position, speed)]
        ## making a pair and sorting in reverse, because we have to start from the car that is nearest to the
        ## target, if other car comes to the last car, it has to follow it with the same speed
        pair.sort(reverse=True)
        for i in range(len(pair)):
            divisors.append((target - pair[i][0])/pair[i][1])
            ## add two cars into stack, check if they can collide, if yes, remove the car that is farther from target
            if len(divisors)>=2 and divisors[-1]<=divisors[-2]:
                divisors.pop()
        return len(divisors)
        

        