# LeetCode Question 
    ## 1512. Number of Good Pairs
# LeetCode Link
    ## https://leetcode.com/problems/number-of-good-pairs/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=BqhDFUo1rjs&ab_channel=NeetCodeIO

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    count += 1
        return count
sol = Solution()

# Example 1
nums1 = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums1))

# Example 2
nums2 = [1,1,1,1]
print(sol.numIdenticalPairs(nums2))


# Example 3
nums3 = [1,2,3]
print(sol.numIdenticalPairs(nums3))


        