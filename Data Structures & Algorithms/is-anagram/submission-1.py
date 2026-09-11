class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sol_s = {}
        for i in s:
            if i in sol_s.keys():
                sol_s[i] += 1
            else:
                sol_s[i] = 1

        sol_t = {}
        for i in t:
            if i in sol_t.keys():
                sol_t[i] += 1
            else:
                sol_t[i] = 1

        return sol_s == sol_t
        