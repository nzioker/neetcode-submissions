class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for i in strs:
            sorted_str = "".join(sorted(i))

            if sorted_str in solution:
                solution[sorted_str].append(i)
            else:
                solution[sorted_str] = [i]
        return [i for i in solution.values()]
        