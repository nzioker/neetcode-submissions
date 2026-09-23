from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        str_counter = defaultdict(int)

        for r in range(len(s)):
            str_counter[s[r]] += 1

            while str_counter[s[r]] > 1:
                str_counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        return longest
        