class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def helper(x):
            x_d = {}
            for i in x:
                if i in x_d.keys():
                    x_d[i] += 1
                else:
                    x_d[i] = 1
            return x_d

        return helper(s) == helper(t)
        