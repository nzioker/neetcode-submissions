class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        def can_eat(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h

        while l < r:
            mid = l + (r-l)//2
            
            if can_eat(mid):
                r = mid
            else:
                l = mid + 1
        return l
        