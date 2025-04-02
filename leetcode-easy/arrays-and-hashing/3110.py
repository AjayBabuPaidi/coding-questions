# LeetCode Question 
    ## 3110. Score of a String
# LeetCode Link
    ## https://leetcode.com/problems/score-of-a-string/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=imbrLFL20tQ&ab_channel=NeetCodeIO


class Solution:
    def scoreOfString(self, s: str) -> int:
        _sum = 0
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                _sum = _sum + abs(ord(s[i]) - ord(s[j]))
                break
        return _sum


sol = Solution()

# Example 1
s1 = "hello"
print(sol.scoreOfString(s1))

# Example 2
s2 = "zaz"
print(sol.scoreOfString(s2))


