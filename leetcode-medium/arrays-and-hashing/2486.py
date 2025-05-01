# LeetCode Question 
    ## 2486. Append Characters to String to Make Subsequence
# LeetCode Link
    ## https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=gKDmO8ZLRD8&ab_channel=NeetCodeIO


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i ,j, m, n = 0, 0, len(s), len(t)
        while (i < m and j < n):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return n - j 
        

sol = Solution()

# Example 1
s1 = "coaching"
t1 = "coding"
print(sol.appendCharacters(s1, t1))

# Example 2
s2 = "abcde"
t2 = "a"
print(sol.appendCharacters(s2, t2))


# Example 3
s3 = "z"
t3 = "abcde"
print(sol.appendCharacters(s3, t3))