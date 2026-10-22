from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        sorted_freq = sorted(freq_counter.keys(), key=lambda x:freq_counter[x], reverse=True)

        return sorted_freq[:k]
        