# LeetCode Question 
    ## 1608. Special Array With X Elements Greater Than or Equal X
# LeetCode Link
    ## https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=Z51jYCeBLVI&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(0, len(nums)+1):
            if (self.count(nums, i) == i):
                return i
        return -1

    def count(self, nums, x):
        _count = 0
        for each in nums:
            if each >= x:
                _count += 1
        return _count


sol = Solution()

# Example 1
nums1 = [3,5]
print(sol.specialArray(nums1))

# Example 2
nums2 = [0,0]
print(sol.specialArray(nums2))

# Example 3
nums3 = [0,4,3,0,4]
print(sol.specialArray(nums3))
