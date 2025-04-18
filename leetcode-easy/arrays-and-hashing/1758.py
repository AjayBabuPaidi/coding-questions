# LeetCode Question 
    ## 1758. Minimum Changes To Make Alternating Binary String
# LeetCode Link
    ## https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=9vAQdmVU2ds&ab_channel=NeetCodeIO


class Solution:
    def minOperations(self, s: str) -> int:
        start_zero = "01" * (len(s) // 2)
        start_one = "10" * (len(s)//2)
        x = 0
        y = 0
        if len(s) % 2 != 0:
             start_zero += "0"
             start_one += "1"
        for i in range(len(s)):
            if s[i] != start_zero[i]:
                x += 1
            if s[i] != start_one[i]:
                y += 1
        return min(x,y)


sol = Solution()

# Example 1
s1 = "0100"
print(sol.minOperations(s1))

# Example 2
s2 = "10"
print(sol.minOperations(s2))

# Example 3
s3 = "1111"
print(sol.minOperations(s3))

# Example 4
s4 = "101101111"
print(sol.minOperations(s4))
