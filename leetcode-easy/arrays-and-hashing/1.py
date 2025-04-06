# LeetCode Question 
    ## 1. Two Sum
# LeetCode Link
    ## https://leetcode.com/problems/two-sum/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
                
sol = Solution()

# Example 1
nums1 = [2,7,11,15]
target1 = 9
print(sol.twoSum(nums1, target1))

# Example 2
nums2 = [3,2,4]
target2 = 6
print(sol.twoSum(nums2, target2))

# Example 3
nums3 = [3,3]
target3 = 6
print(sol.twoSum(nums3, target3))