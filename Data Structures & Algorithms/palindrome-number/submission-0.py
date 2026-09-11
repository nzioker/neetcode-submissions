class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        l,r = 0, len(x_list) - 1

        while l <= r:
            if x_list[l] != x_list[r]:
                return False
            l += 1
            r -= 1
        return True
        