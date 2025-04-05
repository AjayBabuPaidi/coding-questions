# LeetCode Question 
    ## 58. Length of Last Word
# LeetCode Link
    ## https://leetcode.com/problems/length-of-last-word/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=KT9rltZTybQ&ab_channel=NeetCode


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped_string = s.strip()
        words_array = stripped_string.split(" ")
        return len(words_array[-1])
    

sol = Solution()

# Example 1
s1 = "Hello World"
print(sol.lengthOfLastWord(s1))

# Example 2
s2 = "   fly me   to   the moon  "
print(sol.lengthOfLastWord(s2))

# Example 3
s3 = "luffy is still joyboy"
print(sol.lengthOfLastWord(s3))
        