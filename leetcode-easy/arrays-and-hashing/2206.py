# LeetCode Question 
    ## 2206. Divide Array Into Equal Pairs
# LeetCode Link
    ## https://leetcode.com/problems/divide-array-into-equal-pairs/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=vxcpdClAktE&ab_channel=NeetCodeIO



from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        n = len(nums) // 2
        _cnt = 0
        for k,v in d.items():
            _cnt += v//2
        return _cnt == n
    

sol = Solution()

# Example 1
nums1 = [3,2,3,2,2,2]
print(sol.divideArray(nums1))

# Example 2
nums2 = [1,2,3,4]
print(sol.divideArray(nums2))