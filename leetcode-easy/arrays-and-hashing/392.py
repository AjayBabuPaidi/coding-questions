# LeetCode Question 
    ## 392. Is Subsequence
# LeetCode Link
    ## https://leetcode.com/problems/is-subsequence/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=99RVfqklbCE&ab_channel=NeetCode


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        m = len(s)
        n = len(t)
        i = 0
        j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == m:
            return True
        return False


sol = Solution()

# Example 1
s1 = "abc"
t1 = "ahbgdc"
print(sol.isSubsequence(s1, t1))

# Example 2
s2 = "axc"
t2 = "ahbgdc"
print(sol.isSubsequence(s2, t2))