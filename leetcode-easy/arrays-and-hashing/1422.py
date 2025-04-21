# LeetCode Question 
    ## 1422. Maximum Score After Splitting a String
# LeetCode Link
    ## https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=mc_eSStDrWw&ab_channel=NeetCodeIO


class Solution:
    def maxScore(self, s: str) -> int:
        d1 = {}
        left_to_right = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left_to_right += 1
            d1[i] = left_to_right

        d2 = {}
        right_to_left = 0
        for i in range(len(s)-1, 0, -1):
            if s[i] == '1':
                right_to_left += 1
            d2[i] = right_to_left

        _max = float('-inf')
        for i in range(len(d1)):
            temp = d1[i] + d2[i+1]
            if temp > _max:
                _max = temp
        return _max

        
sol = Solution()

# Example 1
s1 = "011101"
print(sol.maxScore(s1))

# Example 2
s2 = "00111"
print(sol.maxScore(s2))

# Example 3
s3 = "1111"
print(sol.maxScore(s3))