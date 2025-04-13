# LeetCode Question 
    ## 349. Intersection of Two Arrays
# LeetCode Link
    ## https://leetcode.com/problems/intersection-of-two-arrays/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=fwUTXaMom6U&ab_channel=NeetCodeIO



from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        final = set()
        for each_num in nums2:
            if each_num in s1:
                final.add(each_num)
        return list(final)
    
sol = Solution()

# Example 1
nums11 = [1,2,2,1]
nums21 = [2,2]
print(sol.intersection(nums11, nums21))

# Example 2
nums12 = [4,9,5]
nums22 = [9,4,9,8,4]
print(sol.intersection(nums12, nums22))
