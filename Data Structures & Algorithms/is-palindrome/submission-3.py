class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string = ''.join(c.lower() for c in s if c.isalnum())
            
        l,r = 0, len(valid_string) - 1
        while l <= r:
            if valid_string[l] != valid_string[r]:
                return False
            l += 1
            r -= 1
        return True
        