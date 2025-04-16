# LeetCode Question 
    ## 290. Word Pattern
# LeetCode Link
    ## https://leetcode.com/problems/word-pattern/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=W_akoecmCbM&ab_channel=NeetCode



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1 = {}
        d2 = {}
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] in d1 and d1[pattern[i]] != s_list[i]:
                return False
            d1[pattern[i]] = s_list[i]

            if s_list[i] in d2 and d2[s_list[i]] != pattern[i]:
                return False
            d2[s_list[i]] = pattern[i]
    
        return True
    
        
sol = Solution()

# Example 1
pattern1 = "abba"
s1 = "dog cat cat dog"
print(sol.wordPattern(pattern1, s1))

# Example 2
pattern2 = "abba"
s2 = "dog cat cat fish"
print(sol.wordPattern(pattern2, s2))

# Example 3
pattern3 = "aaaa"
s3 = "dog cat cat dog"
print(sol.wordPattern(pattern3, s3))

