# LeetCode Question 
    ## 409. Longest Palindrome
# LeetCode Link
    ## https://leetcode.com/problems/longest-palindrome/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=_g9jrLuAphs&ab_channel=NeetCodeIO


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        final = 0
        for each_char in s:
            d[each_char] = d.get(each_char, 0) + 1
        for k,v in d.items():
            if v % 2 == 0:
                final = final + v
                d[k] = 0
            else:
                final = final + (2 * (v//2))
                d[k] = v % 2
        for v in d.values():
            if v == 1:
                final = final + 1
                break
        return final
            

sol = Solution()

# Example 1
s1 = "abccccdd"
print(sol.longestPalindrome(s1))

# Example 2
s2 = "a"
print(sol.longestPalindrome(s2))
    
