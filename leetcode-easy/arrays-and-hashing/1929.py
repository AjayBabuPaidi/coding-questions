# LeetCode Question 
    ## 1929. Concatenation of Array
# LeetCode Link
    ## https://leetcode.com/problems/concatenation-of-array/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=68isPRHgcFQ&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    

sol = Solution()

# Example 1
nums1 = [1,2,1]
print(sol.getConcatenation(nums1))

# Example 2
nums2 = [1,3,2,1]
print(sol.getConcatenation(nums2))