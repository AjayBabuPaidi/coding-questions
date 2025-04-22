# LeetCode Question 
    ## 28. Find the Index of the First Occurrence in a String
# LeetCode Link
    ## https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=JoF0Z7nVSrA&ab_channel=NeetCode


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(0, len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                return i

        return -1
        
sol = Solution()

# Example 1
haystack1 = "sadbutsad"
needle1 = "sad"
print(sol.strStr(haystack1, needle1))

# Example 2
haystack2 = "leetcode"
needle2 = "leeto"
print(sol.strStr(haystack2, needle2))
