# LeetCode Question 
    ## 1913. Maximum Product Difference Between Two Pairs
# LeetCode Link
    ## https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=d-ulaeRBA64&ab_channel=NeetCodeIO



from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        new_nums = sorted(nums, reverse=True)
        return (new_nums[0] * new_nums[1]) - (new_nums[-1] * new_nums[-2])
    
sol = Solution()

# Example 1
nums1 = [5,6,2,7,4]
print(sol.maxProductDifference(nums1))

# Example 2
nums2 = [4,2,5,9,7,4,8]
print(sol.maxProductDifference(nums2))