# LeetCode Question 
    ## 1897. Redistribute Characters to Make All Strings Equal
# LeetCode Link
    ## https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=a3SmUiimBi8&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        n = len(words)
        for each_word in words:
            for each_char in each_word:
                d[each_char] = d.get(each_char, 0) + 1
        for v in d.values():
            if v%n != 0:
                return False
        return True
        
sol = Solution()

# Example 1
words1 = ["abc","aabc","bc"]
print(sol.makeEqual(words1))

# Example 2
words2 = ["ab","a"]
print(sol.makeEqual(words2))
    