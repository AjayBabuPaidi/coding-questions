# LeetCode Question 
    ## 1051. Height Checker
# LeetCode Link
    ## https://leetcode.com/problems/height-checker/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=mQAoeYaE3Xk&ab_channel=NeetCodeIO




from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expec = sorted(heights)
        final = 0

        for i in range(len(heights)):
            if heights[i] != expec[i]:
                final += 1
        return final
    

sol = Solution()

# Example 1
heights1 = [1,1,4,2,1,3]
print(sol.heightChecker(heights1))

# Example 2
heights2 = [5,1,2,3,4]
print(sol.heightChecker(heights2))

# Example 3
heights3 = [1,2,3,4,5]
print(sol.heightChecker(heights3))
        