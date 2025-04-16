# LeetCode Question 
    ## 3151. Special Array I
# LeetCode Link
    ## https://leetcode.com/problems/special-array-i/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=RY6P9V878-0&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i-1] % 2 == 0 and nums[i] % 2 != 0) or (nums[i-1] % 2 != 0 and nums[i] % 2 == 0):
                continue
            else:
                return False
        return True
        

sol = Solution()

# Example 1
nums1 = [1]
print(sol.isArraySpecial(nums1))

# Example 2
nums2 = [2,1,4]
print(sol.isArraySpecial(nums2))

# Example 3
nums3 = [4,3,1,6]
print(sol.isArraySpecial(nums3))