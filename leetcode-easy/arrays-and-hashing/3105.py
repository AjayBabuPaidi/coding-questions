# LeetCode Question 
    ## 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# LeetCode Link
    ## https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=zDbApBI7UpE&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        _max = 1
        dec_count = 1
        inc_count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_count += 1
                dec_count = 1
            elif nums[i] < nums[i-1]:
                dec_count += 1
                inc_count = 1
            else:
                dec_count = 1
                inc_count = 1
            _max = max(_max, dec_count, inc_count)
        return _max


        
sol = Solution()

# Example 1
nums1 = [1,4,3,3,2]
print(sol.longestMonotonicSubarray(nums1))

# Example 2
nums1 = [3,3,3,3]
print(sol.longestMonotonicSubarray(nums1))
