# LeetCode Question 
    ## 242. Valid Anagram
# LeetCode Link
    ## https://leetcode.com/problems/valid-anagram/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=9UtInBqnCgA&ab_channel=NeetCode


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        return d1 == d2



sol = Solution()

# Example 1
s1 = "anagram"
t1 = "nagaram"
print(sol.isAnagram(s1, t1))

# Example 2
s2 = "rat"
t2 = "car"
print(sol.isAnagram(s2, t2))