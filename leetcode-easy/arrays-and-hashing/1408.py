# LeetCode Question 
    ## 1408. String Matching in an Array
# LeetCode Link
    ## https://leetcode.com/problems/string-matching-in-an-array/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=7K2BjgjCFDo&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        final = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    final.add(words[i])
        return list(final)

sol = Solution()

# Example 1
words1 = ["mass","as","hero","superhero"]
print(sol.stringMatching(words1))

# Example 2
words2 = ["leetcode","et","code"]
print(sol.stringMatching(words2))

# Example 3
words3 = ["blue","green","bu"]
print(sol.stringMatching(words3))