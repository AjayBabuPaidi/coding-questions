# LeetCode Question 
    ## 1624. Largest Substring Between Two Equal Characters
# LeetCode Link
    ## https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=66b2V_rCuJw&ab_channel=NeetCodeIO


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        se = set(s)
        _max = -2
        for each_char in se:
            _first = self.first_occurence(s, each_char)
            _last = self.last_occurence(s, each_char)
            if _last - _first > _max:
                _max = _last - _first

        return _max-1

    def first_occurence(self, s, ch):
        for i in range(len(s)):
            if s[i] == ch:
                return i

    def last_occurence(self, s, ch):
        for i in range(len(s)-1, -1, -1):
            if s[i] == ch:
                return i


sol = Solution()

# Example 1
s1 = "aa"
print(sol.maxLengthBetweenEqualCharacters(s1))

# Example 2
s2 = "abca"
print(sol.maxLengthBetweenEqualCharacters(s2))

# Example 3
s3 = "cbzxy"
print(sol.maxLengthBetweenEqualCharacters(s3))
    
        