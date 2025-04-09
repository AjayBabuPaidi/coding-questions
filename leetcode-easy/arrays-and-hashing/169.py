# LeetCode Question 
    ## 169. Majority Element
# LeetCode Link
    ## https://leetcode.com/problems/majority-element/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=7pnhv842keE&ab_channel=NeetCode


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for each_num in nums:
            d[each_num] = d.get(each_num, 0) + 1
        
        for k,v in d.items():
            if v > n//2:
                return k
        
sol = Solution()

# Example 1
nums1 = [3,2,3]
print(sol.majorityElement(nums1))

# Example 2
nums2 = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums2))


