class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_counter = {}
        for i in nums:
            if i in dict_counter.keys():
                dict_counter[i] += 1
            else:
                dict_counter[i] = 1

        for i in dict_counter.values():
            if i > 1:
                return True
        return False
        
        