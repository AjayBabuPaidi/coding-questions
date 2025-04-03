# LeetCode Question 
    ## 217. Contains Duplicate
# LeetCode Link
    ## https://leetcode.com/problems/contains-duplicate/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=3OamzN90kPg&ab_channel=NeetCode


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
            if d.get(nums[i], 0) == 2:
                return True
        return False


sol = Solution()

# Example 1
nums1 = [1,2,3,1]
print(sol.containsDuplicate(nums1))

# Example 2
nums2 = [1,2,3,4]
print(sol.containsDuplicate(nums2))

# Example 3
nums3 = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(nums3))
        