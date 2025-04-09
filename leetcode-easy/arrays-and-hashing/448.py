# LeetCode Question 
    ## 448. Find All Numbers Disappeared in an Array
# LeetCode Link
    ## https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=8i-f24YFWC4&ab_channel=NeetCode


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        final = []
        s = set(nums)
        for i in range(1, len(nums)+1):
            if i not in s:
                final.append(i)

        return final
        

sol = Solution()

# Example 1
nums1 = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(nums1))

# Example 2
nums2 = [1,1]
print(sol.findDisappearedNumbers(nums2))
