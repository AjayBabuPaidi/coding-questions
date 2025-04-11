# LeetCode Question 
    ## 496. Next Greater Element I
# LeetCode Link
    ## https://leetcode.com/problems/next-greater-element-i/description/
# NeetCode Explanation
    ## https://www.youtube.com/watch?v=68a1Dc_qVq4&ab_channel=NeetCode


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        final = []
        for i in range(len(nums2)):
            d[nums2[i]] = i
    
        for each_num in nums1:
            index_of_num = d[each_num]
            _max = -1
            for j in range(index_of_num+1, len(nums2)):
                if nums2[j] > each_num:
                    _max = nums2[j]
                    break
            final.append(_max)
        
        return final
    
sol = Solution()

# Example 1
nums11 = [4,1,2]
nums21 = [1,3,4,2]
print(sol.nextGreaterElement(nums11, nums21))

# Example 2
nums12 = [2, 4]
nums22 = [1,2,3,4]
print(sol.nextGreaterElement(nums12, nums22))