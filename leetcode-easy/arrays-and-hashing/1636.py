# LeetCode Question 
    ## 1636. Sort Array by Increasing Frequency
# LeetCode Link
    ## https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=Evq1SfUbhBg&ab_channel=NeetCodeIO


from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        result = []
        sorted_dick = dict(sorted(d.items(), key = lambda x: (x[1], -x[0])))
        for k,v in sorted_dick.items():
            result.extend([k] * v)
        return result
    
sol = Solution()

# Example 1
nums1 = [1,1,2,2,2,3]
print(sol.frequencySort(nums1))

# Example 2
nums2 = [2,3,1,3,2]
print(sol.frequencySort(nums2))

# Example 3
nums3 = [-1,1,-6,4,5,-6,1,4,1]
print(sol.frequencySort(nums3))