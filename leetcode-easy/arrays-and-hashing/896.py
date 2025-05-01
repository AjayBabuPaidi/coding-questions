# LeetCode Question 
    ## 896. Monotonic Array
# LeetCode Link
    ## https://leetcode.com/problems/monotonic-array/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=sqWOFIZ9Z0U&ab_channel=NeetCodeIO

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        res1 = True
        res2 = True
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                res1 = False
                break

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                continue
            else:
                res2 = False
                break
        
        return res1 or res2
    

sol = Solution()

# Example 1
nums1 = [1,2,2,3]
print(sol.isMonotonic(nums1))

# Example 2
nums2 = [6,5,4,4]
print(sol.isMonotonic(nums2))

# Example 3
nums3 = [1,3,2]
print(sol.isMonotonic(nums3))