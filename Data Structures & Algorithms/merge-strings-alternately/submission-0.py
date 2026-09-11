class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1 = len(word1)
        len_2 = len(word2)
        final_string = ''
        i = j = 0
        while i < len_1 and j < len_2:
            final_string += word1[i] + word2[j]
            i += 1
            j += 1

        if i < len_1:
            final_string += word1[i:]
        final_string += word2[j:]
        return final_string
        