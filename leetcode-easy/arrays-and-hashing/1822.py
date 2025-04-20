# LeetCode Question 
    ## 1822. Sign of the Product of an Array
# LeetCode Link
    ## https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=ILDLM86jNow&ab_channel=NeetCodeIO



from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_numbers = 0
        for each in nums:
            if each == 0:
                return 0
            if each < 0:
                negative_numbers += 1
        if negative_numbers % 2 == 0:
            return 1
        return -1
    
sol = Solution()

# Example 1
nums1 = [-1,-2,-3,-4,3,2,1]
print(sol.arraySign(nums1))

# Example 2
nums2 = [1,5,0,2,-3]
print(sol.arraySign(nums2))

# Example 3
nums3 = [-1,1,-1,1,-1]
print(sol.arraySign(nums3))
        
        