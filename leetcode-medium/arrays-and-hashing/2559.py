# LeetCode Question 
    ## 2559. Count Vowel Strings in Ranges
# LeetCode Link
    ## https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=TLJd7W-z-yc&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        precompute = [0] * len(words)
        final = []
        till = 0
        i = 0
        for each_word in words:
            if each_word[0] in vowels and each_word[-1] in vowels:
                till += 1
            precompute[i] = till
            i += 1
        for each_query in queries:
            if each_query[0] == 0:
                final.append(precompute[each_query[1]])
            else:
                up = precompute[each_query[1]]
                low = precompute[each_query[0] - 1]
                final.append(up - low)
        return final
        

sol = Solution()

# Example 1
words1 = ["aba","bcb","ece","aa","e"]
queries1 = [[0,2],[1,4],[1,1]]
print(sol.vowelStrings(words1, queries1))

# Example 2
words2 = ["a","e","i"]
queries2 = [[0,2],[0,1],[2,2]]
print(sol.vowelStrings(words2, queries2))