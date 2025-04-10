# LeetCode Question 
    ## 387. First Unique Character in a String
# LeetCode Link
    ## https://leetcode.com/problems/first-unique-character-in-a-string/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=rBENYgWy3xU&ab_channel=NeetCodeIO


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


sol = Solution()

# Example 1
s1 = "leetcode"
print(sol.firstUniqChar(s1))

# Example 2
s2 = "loveleetcode"
print(sol.firstUniqChar(s2))

# Example 3
s3 = "aabb"
print(sol.firstUniqChar(s3))