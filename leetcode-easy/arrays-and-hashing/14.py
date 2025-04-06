# LeetCode Question 
    ## 14. Longest Common Prefix
# LeetCode Link
    ## https://leetcode.com/problems/longest-common-prefix/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=0sWShKIJoo4&ab_channel=NeetCode


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # finding the smallest word in the list
        min_length = float("inf")
        smallest_word = None
        for each_word in strs:
            if len(each_word) < min_length:
                smallest_word = each_word
                min_length = len(each_word)

        common_prefix = ""
        for i in range(len(smallest_word)):
            for each in strs:
                if smallest_word[i] != each[i]:
                    return common_prefix
            
            common_prefix += smallest_word[i]

        return common_prefix
    
sol = Solution()

# Example 1
strs1 = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs1))

# Example 2
strs2 = ["dog","racecar","car"]
print(sol.longestCommonPrefix(strs2))