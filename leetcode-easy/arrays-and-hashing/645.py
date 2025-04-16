# LeetCode Question 
    ## 645. Set Mismatch
# LeetCode Link
    ## https://leetcode.com/problems/set-mismatch/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=d-ulaeRBA64&ab_channel=NeetCodeIO


from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        _max = len(nums)
        d = {}
        final = [0, 0]
        for each in nums:
            d[each] = d.get(each,0) + 1
        for i in range(1, _max+1):
            if d.get(i, 0) == 2:
                final[0] = i
                break
        for i in range(1, _max+1):
            if i not in d:
                final[1] = i
                break
        return final



sol = Solution()

# Example 1
nums1 = [1,2,2,4]
print(sol.findErrorNums(nums1))

# Example 2
nums2 = [1,1]
print(sol.findErrorNums(nums2))