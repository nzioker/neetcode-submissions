class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def b_search(nums, target):
            l,r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return True
            return False
        all_nums = []
        for i in matrix:
            all_nums.extend(i)
        return b_search(all_nums, target)