class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}

        for idx, i in enumerate(nums):
            sol[i] = idx

        for idx, i in enumerate(nums):
            x = target - i
            if x in sol and sol[x] != idx:
                return sorted([idx,sol[x]])

        return []
        
        