from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = defaultdict(list)
        for i in strs:
            sorted_str = "".join(sorted(i))
            solution[sorted_str].append(i)
        return list(solution.values())
        