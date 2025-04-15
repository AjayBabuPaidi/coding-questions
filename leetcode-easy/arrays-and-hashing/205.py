# LeetCode Question 
    ## 205. Isomorphic Strings
# LeetCode Link
    ## https://leetcode.com/problems/isomorphic-strings/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=7yF-U1hLEqQ&ab_channel=NeetCode



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] in d1 and d1[s[i]] != t[i]:
                return False
            d1[s[i]] = t[i]

            if t[i] in d2 and d2[t[i]] != s[i]:
                return False
            d2[t[i]] = s[i]

        return True
        

sol = Solution()

# Example 1
s1 = "egg"
t1 = "add"
print(sol.isIsomorphic(s1, t1))

# Example 2
s2 = "foo"
t2 = "bar"
print(sol.isIsomorphic(s2, t2))
